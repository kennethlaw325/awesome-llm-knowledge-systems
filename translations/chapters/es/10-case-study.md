# Capítulo 10: Construyendo un Knowledge Harness del mundo real

> **En una frase:** un desarrollador construyó un sistema de conocimiento de IA completo con un equipo de 4 agentes, enrutamiento por progressive disclosure y un pipeline de contenido automatizado.
>
> **Por qué importa:** esto prueba que una persona con la arquitectura adecuada puede construir lo que antes requería un equipo. Los conceptos de esta guía no son teóricos.

Este capítulo presenta un caso de estudio anonimizado de un desarrollador en solitario ——al que se llama "el builder" —— que construyó un knowledge harness completo a lo largo de varios meses de desarrollo iterativo. El sistema descrito aquí es real y se usa diariamente en producción. Demuestra cómo los conceptos discutidos en los capítulos anteriores ——context engineering, progressive disclosure, sistemas de skills y orquestación de agents —— se combinan en la práctica.

## El punto de partida

El builder comenzó con un problema simple: demasiado conocimiento, poca estructura. Un vault de conocimiento personal había crecido hasta más de 300 notas que abarcaban proyectos activos, referencias técnicas, registros de reuniones e ideas fugaces. El enfoque estándar ——buscar cuando necesitas algo —— se rompía a medida que el vault crecía. Las notas se olvidaban, las intuiciones se redescubrían en vez de recuperarse y el contexto se perdía entre sesiones de trabajo.

La solución inicial fue modesta: usar un asistente LLM con acceso al vault. Pero el acceso directo a más de 300 notas significaba inundar el context window. El verdadero reto de ingeniería no era "¿puede el LLM leer mis notas?" sino "¿cómo le doy al LLM las notas correctas en el momento correcto?".

## Capa de conocimiento: el vault como grafo de conocimiento implícito

El cimiento del sistema es un vault de Obsidian organizado en una jerarquía de carpetas deliberada:

- **Inbox** para captura (todas las notas nuevas aterrizan aquí)
- **Active** para notas de uso diario (mantenidas entre 5–10 items)
- **Projects** para trabajo acotado en el tiempo con deadlines
- **Areas** para responsabilidades continuas sin deadlines
- **Notes** para conocimiento atómico (una idea por nota, títulos como afirmaciones)
- **Daily** para diarios e informes de revisión
- **Archive** para material completado o desactualizado

Cada nota usa wikilinks para conectarse a notas relacionadas, creando un grafo de conocimiento implícito sin requerir una base de datos de grafos formal. La convención de enlace es simple pero estricta: si la nota A referencia un concepto que la nota B desarrolla, A debe enlazar a B. Con el tiempo, esto produce una red navegable de conocimiento donde cualquier punto de entrada conduce al contexto relacionado.

El vault se mantiene mediante un ciclo de revisión: las revisiones diarias procesan el inbox y clasifican las notas nuevas; las revisiones semanales analizan tendencias de acumulación de conocimiento y resurgen notas antiguas valiosas; las revisiones mensuales verifican contradicciones, fusionan notas que se solapan y archivan proyectos completados. Este mantenimiento no es opcional. Sin él, la capa de conocimiento se degrada en semanas a medida que las notas se vuelven obsoletas, redundantes o huérfanas.

## Context Engineering: el system prompt como índice

El enfoque de context engineering del builder trata el system prompt no como un conjunto monolítico de instrucciones sino como un índice hacia recursos más profundos. Un fichero de configuración central (análogo a un README para la IA) contiene:

- **Detalles del entorno**: OS, shell, peculiaridades conocidas que evitar
- **Preferencias de idioma**: el idioma de trabajo del builder y las convenciones de formato
- **Una routing table**: una lista priorizada de categorías de skills con palabras clave disparadoras y punteros a ficheros de enrutamiento

Este fichero de configuración siempre se carga. Es compacto ——por debajo de 2.000 tokens —— porque contiene punteros, no payloads. Cuando el LLM encuentra una petición de usuario, la coteja con la routing table y carga únicamente el fichero de enrutamiento relevante, que a su vez apunta al skill específico necesario.

Un sistema de memoria separado gestiona la persistencia entre sesiones. Almacena:

- Ubicaciones y estructuras de proyectos activos
- Preferencias de usuario aprendidas del feedback
- Patrones técnicos y convenciones específicas de cada proyecto
- Referencias a subficheros detallados para temas complejos

El fichero de memoria crece orgánicamente. Cuando el builder corrige el comportamiento del asistente, esa corrección se registra como una preferencia. Cuando se establece la estructura de un proyecto, se documenta una vez y se referencia desde entonces. Esto elimina el repetitivo problema de "déjame volver a explicarte mi proyecto" que afecta a las interacciones LLM sin estado.

## Harness Engineering: el equipo de agents

El sistema emplea un equipo de cuatro agents, cada uno con un rol definido:

1. **Data Collector**: reúne información de fuentes externas (búsquedas web, llamadas a APIs, parseo de documentos). Opera con permisos amplios pero sin capacidad de publicar.
2. **Pipeline Orchestrator**: coordina los flujos de trabajo, decide qué agents invocar y gestiona la secuencia. Escribe "sprint contracts" ——documentos que especifican los criterios de salida esperados para cada tarea.
3. **Content Writer**: produce la salida (informes, publicaciones en redes sociales, documentos técnicos). Opera bajo content guards que imponen el brand voice y los estándares de formato.
4. **QA Evaluator**: revisa toda la salida contra el sprint contract antes de que pueda publicarse. Verifica la precisión factual, el cumplimiento del formato y la alineación con la marca.

El mecanismo del sprint contract merece elaboración. Cuando el orchestrator inicia una tarea de contenido, no se limita a decir "escribe una publicación sobre X". Produce un contrato que especifica: la plataforma objetivo, el rango de palabras, los elementos requeridos (por ejemplo, debe incluir una estadística, debe terminar con una call to action), los elementos prohibidos (por ejemplo, sin superlativos, sin afirmaciones no verificadas) y los criterios de evaluación. El content writer produce contra este contrato. El QA evaluator califica contra él. Si la salida falla la evaluación, se devuelve al writer con feedback específico que referencia los criterios del contrato. Esto no es un reintento único ——el bucle continúa hasta que el contrato se satisface o un humano interviene.

Los content guards operan en tres capas:

- **Guards a nivel de prompt**: instrucciones embebidas en el system prompt que definen qué debe y qué no debe hacer el agent
- **Auto-correction**: procesamiento posterior a la generación que detecta y corrige problemas comunes (por ejemplo, eliminar patrones de formato no deseados, imponer terminología consistente)
- **Regex strip**: una pasada final que elimina patrones específicos que nunca deberían aparecer en la salida (por ejemplo, ciertos caracteres que rompen sistemas aguas abajo, tokens de metadatos que se filtran del modelo)

La comunicación entre agents se basa en triggers. Los agents no se sondean unos a otros. Cuando el data collector termina de reunir información, escribe la salida en una ubicación definida y dispara al orchestrator. Cuando el writer produce contenido, dispara al evaluator. Esta arquitectura orientada a eventos mantiene el sistema responsivo sin cómputo innecesario.

## Evolución del sistema de skills

El sistema de skills atravesó cuatro etapas evolutivas distintas, cada una impulsada por limitaciones prácticas descubiertas en producción.

**Etapa 1: ficheros de skill planos.** Cada skill era un fichero markdown independiente que contenía instrucciones. El LLM cargaba todos los ficheros de skill al inicio de la sesión. Esto funcionaba con 5–10 skills pero se volvió insostenible a medida que la colección crecía. Los context windows se llenaban con definiciones de skill, dejando poco espacio para el trabajo real.

**Etapa 2: YAML frontmatter enriquecido.** Los skills ganaron metadatos estructurados: condiciones de trigger, contexto requerido, dependencias y números de versión. Esto permitió al sistema filtrar los skills por relevancia, pero la lógica de filtrado en sí misma consumía tokens y añadía latencia.

**Etapa 3: wikilinks entre skills.** Los skills empezaron a enlazarse entre sí, creando un skill graph. Un skill para "deploy" enlazaría a "run tests" como prerrequisito. Esto permitió al sistema cargar cadenas de skills en vez de skills individuales, pero la navegación del grafo seguía requiriendo cargar el índice del grafo.

**Etapa 4: progressive disclosure con ficheros de enrutamiento.** La arquitectura final usa un índice compacto (la routing table en el system prompt) que apunta a siete ficheros de enrutamiento específicos por categoría. Cada fichero de enrutamiento lista los skills de esa categoría con sus condiciones de trigger. El LLM carga solo el fichero de enrutamiento de la categoría coincidente y luego carga solo el skill específico necesario. En cualquier momento dado, el sistema tiene cargados: el índice del system prompt (~2K tokens) + un fichero de enrutamiento (~500 tokens) + un fichero de skill (~1–2K tokens). Sobrecarga total: por debajo de 4K tokens independientemente de cuántos skills existan en el sistema.

El builder probó esta arquitectura de enrutamiento con 85 consultas de prueba que cubrían todas las categorías y logró 85/85 enrutamientos correctos ——100% de precisión. Los casos límite (consultas ambiguas que podrían coincidir con varias categorías) se manejan mediante reglas explícitas de desambiguación en la routing table.

## Resultados

Los resultados medibles de esta arquitectura:

- **Reducción del 65% en tokens** por progressive disclosure comparado con el enfoque de ficheros planos. Las mismas tareas que antes consumían 8–12K tokens de contexto de skills ahora requieren menos de 4K.
- **Pipeline de contenido automatizado** que produce salida diaria a través de múltiples plataformas con calidad consistente, gestionado por una sola persona.
- **Mantenimiento del conocimiento** mediante un linting automatizado del vault que detecta contradicciones, notas huérfanas e información obsoleta ——problemas que antes requerían sesiones de revisión manual.
- **Continuidad entre sesiones** que elimina el problema del "arranque en frío". El sistema de memoria significa que el asistente retoma donde lo dejó, cada vez.

## Lecciones aprendidas

**Empieza simple, luego apila complejidad.** El builder no diseñó el sistema de cuatro agents con sprint-contract el primer día. Empezó como un solo agent con un fichero de texto de instrucciones. Cada capa de complejidad se añadió en respuesta a un modo de fallo específico: los agents alucinaban (añadir QA evaluator), la salida era inconsistente (añadir content guards), los context windows desbordaban (añadir progressive disclosure). Una arquitectura prematura habría producido un sistema optimizado para problemas imaginados en lugar de reales.

**Progressive disclosure compensa el coste de configuración.** Construir y mantener la routing table, los siete ficheros de enrutamiento y los ficheros de skill individuales requiere esfuerzo continuo. Pero la reducción del 65% en tokens se paga sola en cada interacción. Más importante, el sistema escala: añadir un nuevo skill significa añadir una entrada a un fichero de enrutamiento, no reestructurar el prompt entero.

**Menos es más.** Las definiciones de skill comprimidas y precisas superan a las verbosas. Un fichero de skill que dice "busca en el vault notas que coincidan con la consulta, devuelve rutas de fichero y extractos relevantes, sugiere conexiones" funciona mejor que una elaboración de 500 palabras de las mismas instrucciones. El LLM no necesita que se le lleve de la mano; necesita intención clara.

**El harness ES el producto.** La ventaja competitiva del builder no es ningún skill o agent individual. Es el harness ——la lógica de enrutamiento, los sprint contracts, los content guards, el ciclo de revisión, el sistema de memoria. Los componentes individuales son sencillos. Donde vive el valor es en la integración. Esto refleja una verdad más amplia sobre la ingeniería del conocimiento: los modelos se están commoditizando, pero los sistemas que los orquestan no.

## Recuadro: Claude Code como implementación de referencia

Durante la mayor parte del periodo en que el sistema del builder evolucionaba, el tooling interno de Anthropic era una caja negra. Los practicantes podían inferir cómo funcionaba Claude Code a partir de su comportamiento, pero nadie fuera de Anthropic había visto el código. Eso cambió el **31 de marzo de 2026**, cuando Anthropic envió accidentalmente un source map de 59.8MB dentro del paquete npm `@anthropic-ai/claude-code` v2.1.88 ——aproximadamente 513.000 líneas de TypeScript sin ofuscar repartidas en 1.906 ficheros (véase el Capítulo 4 para la historia completa). La filtración dio a la comunidad su primera mirada empírica a un harness de producción de un frontier lab, y varios de sus patrones riman estrechamente con lo que el builder llegó a alcanzar de forma independiente:

- **Self-Healing Memory, no un único fichero grande.** La arquitectura filtrada de Claude Code está organizada alrededor de un sistema "Self-Healing Memory" de tres capas con lógica de reparación explícita entre capas. El bucle vault + fichero de memoria + sprint-contract del builder es un pariente más pobre de la misma idea: un estado de trabajo a corto plazo (la sesión actual), un estado compactado a medio plazo (el fichero de memoria) y conocimiento duradero a largo plazo (el vault). En ambos sistemas, la "memoria" no es un lugar; es un conjunto de capas con transiciones entre ellas.
- **MEMORY.md como índice, no como almacén.** Dentro de Claude Code, `MEMORY.md` es un índice ligero al estilo de punteros hacia notas más detalladas ——no una transcripción monolítica. El fichero de configuración del builder cumple exactamente el mismo rol: contiene routing table y punteros, no payloads, y es la razón por la que el contexto base se mantiene por debajo de 2K tokens.
- **`KAIROS` y el modo daemon autónomo.** El código fuente de Claude Code referencia un feature flag `KAIROS` más de 150 veces. Habilita un modo daemon autónomo ——un bucle de ejecución no supervisado y de larga duración que va mucho más allá del REPL interactivo. La comunicación entre agents del builder, basada en triggers y orientada a eventos, es una versión hecha a mano de la misma idea: agents que despiertan ante eventos, hacen trabajo y se pasan el testigo, sin un humano en el bucle en cada paso.

El punto de este recuadro no es que el sistema del builder sea secretamente Claude Code. Los dos sistemas están separados por órdenes de magnitud en esfuerzo de ingeniería, y la versión del builder hace en cientos de ficheros markdown lo que Anthropic hace en medio millón de líneas de TypeScript. El punto es que **ambos sistemas convergieron de forma independiente hacia la misma forma** ——memoria por capas con un índice, enrutamiento sobre payloads y orquestación orientada a eventos —— lo que sugiere que estos patrones no son elecciones estilísticas. Es a lo que se parecen los harnesses de producción cuando sobreviven al contacto con cargas de trabajo reales.

## Implicaciones para los practicantes

Este caso de estudio ilustra que un solo desarrollador, trabajando iterativamente durante meses, puede construir un knowledge harness que hace dos años habría requerido un equipo de ingenieros. Los habilitadores clave son: LLMs lo bastante capaces como para seguir instrucciones complejas de múltiples pasos, protocolos abiertos (MCP) para la integración de herramientas, y la disciplina emergente del context engineering que aporta patrones de diseño para estos sistemas.

El sistema del builder no es una plantilla para copiar. Es una prueba de concepto de que los principios de esta guía ——progressive disclosure, context engineering, skill graphs, orquestación de agents —— producen resultados medibles en producción. Tu harness se verá distinto. La arquitectura debería ser la misma.

---

*Capítulo siguiente: [Capítulo 11 — Momentos clave en la ingeniería del conocimiento con LLMs](11-timeline.md)*
