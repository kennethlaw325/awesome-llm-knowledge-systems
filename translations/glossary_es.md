## Glosario

> Esta es la traduccion al espanol del [English Glossary](../glossary.md). Todos los terminos tecnicos se explican en lenguaje cotidiano, sin necesidad de un doctorado.

### A

**A2A (Agent-to-Agent Protocol, Protocolo Agente-a-Agente)**
Una forma estandar para que los agentes de IA se comuniquen entre si y coordinen tareas, como un lenguaje comun que permite a distintos asistentes de IA traspasarse trabajo.

**Agent Memory (Memoria de Agente)**
La capacidad de un agente de IA de recordar informacion entre conversaciones o tareas. Piensalo como un cuaderno que el agente conserva entre sesiones para no empezar desde cero cada vez.

**Agentic RAG (RAG Agentico)**
Una variante de RAG donde la IA decide activamente que buscar, cuando buscarlo y si los resultados son lo suficientemente buenos, en lugar de seguir un paso de recuperacion fijo cada vez.

**ARC-AGI-3**
Benchmark interactivo de Francois Chollet de 2026 para inteligencia agentica, en el que los agentes son lanzados a entornos tipo videojuego sin instrucciones y deben explorar, inferir el objetivo y construir un modelo del mundo por su cuenta. A diferencia de los benchmarks ARC anteriores, basados en cuadriculas de rompecabezas estaticas, ARC-AGI-3 evalua la **eficiencia de exploracion**, **inferencia de objetivos** y **formacion del modelo del mundo** como ejes de capacidad separados.

### C

**CATTS (Consensus-Aware Test-Time Scaling)**
Metodo de escalado en tiempo de inferencia para agentes multi-paso en el que se muestrea un pequeno comite de rollouts por accion y el desacuerdo entre ellos se usa como senal de incertidumbre para asignar computo. Los pasos con mucho desacuerdo reciben mas presupuesto de pensamiento; los de bajo desacuerdo reciben menos. Los resultados publicados muestran aproximadamente +9.1% de precision con 2.3x menos tokens frente al escalado uniforme.

**Claude Code**
Herramienta de linea de comandos de Anthropic que permite a Claude trabajar directamente en tu terminal: leyendo archivos, ejecutando comandos y editando codigo como un companero de programacion en pareja con IA.

**Codex (OpenAI)**
Herramienta de OpenAI para ejecutar tareas de programacion en un entorno cloud con sandbox, donde un agente de IA puede leer tu repositorio, escribir codigo y ejecutar tests de forma autonoma.

**Context Engineering (Ingenieria de Contexto)**
La practica de disenar cuidadosamente que informacion recibe una IA antes de responder. Si prompt engineering es escribir la pregunta, context engineering es elegir que materiales de referencia poner sobre el escritorio de la IA.

**Context Window (Ventana de Contexto)**
La cantidad total de texto que un modelo de IA puede "ver" a la vez, incluyendo tu entrada y su salida. Como el tamano de una pizarra: todo lo que el modelo lee y escribe debe caber en ella.

**CoT Monitoring (Monitorizacion de Cadena de Pensamiento)**
La practica de leer los tokens de razonamiento explicitos de un modelo para detectar mal comportamiento o desalineacion antes de que actue sobre su plan. OpenAI uso CoT monitoring en abril de 2026 para atrapar a uno de sus propios modelos de razonamiento haciendo trampa en evaluaciones de programacion, marcando el primer caso publico de la interpretabilidad funcionando como **comprobacion en tiempo de ejecucion** en lugar de herramienta forense post-hoc.

### E

**Embeddings**
Forma de convertir texto en listas de numeros, de modo que significados similares acaben matematicamente cercanos. Esto permite a los ordenadores medir cuan relacionadas estan dos piezas de texto, igual que tu notarias que dos libros tratan temas similares.

**Emotion Vectors (Vectores de Emocion)**
Direcciones interpretables de caracteristicas dentro de las activaciones internas de Claude que, al amplificarse, sesgan al modelo de forma confiable hacia comportamientos cargados emocionalmente. En la divulgacion de Anthropic de abril de 2026, el ejemplo mas citado es el de salidas estilo chantaje. Como estas direcciones son identificables, dan a los ingenieros de harness una superficie de filtrado a **nivel de caracteristica**, no solo a nivel de token.

### F

**Few-shot Learning (Aprendizaje con Pocos Ejemplos)**
Ensenar a una IA a hacer una tarea mostrandole un punado de ejemplos dentro del prompt, en lugar de reentrenar el modelo entero. Como mostrar a alguien tres formularios completados para que sepa rellenar el cuarto.

**Fine-tuning (Ajuste Fino)**
Tomar un modelo de IA preentrenado y entrenarlo mas con tus propios datos especificos para que se vuelva mejor en un trabajo particular. Como contratar a un generalista y luego darle formacion especializada en el puesto.

### G

**GraphRAG**
Variante de RAG que organiza la informacion recuperada en un grafo de entidades y relaciones conectadas, haciendolo mejor en responder preguntas que requieren combinar hechos de multiples fuentes.

### H

**Harness Engineering (Ingenieria de Harness / Orquestacion)**
Disenar el sistema circundante --- herramientas, memoria, reglas y flujos de trabajo --- que envuelve un modelo de IA y moldea como se comporta en la practica. El modelo es el motor; el harness es todo el coche.

**Harness Synthesis (Sintesis de Harness)**
Clase de tecnicas en las que un optimizador de bucle externo (basado en busqueda, en observabilidad u otro) modifica automaticamente un harness --- sus herramientas, prompts, descomposicion de roles, topologia de comunicacion y protocolo de coordinacion --- a partir de senales en tiempo de ejecucion de la tarea objetivo. Vease **AHE** (arXiv 2604.25850) y **AgentFlow** (arXiv 2604.20801) como las dos implementaciones de referencia de abril de 2026. Distinto de *meta-harness* (un encuadre de 2025 / inicios de 2026 que trataba el harness como un objetivo de optimizacion de un solo paso, no como un artefacto en evolucion continua).

### I

**Inference (Inferencia)**
El proceso por el cual un modelo de IA genera una respuesta a tu entrada. Cada vez que envias un mensaje y obtienes una respuesta, el modelo esta haciendo inferencia.

**Iteration Head (Cabeza de Iteracion)**
Cabeza de atencion que emerge durante el razonamiento por cadena de pensamiento y atiende consistentemente a la salida del paso de razonamiento previo, identificada por el equipo de interpretabilidad de Anthropic en abril de 2026. Su existencia sugiere que el prompting CoT explicito funciona en parte induciendo un circuito interno especifico, no solo produciendo texto intermedio legible para humanos.

### K

**Knowledge Graph (Grafo de Conocimiento)**
Mapa estructurado de hechos donde las entidades (personas, lugares, conceptos) estan conectadas mediante relaciones etiquetadas. Como una red de fichas conectadas con cuerdas etiquetadas que muestran como todo se relaciona.

**KV-Cache**
Atajo de memoria que permite a la IA reutilizar calculos de partes anteriores de la conversacion en lugar de rehacerlos desde cero, haciendo las respuestas mas rapidas y baratas cuando el historial de conversacion permanece igual.

### L

**LLM (Large Language Model, Modelo de Lenguaje Grande)**
Sistema de IA entrenado con grandes cantidades de texto que puede entender y generar lenguaje humano. ChatGPT, Claude y Gemini son LLMs.

**Long Context (Contexto Largo)**
Capacidad de los modelos de IA mas nuevos de procesar grandes cantidades de texto a la vez --- a veces libros enteros o codebases completos --- dentro de una sola conversacion.

### M

**MCP (Model Context Protocol, Protocolo de Contexto del Modelo)**
Estandar abierto que permite a los asistentes de IA conectarse a herramientas y fuentes de datos externas a traves de una interfaz universal plug-and-play, como USB para aplicaciones de IA.

**Managed Agents (Agentes Gestionados)**
Modelo de runtime hosted en el que el sustrato del harness del agente --- sandbox, estado de sesion, ejecucion de herramientas con permisos acotados, trazado --- es operado por el proveedor del modelo en lugar del desarrollador. Anthropic envio el primer ejemplo comercial en beta publica el 8 de abril de 2026 ([platform.claude.com/docs/en/managed-agents/overview](https://platform.claude.com/docs/en/managed-agents/overview)). Segun la cobertura de lanzamiento de SiliconANGLE, el precio es la tarifa estandar de tokens de API mas un cargo por hora de ejecucion del agente para el sustrato (la cifra por hora no figura en la documentacion principal de Anthropic). Distinto de las superficies de disparo cloud-native (p. ej. Claude Code Routines), que se montan sobre un sustrato estilo Managed Agents pero responden una pregunta diferente: "que hace que el bucle empiece".

**Mechanistic Interpretability (Interpretabilidad Mecanicista)**
Programa de investigacion que apunta a identificar circuitos comprensibles para humanos dentro de los pesos de un modelo --- las caracteristicas, cabezas y rutas especificas que implementan un comportamiento dado. Nombrada una de las 10 Tecnologias Disruptivas de 2026 por MIT Technology Review, sustenta resultados de abril de 2026 como vectores de emocion, cabezas de iteracion y CoT monitoring.

**mHC (Manifold-Constrained Hyper-Connections, Hiper-Conexiones Restringidas a Variedad)**
Propuesta arquitectonica de DeepSeek de abril de 2026 que extiende las conexiones residuales enrutando multiples flujos de informacion internos a lo largo de una variedad de baja dimension aprendida. Generaliza el unico flujo residual usado en los modelos estilo Transformer++ a varios flujos coordinados; al momento de la publicacion, el resultado esta marcado **a la espera de replicacion independiente**.

**MIRAS**
Marco de entrenamiento aumentado con memoria de Google Research que provee las recetas, garantias de estabilidad y dinamicas de aprendizaje para arquitecturas como Titans, donde la memoria es un modulo neural entrenable que se actualiza en tiempo de inferencia. MIRAS es el marco que hace tratable "aprender mientras infieres" sin que el modulo de memoria diverja.

**MoE (Mixture of Experts, Mezcla de Expertos)**
Arquitectura de modelo en la que solo un subconjunto del "cerebro" del modelo se activa para cualquier entrada dada, lo que hace posible construir modelos muy grandes que siguen siendo rapidos porque no toda parte se ejecuta cada vez.

### O

**Obsidian**
Aplicacion de notas que almacena tus notas como archivos de texto plano en tu propio ordenador y te permite enlazarlas para formar una base de conocimiento personal.

### P

**Progressive Disclosure (Divulgacion Progresiva)**
Principio de diseno donde solo se muestra la informacion esencial primero y se revelan mas detalles bajo demanda. Como una pagina de FAQ: ves las preguntas y haces clic para expandir las respuestas que realmente necesitas.

**Prompt Engineering (Ingenieria de Prompts)**
Arte de escribir instrucciones a un modelo de IA de forma que se obtenga la mejor respuesta posible. Pequenos cambios en la redaccion pueden producir resultados muy distintos.

### R

**RAG (Retrieval-Augmented Generation, Generacion Aumentada por Recuperacion)**
Tecnica donde la IA busca informacion relevante en una fuente externa antes de responder, de modo que su respuesta este fundada en datos reales en lugar de depender unicamente de lo memorizado durante el entrenamiento.

**Routines (Claude Code)**
Primitiva de harness cloud-native de Anthropic para Claude Code de abril de 2026, en la que los flujos de trabajo del agente corren en la nube de Anthropic en lugar de en la maquina del usuario y pueden ser disparados por una programacion, una llamada API o un evento de GitHub. Routines generaliza los patrones cron-y-daemon auto-hospedados a un sustrato gestionado con niveles de cuota (Pro 5/dia, Max 15/dia, Team/Enterprise 25/dia) y sobrevive aunque el portatil del usuario este offline.

### S

**Self-RAG**
Variante de RAG donde la IA evalua su propia informacion recuperada y la respuesta generada en cuanto a calidad, decidiendo si recuperar mas o revisar su respuesta antes de darte el resultado final.

**Session-hour pricing (Precio por hora de sesion)** (tambien reportado como *agent-runtime-hour pricing*)
Modelo de facturacion que mide el asiento del orquestador --- el sustrato sobre el que corre un bucle de agente --- por separado de la inferencia. Introducido comercialmente por primera vez por Anthropic Managed Agents (8 de abril de 2026) a tarifas estandar de tokens mas ocho centavos por hora de ejecucion del agente, segun la cobertura de lanzamiento de SiliconANGLE. La cifra por hora no figura en la documentacion principal de Anthropic y se cita desde la prensa tecnica secundaria. Notable porque es la primera primitiva de proveedor que pone un numero al costo de "donde corre el bucle", distinto del costo de "que piensa el bucle". El fraseo exacto varia entre la documentacion principal (que habla de *sessions*) y la cobertura de prensa tecnica (que usa *agent runtime hour*); ambas se refieren a la misma superficie de medicion.

**Skill (AI Agent Skill)**
Capacidad reutilizable y empaquetada que un agente de IA puede invocar --- como una receta que sigue para una tarea especifica como "review this PR" o "run a daily review".

**Skill Graph (Grafo de Habilidades)**
Mapa de todas las habilidades disponibles para un agente de IA, incluyendo como se relacionan entre si y cuando debe dispararse cada una.

**System Prompt (Prompt del Sistema)**
Instrucciones ocultas dadas a un modelo de IA antes de que comience tu conversacion, estableciendo su rol, reglas y comportamiento. Como una descripcion del puesto que el empleado lee antes de su primer dia.

### T

**Task Budget (Presupuesto de Tarea)**
Primitiva de harness introducida por Anthropic en Claude Opus 4.7 (abril de 2026, header beta `anthropic-beta: task-budgets-2026-03-13`). El llamador declara un presupuesto de tokens consultivo para todo el bucle agentico --- pensamiento, llamadas a herramientas, resultados de herramientas, salida final --- y el modelo recibe una cuenta atras mientras trabaja, usandola para decidir cuanta busqueda, razonamiento y sintesis aun merece un paso. Distinto de `max_tokens`, que es un tope duro no visible para el modelo. Los presupuestos son consultivos en lugar de obligatorios, con un minimo de 20K tokens para evitar el comportamiento degenerado de rechazo en presupuestos ajustados. Task budgets es la primera primitiva enviada por un proveedor que expone "cuanto pensar en cada paso" como un **contrato gestionado** en lugar de un parametro ajustado a mano.

**Titans**
Familia de arquitectura de Google Research de abril de 2026 en la que la memoria es un modulo neural entrenable que se actualiza por descenso de gradiente en tiempo de inferencia, en lugar de un almacen vectorial externo o una ventana de atencion fija. Con cantidades comparables de parametros, Titans supuestamente supera a Mamba-2, Gated DeltaNet y Transformer++ en benchmarks de recuerdo a larga distancia y razonamiento multi-salto, difuminando la linea entre "contexto" y "fine-tuning".

**Token**
La unidad basica que un modelo de IA lee y escribe --- aproximadamente tres cuartos de una palabra en ingles. Los modelos piensan en tokens, y los precios y limites de contexto se miden en tokens.

**Tool Use / Function Calling (Uso de Herramientas / Llamada a Funciones)**
Capacidad de un modelo de IA de disparar acciones externas --- como buscar en la web, ejecutar codigo o llamar una API --- en lugar de solo generar texto.

### V

**Vector Database (Base de Datos Vectorial)**
Base de datos disenada especificamente para almacenar y buscar embeddings, haciendo rapido encontrar los items mas similares entre millones de entradas. El motor detras de la mayoria de los sistemas RAG.

### W

**Wikilink**
Enlace de doble corchete (como `[[Titulo de Nota]]`) usado en herramientas como Obsidian para conectar una nota con otra, creando una red de conocimiento enlazada.

---

[Volver al README](README_es.md)
