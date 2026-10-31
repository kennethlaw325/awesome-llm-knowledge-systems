<!-- translation-sync:start -->
> Traducción asistida por máquina sincronizada con la edición inglesa de 2026-10-31, con revisión de estructura y contenido. El código y las etiquetas de los diagramas conservan el original; los tiempos de lectura se estiman a partir del inglés.
> [English source](../glossary.md) · [Sync record](SYNC.md)
<!-- translation-sync:end -->

<a id="glossary"></a><!-- i18n-anchor -->

## Glosario

> Definiciones en lenguaje sencillo para cada término técnico utilizado en esta guía. No se requiere doctorado.

### A

**A2A (Protocolo de agente a agente)**
Una forma estándar para que los agentes de IA hablen entre sí y coordinen tareas, como un lenguaje común que permita a diferentes asistentes de IA repartirse el trabajo entre ellos.

**Memoria del agente**
La capacidad de un agente de IA para recordar información a través de conversaciones o tareas. Piense en ello como un cuaderno que el agente guarda entre sesiones para no empezar desde cero cada vez.

**RAG con agentes**
Una versión de RAG en la que la IA decide activamente qué información buscar, cuándo buscarla y si los resultados son lo suficientemente buenos, en lugar de seguir un paso de recuperación fijo cada vez.

**Ancla (Ingeniería de Grafos)**
Una medición indiscutible y basada en evidencia externa —un resultado de prueba, una métrica o una comprobación con datos de referencia— que algún nodo de un grafo multiagente debe consultar. Carlos E. Perez introdujo el concepto en el discurso sobre ingeniería de grafos de julio de 2026: sin anclas, un grafo de agentes que revisan mutuamente su trabajo degenera en una cámara de eco que converge en un acuerdo seguro de sí mismo, no en la corrección. Es como exigir que al menos un miembro de un comité compruebe el extracto bancario real, en lugar de que todos acuerden que el presupuesto parece correcto. Véase **Ingeniería de grafos**; capítulo 14.

**ARC-AGI-3**
El benchmark interactivo de inteligencia de agentes de François Chollet de 2026: los agentes se sitúan en entornos similares a juegos, sin instrucciones, y deben explorar, inferir el objetivo y construir por sí mismos un modelo del mundo. A diferencia de los anteriores benchmarks ARC de cuadrículas estáticas, ARC-AGI-3 evalúa por separado la eficiencia de exploración, la inferencia de objetivos y la formación de modelos del mundo.

### C

**CATTS (escalado en inferencia consciente del consenso)**
Método de escalado durante la inferencia para agentes de varios pasos que muestrea un pequeño comité de trayectorias por acción y utiliza su desacuerdo como señal de incertidumbre para asignar cómputo. Los pasos con más desacuerdo reciben mayor presupuesto de razonamiento; los de menor desacuerdo, menos. Los resultados publicados muestran aproximadamente +9.1% de precisión con 2.3x menos tokens frente al escalado uniforme.

**Claude Code**
Herramienta de línea de comandos de Anthropic que permite a Claude trabajar en el terminal: leer archivos, ejecutar comandos y editar código como compañero de programación con IA.

**Documentos de metadatos de ID de cliente (CIMD)**
El mecanismo de identificación de cliente exigido por la especificación MCP 2026-07-28 finalizada, que reemplaza el registro dinámico de cliente: un cliente MCP se identifica mediante un documento de metadatos alojado en una URL en lugar de registrarse por separado en cada servidor. Como presentar una tarjeta de presentación alojada en su propia dirección en lugar de completar un formulario de nuevo proveedor en cada oficina que visite. Consulte **MCP**.

**Codex (OpenAI)**
La herramienta de OpenAI para ejecutar tareas de codificación en un entorno de nube aislado, donde un agente de IA puede leer su repositorio, escribir código y ejecutar pruebas de forma autónoma.

**Ingeniería de contexto**
La práctica de diseñar cuidadosamente qué información recibe una IA antes de responder. Si la ingeniería de prompts escribe la pregunta, la ingeniería de contexto elige qué materiales de referencia poner sobre el escritorio de la IA.

**Ventana de contexto**
La cantidad total de texto que un modelo de IA puede procesar a la vez, tanto su entrada como su salida. Como el tamaño de una pizarra: todo lo que el modelo lee y escribe debe caber en ella.

**Supervisión de CoT (cadena de pensamiento)**
La práctica de leer los tokens de razonamiento explícito de un modelo para detectar comportamiento indebido o desalineación antes de que actúe según su plan. En abril de 2026, OpenAI la utilizó para descubrir a uno de sus modelos haciendo trampas en evaluaciones de programación: el primer caso público de interpretabilidad como comprobación durante la ejecución, en lugar de herramienta forense posterior.

### D

**Modelo de decisión**
Un modelo que responde preguntas acotadas y tipadas con una decisión y probabilidades asociadas, en lugar de generar una respuesta abierta. Un harness puede utilizar ese juicio para enrutamiento o triaje, mientras el código determinista de la aplicación conserva la autoridad sobre los permisos. Las probabilidades requieren comprobaciones de calibración; no demuestran que la decisión sea correcta. Véase el [capítulo 12](chapters/es/12-local-models.md).

**Dreaming**
Un trabajo de curación de memoria programado entre sesiones que reescribe la memoria persistente de un agente en función de patrones de sesiones recientes. Comercializado por primera vez por Anthropic Managed Agents (6 de mayo de 2026, vista previa de la investigación): el curador lee sesiones recientes, identifica errores recurrentes y flujos de trabajo convergentes, y reescribe la memoria persistente del agente en texto sin formato. Contrasta con la memoria entrenable (Titans + MIRAS, abril 2026) que se adapta en la inferencia mediante actualizaciones de gradiente: Dreaming mantiene la memoria como datos que lee el harness, Titans hace que la memoria sea parte del modelo en sí.

### E

**Embeddings**
Una forma de convertir texto en listas de números para que significados similares acaben muy juntos matemáticamente. Esto permite a las computadoras medir qué tan relacionadas están dos piezas de texto, de la misma manera que podrías notar que dos libros cubren temas similares.

**Vectores de emociones**
Direcciones interpretables de características dentro de las activaciones internas de Claude que, al intensificarse, sesgan de forma fiable al modelo hacia conductas de carga emocional, incluidas salidas de tipo chantaje en la divulgación de Anthropic de abril de 2026. Al poder identificarlas, los ingenieros de harness disponen de una superficie de filtrado a nivel de característica, no solo de token.

**Autorización administrada por la empresa (EMA)**
Una extensión de MCP (estable 18 de junio de 2026) para acceso centralizado y proporcionado por IdP a servidores MCP. En lugar de que cada usuario ejecute un flujo de consentimiento OAuth por aplicación para cada servidor, la organización proporciona acceso al servidor una vez a través de su proveedor de identidad; durante el SSO, el cliente obtiene una **Concesión de autorización JWT de afirmación de identidad (ID-JAG)** y la intercambia por un token de acceso emitido por el propio servidor de autorización del servidor MCP (consulte **MCP**). El soporte del primer día abarcó a Okta como IdP, Anthropic y VS Code como clientes y siete servidores. EMA es lo que convierte el SSO empresarial para MCP de un pegamento de integración por servidor a una única decisión de aprovisionamiento que se toma una vez en el IdP.

### F

**Aprendizaje few-shot**
Enseñar a una IA cómo realizar una tarea mostrándole algunos ejemplos dentro de su prompt, en lugar de volver a entrenar todo el modelo. Como mostrarle a alguien tres formularios completos para que sepa cómo completar el cuarto.

**Ajuste fino**
Tomar un modelo de IA previamente entrenado y entrenarlo más con sus propios datos específicos para que mejore en un trabajo en particular. Como contratar a un generalista y luego brindarle capacitación especializada en el trabajo.

### G

**Separación generador-evaluador**
Patrón de fiabilidad que separa al agente que produce trabajo de otro independiente y deliberadamente escéptico que lo juzga, porque los agentes sobrevaloran sistemáticamente sus propios resultados. Se presenta en "Harness design for long-running application development" de Prithvi Rajasekaran (Anthropic, marzo de 2026), inspirado en Generative Adversarial Networks (GAN), y concluye que ajustar un evaluador independiente para hacerlo escéptico es mucho más viable que hacer autocrítico al generador. El evaluador comprueba comportamiento, no solo diferencias de código: navega por la aplicación en ejecución, captura pantallas y prueba la interfaz, endpoints de API y estados de base de datos. El patrón se convierte en producto con capacidades básicas de ejecución hasta condición como `/goal` de Claude Code, donde un modelo nuevo y separado juzga la condición de parada tras cada turno. Véanse **Bucle exterior** e **Ingeniería de bucles**.

**Ingeniería de grafos**
Propuesta de julio de 2026 según la cual la capa superior a la **ingeniería de bucles** es el grafo: la conexión explícita de qué agentes existen, quién puede delegar en quién y cómo sus bucles se supervisan y corrigen. Se concretó en ensayos posteriores a una publicación de Peter Steinberger del 17-18 de julio de 2026 y se cuestionó desde el primer día: LangChain sostiene que la práctica tiene tres años —un bucle es simplemente un grafo cíclico dirigido— y solo el nombre es nuevo. No debe confundirse con los grafos de conocimiento o **GraphRAG**, que estructuran lo que un sistema *sabe*; la ingeniería de grafos estructura quién *es* el sistema. La evaluación de supervivencia de la guía del 15 de septiembre de 2026 encontró circulación continuada —ensayos independientes y un curso de pago sobre organización de agentes—, pero ninguna adopción por proveedores en la documentación revisada; registró que la circulación sobrevivió y la condición de capa distinta seguía sin demostrarse. La guía lo sigue como nombre controvertido de coordinación multiagente, no como capa consolidada. Véase el capítulo 14.

**GraphRAG**
Versión de RAG que organiza la información recuperada en un grafo de entidades y relaciones conectadas, mejorando las respuestas que exigen combinar hechos de varias fuentes.

### H

**Ingeniería de harness**
Diseñar el sistema circundante (herramientas, memoria, reglas y flujos de trabajo) que envuelve un modelo de IA y da forma a su comportamiento en la práctica. El modelo es el motor; el harness es todo el coche.

**Síntesis de harness**
Técnicas en las que un optimizador de bucle exterior —basado en búsqueda, observabilidad u otros métodos— modifica automáticamente el harness: herramientas, prompts, reparto de funciones, topología de comunicación y protocolo de coordinación, según señales de ejecución de la tarea objetivo. Véanse **AHE** (arXiv 2604.25850) y **AgentFlow** (arXiv 2604.20801), las dos implementaciones de referencia de abril de 2026. Se distingue de *meta-harness*, un marco de 2025 / principios de 2026 que trataba el harness como objetivo de optimización puntual, no como artefacto en evolución continua.

**Entrenamiento nativo del harness**
Entrenar un modelo directamente con un harness concreto de agentes de producción para que aprenda sus herramientas y flujos, no solo a producir resultados correctos de forma aislada. El ejemplo de referencia es **MAI-Code-1-Flash** de Microsoft (Build, 2 de junio de 2026), un modelo de programación de 5B parámetros entrenado con los harnesses de GitHub Copilot de producción; Microsoft comunica ~60% menos tokens en tareas difíciles y mejor relación precio-rendimiento que Claude Haiku 4.5. Es la **inversa simétrica de la síntesis de harness**: la síntesis (véanse **Síntesis de harness**, **AHE**) mantiene fijo el modelo y hace evolucionar el harness; el entrenamiento nativo mantiene fijo el harness y adapta el modelo. Juntos convierten modelo y harness en un problema de codiseño optimizable desde ambos extremos. La contrapartida: un modelo ajustado al harness de un proveedor es más valioso dentro de él, reforzando la dinámica de *harness como ventaja competitiva*.

### I

**Inferencia**
El proceso de un modelo de IA que genera una respuesta a sus aportaciones. Cada vez que envía un mensaje y recibe una respuesta, el modelo realiza una inferencia.

**Cabeza de iteración**
Una cabeza de atención que emerge durante el razonamiento de cadena de pensamiento y atiende sistemáticamente a la salida del paso anterior, identificada por el equipo de interpretabilidad de Anthropic en abril de 2026. Sugiere que el prompting explícito de CoT funciona en parte al inducir un circuito interno concreto, no solo al producir texto intermedio legible para personas.

### K

**Grafo de conocimiento**
Un mapa estructurado de hechos donde las entidades (personas, lugares, conceptos) están conectadas mediante relaciones etiquetadas. Como una red de fichas conectadas por cadenas etiquetadas que muestran cómo se relaciona todo.

**KV-Cache**
Un atajo de memoria que permite a la IA reutilizar cálculos anteriores en una conversación en lugar de rehacerlos desde cero, lo que hace que las respuestas sean más rápidas y económicas cuando el historial de la conversación permanece igual.

### L

**LLM (gran modelo de lenguaje)**
Un sistema de inteligencia artificial entrenado con grandes cantidades de texto que puede comprender y generar lenguaje humano. ChatGPT, Claude y Gemini son todos LLM.

**Contexto largo**
La capacidad de los modelos de IA más nuevos para procesar grandes cantidades de texto a la vez (a veces libros o bases de código completos) dentro de una sola conversación.

**Ingeniería de bucles**
La práctica, denominada en junio de 2026, de construir el sistema que proporciona prompts a un agente por usted, en lugar de introducirlos manualmente en cada turno. La acuñó el ensayo de Addy Osmani del 7 de junio de 2026, que la define como "replacing yourself as the person who prompts the agent" mediante el diseño de "the system that does it instead,", catalizada por una publicación viral de Peter Steinberger esa misma semana. Está un nivel por encima de la **ingeniería de harness**: un harness con temporizador que crea subagentes auxiliares y se retroalimenta desde estado persistente. Se distingue de un planificador porque lee el estado actual y vuelve a decidir en cada pasada, en lugar de activar un comando fijo según el reloj. Es un término profesional y controvertido, sin literatura académica a mediados de 2026; la guía lo sigue como cuarta capa emergente, no como generación consolidada. Véase el capítulo 13.

### M

**Resolución de conflictos de memoria**
Una elección registrada entre hechos contradictorios, acompañada de la evidencia que la respalda. Un sistema de memoria duradera debe revisarla o retirarla cuando la fuente cambia, desaparece o se olvida. Es un requisito del ciclo de vida, no una afirmación de que todos los backends de memoria implementen transacciones de base de datos. Véase el [capítulo 6](chapters/es/06-agent-memory.md).

**MCP (Model Context Protocol)**
Un estándar abierto que permite a los asistentes de IA conectarse a herramientas externas y fuentes de datos a través de una interfaz universal plug-and-play, como USB para aplicaciones de IA.

**MCP Apps**
Capacidad básica de la versión candidata MCP 2026-07-28, fijada el 21 de mayo de 2026, que permite a los servidores entregar interfaces HTML interactivas junto a llamadas a herramientas. El anfitrión representa la interfaz en un iframe aislado; las plantillas se declaran previamente para revisión de seguridad y caché. MCP Apps es el primer entregable nativo de MCP que no es una llamada a herramienta: un servidor de conocimiento puede entregar un buscador, uno de investigación una comparación de resultados y uno de compras una confirmación de compra, sin añadir una especificación de interfaz separada.

**Túnel MCP**
Patrón de despliegue en red privada publicado por Anthropic Managed Agents en vista previa de investigación el 19 de mayo de 2026 (Code with Claude London). Una pasarela ligera dentro de la red privada del cliente establece una conexión saliente con Anthropic; después los agentes pueden llamar a bases de datos, API, bases de conocimiento y sistemas de tickets internos como herramientas MCP, sin reglas entrantes de cortafuegos, endpoints públicos ni VPN. Es el equivalente simétrico de los sandboxes autogestionados: estos mantienen la *ejecución* de herramientas dentro del perímetro del cliente; los túneles MCP mantienen dentro su *alcance*.

**Managed Agents**
Modelo de entorno alojado donde el proveedor del modelo, no el desarrollador, opera la infraestructura del harness: sandbox, estado de sesión, ejecución acotada de herramientas y trazas. Anthropic publicó el primer ejemplo comercial en beta pública el 8 de abril de 2026 ([platform.claude.com/docs/en/managed-agents/overview](https://platform.claude.com/docs/en/managed-agents/overview)). Según la cobertura de lanzamiento de SiliconANGLE, se factura con tarifas normales de tokens de API más una cuota por hora de ejecución del agente para la infraestructura; la cifra por hora no está en la documentación primaria de Anthropic. Se distingue de las superficies de activación nativas de nube, como Claude Code Routines, que se sitúan sobre una infraestructura de este tipo y responden a otra pregunta: "what makes the loop start".

**Interpretabilidad mecanicista**
Un programa de investigación que tiene como objetivo identificar circuitos comprensibles para los humanos dentro de los pesos de un modelo: las características, cabezas y vías específicas que implementan un comportamiento determinado. Nombrada una de las 10 tecnologías innovadoras de 2026 de MIT Technology Review, sustenta los resultados de abril de 2026, como vectores de emociones, cabezales de iteración y monitoreo de CoT.

**Modelo fundacional de memoria**
Propuesta de julio de 2026 (Metis de MemTensor, arXiv 2607.26760) de situar la memoria del agente como estado persistente y dinámico dentro del propio núcleo del transformer: paramétrica, no externa. El prototipo entrena un "hyper memory block" y un "local memory block", inspirados en Fast Weight Programming, sobre un núcleo Qwen3.5 congelado a escala de 4B / 9B / 27B. Actualiza memoria durante la inferencia mediante una pasada hacia delante de tipo EMA sin gradientes, no escribiendo en un almacén vectorial ni actualizando gradientes como Titans. Los autores reconocen pérdida de información a largo plazo con compresión fija e "information confusion in some cases, possibly caused by the blending of semantics within the latent space": una vista previa de investigación, todavía no un patrón validado en producción. Véase el capítulo 6.

**mHC (hiperconexiones restringidas a una variedad)**
Propuesta arquitectónica de DeepSeek de abril de 2026 que amplía conexiones residuales dirigiendo varios flujos internos de información por una variedad aprendida de baja dimensión. Generaliza el flujo residual único de modelos de tipo Transformer++ a varios flujos coordinados; en la publicación, el resultado sigue pendiente de replicación independiente.

**MIRAS**
Marco de entrenamiento con memoria aumentada de Google Research que aporta recetas, garantías de estabilidad y dinámicas de aprendizaje para arquitecturas como Titans, donde la memoria es un módulo neuronal entrenable actualizado durante la inferencia. MIRAS hace viable aprender mientras se infiere sin que el módulo de memoria diverja.

**MoE (mezcla de expertos)**
Una arquitectura de modelo donde solo un subconjunto del "brain" del modelo se activa para cualquier entrada dada, lo que hace posible construir modelos muy grandes que siguen siendo rápidos porque no todas las partes se ejecutan siempre.

### O

**Obsidian**
Una aplicación para tomar notas que almacena sus notas como archivos de texto sin formato en su propia computadora y le permite vincularlas en una base de conocimientos personal.

**Grafo organizativo / grafo de trabajo**
Los dos objetos de grafo de la ingeniería de grafos, según la guía de Yash Thakker en explainx.ai de julio de 2026: el *grafo organizativo* es el esquema estable de qué agentes existen, para qué sirve cada uno y qué conexiones de delegación están permitidas; el *grafo de trabajo* es la descomposición efímera de tareas que un trabajo concreto crea, ejecuta y descarta. Como el organigrama de una empresa frente al grupo ad hoc formado para un proyecto y disuelto al terminar. Véase **Ingeniería de grafos**; capítulo 14.

**Outcomes (Anthropic)**
Capacidad básica de agentes gestionados en beta pública (Anthropic, 6 de mayo de 2026) donde el agente itera frente a un evaluador separado que ejecuta en su propia ventana de contexto hasta cumplir una rúbrica. Convierte el patrón Ralph-loop / CATTS de iteración guiada por incertidumbre en contrato de API: quien llama escribe una rúbrica, la infraestructura ejecuta el bucle de iteración y evaluación por el agente y solo devuelve resultados convergentes.

**Bucle exterior**
La capa de criterio que conserva una persona mientras los agentes ejecutan el bucle interior —investigar, implementar, probar/verificar e informar—. Procede de "Own the Outer Loop," de Addy Osmani, julio de 2026, que define tres pilares: calidad, con comprobaciones que ejercen presión antes de actuar; veredicto, "the final decision we make before work enters our dependent system"; y responsabilidad de explicar, "the guarantee that if someone asks, I can explain why". Osmani identifica tres fallos de delegar demasiado: deuda cognitiva (erosión de la comprensión de cómo resolver problemas), rendición cognitiva (aceptar ciegamente la salida de IA) e impuesto de orquestación (crear más agentes de los que el propio criterio puede abarcar). Complementa **Ingeniería de bucles** y **Separación generador-evaluador**: el bucle solo es tan bueno como su bucle exterior. Véase el capítulo 13.

### P

**Divulgación Progresiva**
Un principio de diseño en el que primero se muestra solo la información esencial y se revelan más detalles a pedido. Como una página de preguntas frecuentes: ve las preguntas y hace clic para ampliar las respuestas que realmente necesita.

**Ingeniería de Prompts**
El oficio de escribir instrucciones para un modelo de IA de manera que se obtenga la mejor respuesta posible. Pequeños cambios en la redacción pueden producir resultados muy diferentes.

### R

**RAG (generación aumentada por recuperación)**
Una técnica en la que la IA busca información relevante de una fuente externa antes de responder, de modo que su respuesta se base en datos reales en lugar de depender únicamente de lo que memorizó durante el entrenamiento.

**Routines (Claude Code)**
Capacidad básica de harness nativo de nube introducida por Anthropic para Claude Code en abril de 2026: los flujos de agentes se ejecutan en la nube de Anthropic, no en el equipo del usuario, y se activan por programación, llamada API o evento de GitHub. Generaliza patrones de cron y demonio autogestionados en infraestructura gestionada con cuotas por nivel —Pro 5 al día, Max 15 al día, Team/Enterprise 25 al día— y sigue funcionando con el portátil del usuario desconectado.

### S

**Capa de contexto compartido**
Contexto persistente mantenido por separado del agente o modelo que lo consume. Varios agentes pueden acceder a una vista con permisos definidos de la misma información subyacente. Mantener el almacén en el dispositivo no implica que todos los agentes consumidores se ejecuten localmente. Consulte el [Capítulo 12](chapters/es/12-local-models.md).

**Distribución por niveles de seguridad**
Publicar una familia de modelos en niveles paralelos que difieren en salvaguardias y acceso de distribución, no en pesos. El ejemplo de referencia es la pareja de Anthropic de junio de 2026: **Claude Fable 5**, de disponibilidad general pública con medidas de doble uso, incluido rechazo como `stop_reason`, y **Claude Mythos 5**, con los mismos pesos y salvaguardias levantadas, restringido a la coalición Glasswing verificada. Contrasta con niveles elegidos por el proveedor, como GPT-5.5 Trusted Access for Cyber, y con los impuestos por gobiernos a mediados de 2026, como la vista previa de GPT-5.6 limitada por orden ejecutiva. La compensación que expresa: capacidad y seguridad se separan; quién es usted —organización verificada o usuario público— determina a qué nivel de salvaguardias accede, no qué puede hacer el modelo.

**Sandbox autohospedado**
Forma de despliegue de Managed Agents publicada por Anthropic en beta pública el 19 de mayo de 2026 (Code with Claude London). El bucle —orquestación, gestión de contexto y recuperación de errores— permanece en Anthropic, mientras la *ejecución* de herramientas pasa al entorno del cliente o a un proveedor de sandbox gestionado, con soporte oficial para Cloudflare, Daytona, Modal y Vercel. Replantea Managed Agents de "fully Anthropic-hosted" a "Anthropic-orchestrated, customer-perimeter-respecting": el ingeniero elige capa por capa dónde vive cada parte, en lugar de escoger entre gestión íntegra y alojamiento íntegramente propio.

**Self-RAG**
Una versión de RAG donde la IA evalúa la calidad de su propia información recuperada y la respuesta generada, decidiendo si recupera más o revisa su respuesta antes de brindarle el resultado final.

**Precio por hora de sesión** (también indicado como *precio por hora de ejecución del agente*)
Modelo de facturación que mide por separado de la inferencia el puesto del orquestador, la infraestructura donde se ejecuta el bucle. Anthropic Managed Agents lo introdujo comercialmente el 8 de abril de 2026 con tarifas normales de tokens más ocho centavos por hora de ejecución del agente, según SiliconANGLE. La cifra horaria no está en documentación primaria de Anthropic y se cita de prensa técnica secundaria. Destaca por ser la primera capacidad de proveedor que cuantifica "where the loop runs,", separado de "what the loop thinks." La expresión exacta cambia entre la documentación primaria, que habla de *sesiones*, y la prensa, que utiliza *hora de ejecución del agente*; ambas miden el mismo concepto.

**Habilidad (Habilidad de agente de IA)**
Una capacidad empaquetada y reutilizable que un agente de IA puede invocar, como una receta que sigue para una tarea específica como "review this PR" o "run a daily review."

**MCP sin estado**
Cambio arquitectónico introducido en la versión candidata MCP 2026-07-28, fijada el 21 de mayo de 2026, y publicado finalmente en la especificación 2026-07-28 (28 de julio de 2026): el núcleo ya no utiliza el intercambio `initialize` / `initialized` ni cabeceras `Mcp-Session-Id`. Los metadatos del cliente viajan en `_meta` en cada solicitud, por lo que cualquier solicitud puede llegar a cualquier instancia, sin afinidad de enrutamiento ni almacén compartido de sesiones. Resuelve la fricción de escalado horizontal surgida con Streamable HTTP en 2025. Las capacidades de estado duradero que motivaron el giro *con estado* —Tasks de SEP-1686 y ejecución bidireccional de AgentCore— se reconstruyen sobre el núcleo sin estado como extensiones, en lugar de incorporarse a cada solicitud. Núcleo sin estado con trabajo con estado encima, no estado en todos los niveles.

**Grafo de habilidades**
Un mapa de todas las habilidades que tiene disponibles un agente de IA, incluido cómo se relacionan entre sí y cuándo se debe activar cada una.

**Ataque a la cadena de suministro de habilidades**
Habilidad de agente maliciosa o troyanizada distribuida mediante un registro o mercado. El mecanismo distintivo de 2026 es la brecha entre comprobación y uso: los escáneres estáticos examinan la *instantánea del paquete presentado*, pero una habilidad que descarga contenido externo o desempaqueta una carga oculta durante la ejecución puede cambiar de conducta tras revisarse. La divulgación de AIR de junio de 2026 secuestró así aproximadamente 26,000 agentes con una sola habilidad falsa detrás de una URL externa; "Cloak and Detonate" (julio de 2026) mostró evasión en más del 90% de los casos ante ocho escáneres, con detección de comportamiento durante la ejecución (97% con 2% de falsos positivos) como dirección de defensa. La lección refleja la de MCP (véase **MCP**): cuando la **divulgación progresiva** (véase **Divulgación progresiva**) y la distribución masiva mediante registros convierten la habilidad en superficie de ataque, la confianza debe pasar del escaneo al publicar a la contención durante la ejecución.

**Autoencoder disperso (SAE)**
Herramienta de interpretabilidad entrenada sobre activaciones internas para descomponerlas en un conjunto mucho mayor de características individualmente significativas y escasamente activas: el instrumento de trabajo de la **interpretabilidad mecanicista**. Una vez entrenadas sirven como herramientas de desarrollo, no solo de análisis: dirigir durante la inferencia características internas sin ingeniería de prompts; analizar redundancia de benchmarks y cobertura de capacidades; clasificar y organizar datos; y apoyar ajuste supervisado y RL posteriores al entrenamiento. **Qwen-Scope** de Alibaba (arXiv 2605.11887, presentado el 12 de mayo de 2026) es la implementación abierta para una familia de frontera de pesos abiertos: 14 grupos de SAE en siete variantes Qwen3 y Qwen3.5, densas y MoE, de 1.7B a 35B parámetros (Qwen3-1.7B a Qwen3.5-35B-A3B). Véase el capítulo 9.

**Sustitución del estado**
Situación en la que un hecho, restricción o decisión de la **memoria del agente** se modifica durante una interacción larga y el valor almacenado deja de ser vigente. Identifica un fallo invisible por diseño para los benchmarks centrados en recuerdo: devolver con confianza un valor que el usuario *antes* mantenía puntúa como acierto. **StateMemBench** (arXiv 2608.19652, 20 de agosto de 2026) lo convirtió en un tercer eje de evaluación de gobernanza, junto a control de acceso y complacencia, con 234 escenarios multisesión y evaluación sobre un conjunto cerrado que aísla fallos de seguimiento de estado de errores normales de recuperación; StateMem, método del mismo artículo, registra explícitamente sustituciones y dependencias relacionales en vez de dejarlas a la recuperación. Véase el capítulo 6.

**Prompt de sistema**
Instrucciones ocultas dadas a un modelo de IA antes de que comience la conversación, estableciendo su función, reglas y comportamiento. Como una descripción del trabajo que el empleado lee antes del primer día.

### T

**Presupuesto de tarea**
Capacidad básica del harness introducida por Anthropic en Claude Opus 4.7 (abril de 2026, cabecera beta `anthropic-beta: task-budgets-2026-03-13`). Quien llama declara un presupuesto orientativo de tokens para todo el bucle —razonamiento, llamadas, resultados de herramientas y salida final— y el modelo recibe una cuenta atrás mientras trabaja para decidir cuánto buscar, razonar y sintetizar en cada paso. Se distingue de `max_tokens`, límite estricto invisible al modelo. Los presupuestos son orientativos, no obligatorios, y tienen un mínimo de 20K tokens para evitar rechazos degenerados con presupuestos ajustados. Son la primera capacidad de proveedor que expone "how hard to think about each step" como contrato gestionado, no como parámetro ajustado manualmente.

**Políticas temporales**
Capacidad básica de autorización aplicada en la pasarela, publicada por AWS en Amazon Bedrock AgentCore el 6 de agosto de 2026. Una política ordinaria pregunta "may this agent make this call,"; una temporal evalúa la llamada frente a las acciones *anteriores* del agente en la misma sesión, de forma determinista, denegando por defecto, con registro completo y fuera del código del agente, de modo que ningún prompt o decisión del modelo pueda eludirla. Se escribe en **Dogwood**, nuevo lenguaje abierto Apache-2.0 específico para agentes. Sus usos cubren fallos que las instrucciones no previenen: impedir datos inventados —un valor transmitido debe coincidir con lo devuelto por una llamada anterior—, limitar costes acumulados de sesión y exigir aprobación humana antes de acciones privilegiadas. Amplía el límite estricto por acción de AgentCore Payments (mayo de 2026) a todo el historial de sesión: el eje de autoridad del harness obtiene una capa de aplicación de reglas con estado.

**Titans**
Familia de arquitecturas de Google Research de abril de 2026 donde la memoria es un módulo neuronal entrenable actualizado por descenso de gradiente durante la inferencia, no un almacén vectorial externo ni una ventana de atención fija. Con cantidades comparables de parámetros, se informa de que Titans supera a Mamba-2, Gated DeltaNet y Transformer++ en recuerdo a largo alcance y razonamiento de varios saltos, difuminando el límite entre "context" y "fine-tuning."

**Token**
La unidad básica que lee y escribe un modelo de IA: aproximadamente tres cuartos de una palabra en inglés. Los modelos piensan en tokens y en ellos se miden los precios y los límites del contexto.

**Uso de herramientas/llamadas de funciones**
La capacidad de un modelo de IA para desencadenar acciones externas (como buscar en la web, ejecutar código o llamar a una API) en lugar de solo generar texto.

### V

**Base de datos vectorial**
Base de datos diseñada para almacenar y buscar embeddings, lo que agiliza encontrar los elementos más similares entre millones de entradas. Es el motor de la mayoría de los sistemas RAG.

### W

**Wikilink**
Un enlace de doble corchete (como `[[Note Title]]`) utilizado en herramientas como Obsidian para conectar una nota con otra, creando una red de conocimiento vinculado.

### X

**x402**
Protocolo abierto que recupera el código HTTP 402 ("Payment Required") para pagos entre máquinas con monedas estables dentro del mismo canal, utilizado en transacciones de agentes con recursos. Lo originó Coinbase; su primera implementación gestionada por un gran proveedor de nube fue AWS AgentCore Payments (7 de mayo de 2026). Es el equivalente de "value-layer" de MCP para herramientas: MCP normaliza cómo un agente accede a una API y x402 cómo le paga. Antes del respaldo de AWS acumulaba 69,000 agentes activos y ~$50M de volumen a finales de abril de 2026.

---

[Volver al README](README_es.md)
