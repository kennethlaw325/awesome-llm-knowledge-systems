"""Verify the recorded translation snapshot without requiring every future English edit to resync it."""
import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANGUAGES = {"zh", "zh-CN", "ja", "ko", "es"}

def digest(path):
    return hashlib.sha256(path.read_text(encoding="utf-8").encode("utf-8")).hexdigest()

def inside(path):
    candidate=(ROOT/path).resolve()
    if not candidate.is_relative_to(ROOT.resolve()):
        raise ValueError("manifest path escapes repository: "+path)
    return candidate

def check(require_current=False):
    manifest=json.loads((ROOT/"translations/sync-manifest.json").read_text(encoding="utf-8"))
    records=manifest["documents"];errors=[];stale=set();pairs=set();targets=set()
    if set(manifest["languages"])!=LANGUAGES or len(manifest["languages"])!=len(LANGUAGES):
        errors.append("language coverage differs from the five supported editions")
    if len(records)!=manifest["document_count"]:errors.append("document count does not match records")
    for item in records:
        pair=(item["language"],item["source"])
        lang,src=pair
        if src=="README.md":expected_target="translations/"+("README-zh.md" if lang=="zh" else "README_"+lang+".md")
        elif src=="glossary.md":expected_target="translations/glossary_"+lang+".md"
        else:expected_target="translations/chapters/"+lang+"/"+Path(src).name
        if item["translation"]!=expected_target:errors.append("wrong language/source target: "+item["translation"])
        if pair in pairs:errors.append("duplicate language/source pair: "+str(pair))
        pairs.add(pair)
        if item["translation"] in targets:errors.append("duplicate translation target: "+item["translation"])
        targets.add(item["translation"])
        source=inside(item["source"]);target=inside(item["translation"])
        if not source.is_file():errors.append("missing source: "+item["source"]);continue
        if not target.is_file():errors.append("missing translation: "+item["translation"]);continue
        if digest(source)!=item["source_sha256"]:stale.add(item["source"])
        elif len(source.read_text(encoding="utf-8").splitlines())!=item["source_lines"]:errors.append("source line count differs: "+item["source"])
        if digest(target)!=item["translation_sha256"]:errors.append("translation changed since review: "+item["translation"])
        body=re.sub(r'^<!-- translation-sync:start -->\n[\s\S]*?<!-- translation-sync:end -->\n\n','',target.read_text(encoding="utf-8"))
        body=re.sub(r'^<a id="[^"]+"></a><!-- i18n-anchor -->\n\n','',body,flags=re.M)
        if len(body.splitlines())!=item["translated_body_lines"]:errors.append("actual translation line count differs: "+item["translation"])
        if item["source_lines"]!=item["translated_body_lines"]:errors.append("recorded line count mismatch: "+item["translation"])
    sources={x["source"] for x in records}
    live_sources={"README.md","glossary.md",*[p.relative_to(ROOT).as_posix() for p in (ROOT/"chapters").glob("*.md")]}
    stale.update(sources.symmetric_difference(live_sources))
    expected={(lang,src) for lang in manifest["languages"] for src in sources}
    if pairs!=expected:errors.append("language/source coverage is incomplete")
    if sum(x["source_lines"] for x in records)!=manifest["aligned_source_lines"]:errors.append("aligned source-line total differs")
    if require_current and stale:errors.append("English sources changed since synchronization")
    for path in sorted(stale):print("::warning file="+path+"::Translation snapshot is dated; English has changed since synchronization")
    for error in errors:print("::error::"+error)
    print(json.dumps({"documents":len(records),"languages":len(manifest["languages"]),"stale_sources":len(stale),"errors":len(errors)}))
    return 1 if errors else 0

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--require-current",action="store_true",help="Require the translation snapshot to match the current English edition")
    raise SystemExit(check(parser.parse_args().require_current))
