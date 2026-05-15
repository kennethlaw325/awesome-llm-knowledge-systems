# Capítulo 01: Las tres generaciones

> **En una frase:** la ingeniería de IA ha evolucionado desde escribir buenos prompts hasta diseñar sistemas operativos enteros alrededor de los modelos de IA.
>
> **Por qué importa:** entender hacia dónde se dirige el campo ayuda a elegir las herramientas adecuadas y evitar enfoques desfasados.

**Del prompt engineering al context engineering y al harness engineering —— y por qué las fronteras entre ellos importan menos de lo que se piensa.**

---

## Generación 1: Prompt Engineering (2022–2024)

Cuando ChatGPT se lanzó en noviembre de 2022, toda la interfaz entre los humanos y los large language models era una caja de texto. La disciplina que emergió fue el prompt engineering: el arte y la ciencia de elaborar el texto de entrada para obtener mejores salidas.

Las técnicas centrales se desarrollaron con rapidez:

**Few-shot prompting** (Brown et al., 2020) demostró que incluir ejemplos en el prompt podía mejorar drásticamente el rendimiento de la tarea sin ningún fine-tuning. En vez de entrenar un modelo para clasificar sentimiento, se le mostraban tres ejemplos y se le pedía clasificar el cuarto.

**Chain-of-thought (CoT) prompting** (Wei et al., 2022) mostró que añadir "Let's think step by step" o incluir trazas de razonamiento en los ejemplos podía desbloquear capacidades de razonamiento multipaso que parecían ausentes en el prompting estándar. Esta fue, posiblemente, la primera pista de que *cómo se estructuraba el contexto* importaba tanto como *qué se preguntaba*.

**Prompt templates** se convirtió en la abstracción estándar. LangChain, LlamaIndex y decenas de frameworks ofrecieron sistemas de plantillas en los que se podían inyectar variables dentro de estructuras de prompt cuidadosamente diseñadas. El modelo mental era claro: el prompt es el programa, el modelo es el runtime.

Otras técnicas de esta era incluyen:

- **ReAct** (Yao et al., 2022): intercalar pasos de razonamiento y de acción, permitiendo a los modelos planificar y ejecutar llamadas a herramientas dentro de una única estructura de prompt.
- **Tree of Thought** (Yao et al., 2023): explorar múltiples caminos de razonamiento y seleccionar el mejor.
- **Self-consistency** (Wang et al., 2022): muestrear varias cadenas de razonamiento y tomar el voto mayoritario.

La limitación de esta era estaba en su supuesto: que la calidad de una interacción con un LLM se determinaba principalmente por la calidad del prompt. Esto era cierto cuando los context windows eran de 4K–8K tokens y la única entrada era el texto del usuario. Dejó de serlo en cuanto los modelos pudieron ingerir más de 100K tokens e invocar herramientas externas.

### Lo que esta era acertó

El prompt engineering estableció que *la estructura importa*. La diferencia entre un prompt bueno y uno malo no es intuición —— es arquitectura de la información. Esa idea se trasladó a todo lo que vino después.

### Lo que esta era pasó por alto

Trataba el context window como un artefacto estático. Se elaboraba un prompt, se enviaba y se obtenía una respuesta. La idea de que el propio context window podía ser *construido dinámicamente* a partir de múltiples fuentes en tiempo de ejecución —— esa fue la intuición de la siguiente generación.

---

## Generación 2: Context Engineering (2025)

A mediados de 2025, Andrej Karpathy publicó lo que se convirtió en una de las observaciones más compartidas en la comunidad de ingeniería de IA:

> "He estado pensando en esto y creo que el término correcto para aquello en lo que la mayoría de la gente realmente necesita mejorar no es 'prompt engineering' sino 'context engineering'. El arte y la ciencia de llenar el context window con la información justa para el siguiente paso."

Este reencuadre fue significativo porque desplazó la atención de la *instrucción* (prompt) al *paquete de información completo* (context window). El context window de una llamada moderna a un LLM contiene mucho más que un prompt de usuario:

- Instrucciones de sistema que definen el comportamiento y las restricciones
- Documentos recuperados de pipelines RAG
- Definiciones de herramientas y esquemas
- Historial de conversación (comprimido selectivamente)
- Ejemplos few-shot elegidos dinámicamente
- Metadatos estructurados sobre la tarea actual

El prompt es un componente. El context engineering consiste en orquestar todos ellos.

### Las seis técnicas

[El análisis de Towards AI](https://towardsai.net/) sobre context engineering identificó seis técnicas centrales que definen la disciplina:

1. **Retrieval-Augmented Generation (RAG)**: extraer documentos relevantes en el momento de la consulta
2. **Integración de tools y APIs**: dar a los modelos acceso a capacidades externas mediante esquemas estructurados
3. **Memory management**: mantener información relevante a lo largo de turnos de conversación y sesiones
4. **Construcción dinámica de prompts**: ensamblar prompts a partir de plantillas, contenido recuperado y estado en tiempo de ejecución
5. **Optimización del context window**: gestionar qué entra y qué se queda fuera de presupuestos de tokens limitados
6. **Jerarquía de instrucciones**: estratificar instrucciones de sistema, de desarrollador y de usuario con una precedencia clara

### Lecciones de Manus

[Manus](https://manus.im/), la plataforma de agentes de IA que se convirtió en uno de los productos más comentados de 2025, compartió lecciones críticas sobre context engineering a escala:

**La intuición sobre la KV-cache**: Manus diseñó su context window para mantener altas tasas de aciertos en la KV-cache —— asegurando que los pares clave-valor previamente computados en el mecanismo de atención pudieran reutilizarse entre turnos. Esto redujo drásticamente la latencia y el coste. El principio: estructura tu contexto de modo que el *prefijo permanezca estable* mientras solo el *sufijo cambia* entre llamadas.

**La proporción 100:1**: Manus reportó que por cada 1 token de salida del modelo se consumían aproximadamente 100 tokens de contexto. Esto invertía el supuesto común de que los tokens de salida eran el principal motor del coste. El verdadero reto de ingeniería no era generar texto —— era *seleccionar qué contexto alimentar*.

**El contexto como producto**: Manus trató la construcción del context window como una característica central del producto, no como un detalle de implementación. La calidad de su agente era directamente proporcional a la calidad de su pipeline de ensamblaje de contexto.

### El cambio de taxonomía

El context engineering reencuadró el desarrollo de aplicaciones LLM desde "escribir buenos prompts" hasta "construir buenas pipelines de información". El modelo se convirtió en un motor de razonamiento que operaba sobre el contexto que recibía. El reto de ingeniería se movió aguas arriba —— hacia la recuperación, el filtrado, el ranking, la compresión y el ensamblaje.

Pero incluso este encuadre tenía un techo. Describía *qué entra en el modelo* pero no *cómo opera el sistema alrededor del modelo*. Eso requería otro desplazamiento.

---

## Generación 3: Harness Engineering (2026)

Desde finales de 2025 hasta principios de 2026, dos textos influyentes formalizaron la siguiente evolución:

**Birgitta Böckeler** (ThoughtWorks), escribiendo en la serie de memorandos *Exploring Generative AI* de Martin Fowler en abril de 2026, publicó un análisis que sostenía que el trabajo de ingeniería más impactante en las aplicaciones LLM no estaba sucediendo en el entrenamiento del modelo ni en la elaboración del prompt, sino en *el harness* —— el sistema circundante de herramientas, enrutamiento, memoria, planificación y recuperación ante errores que orquesta las llamadas al modelo dentro de flujos de trabajo fiables.

**El equipo de Codex de OpenAI** ha publicado material de caso de estudio sobre el lado del harness de la codificación agéntica (véase openai.com/index/introducing-codex para el material público). La cifra ampliamente citada de "tres ingenieros / ~1M de líneas / ~1.500 PRs" circuló en charlas y publicaciones de OpenAI de 2025–2026; la observación subyacente es que la calidad de Codex se determinaba principalmente no por el modelo, sino por el harness —— el sistema que decidía *cuándo* llamar al modelo, *qué contexto* proporcionar, *qué herramientas* hacer disponibles y *cómo* validar y recuperarse de los errores.

### La analogía de Phil Schmid

[Phil Schmid](https://www.philschmid.de/) (Hugging Face) ofreció la analogía que cristalizó el concepto:

- **El modelo es la CPU** —— capacidad de cómputo en bruto
- **El context window es la RAM** —— la memoria de trabajo para la operación actual
- **El harness es el OS** —— planificación, gestión de recursos, I/O, manejo de errores e interfaz de usuario

Esta analogía aclara por qué importa el harness engineering: nadie envía una CPU sin un OS. El modelo es necesario pero no suficiente. El harness determina lo que el modelo puede lograr realmente.

### El paper Meta-Harness y la brecha 6x

Investigación publicada a principios de 2026 cuantificó lo que los practicantes ya sospechaban: la brecha entre un modelo desnudo y un modelo bien harnessed era de aproximadamente **6x en tareas complejas**. El mismo modelo, con los mismos pesos, con los mismos datos de entrenamiento, producía resultados que variaban por un factor de seis según la calidad de su harness.

Esto significaba que el harness engineering ofrecía más palanca que la mejora del modelo para la mayoría de las aplicaciones prácticas. Un mejor harness sobre un buen modelo superaba a un gran modelo con un harness mediocre.

### El framework IMPACT

En el discurso de practicantes de mediados de la década de 2020, el mnemónico IMPACT emergió como una checklist para evaluar la calidad del harness:

- **I**nstructions —— claridad y completitud de las instrucciones de sistema
- **M**emory —— persistencia y recuperación a través de sesiones
- **P**lanning —— descomposición y secuenciación de tareas
- **A**ctions —— disponibilidad y fiabilidad de herramientas
- **C**ontext —— ensamblaje dinámico de información relevante
- **T**esting —— bucles de evaluación y aseguramiento de calidad

IMPACT posiciona el context engineering como un componente (la "C") dentro de la disciplina más amplia del harness engineering. Este anidamiento es la clave estructural: el context engineering está *dentro* del harness engineering, no es reemplazado por él.

### Meta adquiere Manus (~$2B)

A principios de 2026, Meta adquirió Manus por aproximadamente 2.000 millones de dólares. La adquisición se interpretó ampliamente como que Meta compraba *el harness, no el modelo*. Meta ya tenía Llama. Lo que no tenía era un sistema probado en producción para ensamblaje de contexto, orquestación de herramientas y gestión del runtime del agente.

La adquisición validó la tesis: la ingeniería más valiosa en el ecosistema LLM se encontraba cada vez más en la capa de orquestación, no en la capa del modelo.

---

## La idea clave: coexistencia, no reemplazo

Estas tres generaciones no son periodos históricos limpios donde uno reemplaza al siguiente. Son *capas anidadas* que coexisten en todo sistema de producción:

```
+--------------------------------------------------+
|              HARNESS ENGINEERING                  |
|  +--------------------------------------------+  |
|  |          CONTEXT ENGINEERING                |  |
|  |  +--------------------------------------+  |  |
|  |  |       PROMPT ENGINEERING             |  |  |
|  |  |                                      |  |  |
|  |  |  System prompts, CoT, few-shot,      |  |  |
|  |  |  instruction formatting              |  |  |
|  |  +--------------------------------------+  |  |
|  |                                            |  |
|  |  RAG pipelines, memory, tool schemas,      |  |
|  |  context window optimization               |  |
|  +--------------------------------------------+  |
|                                                  |
|  Skill routing, planning loops, error recovery,  |
|  progressive disclosure, multi-agent coord       |
+--------------------------------------------------+
```

Un harness engineer sigue escribiendo prompts. Sigue haciendo context engineering. Pero además construye el *sistema* que decide qué prompts usar y cuándo, qué contexto ensamblar para cada situación y cómo recuperarse cuando algo sale mal.

La evolución no consiste en abandonar las técnicas anteriores. Consiste en reconocer que son necesarias pero insuficientes —— y construir las capas que están por encima de ellas y que convierten la capacidad bruta del LLM en aplicaciones fiables de grado de producción.

Una encuesta de 19 autores de Shanghai Jiao Tong y colaboradores, **"Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering"** (arXiv 2604.08224, 9 de abril de 2026), llega de manera independiente a la misma organización de tres capas que utiliza este capítulo: la progresión del campo, en su encuadre, va de *weights* a *context* y a *harness*, y tratan memory, skills, protocols y harness engineering como cuatro componentes externalizados unificados por el harness como capa de integración. La convergencia merece señalarse para los lectores que vienen de la literatura académica: este no es un encuadre exclusivo de practicantes ni es único de esta guía —— es el eje organizador que la encuesta académica de finales de abril de 2026 también eligió.

---

## Sources

- Brown, T. et al. (2020). "Language Models are Few-Shot Learners." [arXiv:2005.14165](https://arxiv.org/abs/2005.14165)
- Wei, J. et al. (2022). "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models." [arXiv:2201.11903](https://arxiv.org/abs/2201.11903)
- Yao, S. et al. (2022). "ReAct: Synergizing Reasoning and Acting in Language Models." [arXiv:2210.03629](https://arxiv.org/abs/2210.03629)
- Yao, S. et al. (2023). "Tree of Thoughts: Deliberate Problem Solving with Large Language Models." [arXiv:2305.10601](https://arxiv.org/abs/2305.10601)
- Wang, X. et al. (2022). "Self-Consistency Improves Chain of Thought Reasoning in Language Models." [arXiv:2203.11171](https://arxiv.org/abs/2203.11171)
- Karpathy, A. (mid-2025). Comentarios públicos que acuñaron "context engineering" como el término correcto para la disciplina; encuadre ampliamente compartido en X y en la comunidad de ingeniería de IA.
- Manus. (2025). "Context Engineering Lessons from Building Manus." [manus.im/blog](https://manus.im/blog) —— Tasa de aciertos de la KV-cache como métrica operativa, contexto append-only, enmascaramiento de herramientas vía logit bias, reescritura rodante de la todo-list.
- Böckeler, Birgitta. (April 2, 2026). "Harness engineering for coding agent users." martinfowler.com (serie *Exploring Generative AI*). [https://martinfowler.com/articles/harness-engineering.html](https://martinfowler.com/articles/harness-engineering.html) —— Taxonomía Guides vs. Sensors, Computational vs. Inferential.
- OpenAI. Material público de Codex: [https://openai.com/index/introducing-codex](https://openai.com/index/introducing-codex). Ancla para el encuadre del diseño del harness de Codex; las cifras ampliamente citadas de "tres ingenieros / ~1M de líneas / ~1.500 PRs" circularon en charlas y publicaciones de OpenAI de 2025–2026 y se reportan aquí como citas de la comunidad y no provenientes de una única publicación canónica.
- Schmid, Philipp. "The New Skill in AI is Not Prompting, It's Context Engineering" y continuación. [https://www.philschmid.de/context-engineering](https://www.philschmid.de/context-engineering); [https://www.philschmid.de/context-engineering-part-2](https://www.philschmid.de/context-engineering-part-2) —— Analogía Model = CPU, Context = RAM, Harness = OS.
- Mnemónico IMPACT. Intent / Memory / Planning / Authority / Control flow / Tools —— checklist de diseño de harness de seis dimensiones que emergió en el discurso de practicantes de mediados de la década de 2020. Se usa en este capítulo como encuadre pedagógico; no se atribuye a una fuente primaria específica.
- Reportajes sobre la adquisición Meta/Manus. (2026). Diversas fuentes.
- Zhou, C. et al. (April 2026). "Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering." [arXiv:2604.08224](https://arxiv.org/abs/2604.08224) —— Encuesta de 19 autores de Shanghai Jiao Tong y colaboradores que utiliza de manera independiente el encuadre histórico de tres capas Weights → Context → Harness. Citada en la sección "Coexistencia, no reemplazo" de este capítulo como evidencia de que la tesis de los practicantes convergió con la literatura académica.

---

*Capítulo siguiente: [Capítulo 2 — RAG, contexto largo y grafos de conocimiento](02-knowledge-layer.md)*
