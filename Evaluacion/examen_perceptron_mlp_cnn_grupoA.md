           ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            EXAMEN TEÓRICO — PERCEPTRÓN, MLP Y CNN (GRUPO A)

                            Eduardo Alcaraz
           ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


1 Datos del alumno
══════════════════

  ━━━━━━━━━━━
   Nombre    Antonio Lopez Martinez
   Grupo   A 
   Fecha    03/11/26
  ━━━━━━━━━━━


2 Pregunta 1 — Idea del perceptrón
══════════════════════════════════

  1. Explica qué recibe un perceptrón, qué hace con los pesos y el bias,
     y qué produce.
  2. ¿Qué quiere decir que dos clases sean *linealmente separables*?
  3. Señala *una* limitación fuerte del perceptrón de una sola capa.


2.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  ┌────
    
    1. un perceptron recibe datos y estos datos los multiplica pos los pesos q en un inicio son aleatorios y le summa el bias o el sesgo para ayudarle a ajustar el resultado
    2. literalmente que se pueden separar dos grupos de datos usando una linea recta, como separar peras de manzanaas
    3. No puede resolver problemas mas complejos en donde los datos no se pueden separar por una linea recta es decir estan tan mezclados q el preceptron no puede clasificarlos

  └────


3 Pregunta 2 — Por qué aparece el MLP
═════════════════════════════════════

  1. ¿En qué sentido un MLP es “más de una capa de neuronas”?
  2. ¿Para qué sirve la capa oculta ?
  3. Si quitas todas las activaciones no lineales, ¿qué tipo de
     comportamiento te queda y por qué importa?


3.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  ┌────

    1. porque ya maneja 3 capas q permiten reconocer patrones mas complejos
    2. es donde el modelo aprende los patrones mas complejjos
    3. se comportaria como uno lineal, si quitamos la virtud de las acttividades no lineales perderiamos esa gran ventaja de reconocer patrones mas complejos  
    
   └────


4 Pregunta 3 — XOR como lección histórica
═════════════════════════════════════════

  1. ¿Qué enseña el ejemplo XOR sobre el perceptrón simple?
  2. ¿Qué cambia al pasar a una red con capas ocultas y no linealidad?
  3. ¿Eso significa que el perceptrón nunca sirve en problemas reales?
     Argumenta.


4.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  ┌────

    1. q un perceptron s no puede resolver todos los problemas porq los resultados no se pueden separar por un linea recta
    2. que ya no usamos siempre una linea recta para separar los datos con las capas ocultas podemos llegar a usar limites mas complicados por asi decirlo
    3. no necesariamente solo servira cuando los datos no estan tan mezclados o q se pueden separar por una linea recta pues, problemas sencillos 

  └────


5 Pregunta 4 — Cómo “aprende” la red
════════════════════════════════════

  1. Describe con palabras el ciclo: predicción → medir error → ajustar
     pesos.
  2. ¿Qué controla el *learning rate* (tasa de aprendizaje) a nivel
     conceptual?
  3. Diferencia *subajuste* y *sobreajuste* con un ejemplo escolar
     breve.


5.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  ┌────

    1. es como jugar a las apuestas en un torneo primero haces una prediccion despues comparas tu respuesta con la correcta y en base a eso calcularias un error entonces modificarias los pesos q serian como los valores  q son mas importantes q tomaste en cuenta para predecir el resultado y repites
    2.  controla los pesos ya que con un learning rate el modelo puede pasarse o muy bajo aprender muy lento esto nos da principalmente q tanto cambian los pesos de un epoca a otra
    3. es como prepararse para el examen de ingreso a la facultad de medicina el subajuste seria cunado no estudias bien y no entiendes los temas del examen y el sobreajuste seria al contrario como si pagaras un curso milagroso q te diera segun todas las respuestas y tu las memorizas en lugar de comprender los temas q ya cuando haces un examen real con tantito q cambien la pregunta ya no la entiendas 

  └────


6 Pregunta 5 — Salidas: sigmoide y softmax
══════════════════════════════════════════

  1. ¿Cuándo usarías sigmoide y cuándo softmax?
  2. ¿Qué significa el vector que sale de un softmax en un problema de
     varias clases?
  3. Pon un ejemplo del curso (juego, riesgo, imágenes, etc.) y di qué
     salida encajaría.


6.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  ┌────

  └────


7 Pregunta 6 — Motivación de la CNN
═══════════════════════════════════

  1. ¿Qué inconveniente conceptual tiene aplastar una imagen y meterla a
     un MLP denso?
  2. ¿Qué aporta la idea de *filtro local* y *pesos compartidos*?
  3. Menciona *dos* dominios (además de fotos cotidianas) donde una CNN
     tiene sentido.


7.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  ┌────

  └────


8 Pregunta 7 — Piezas de una CNN
════════════════════════════════

  Explica el *para qué* de:
  1. Convolución
  2. Pooling
  3. Flatten + Dense al final
  4. Dropout durante el entrenamiento


8.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  ┌────

  └────


9 Pregunta 8 — Capas bajas vs capas altas
═════════════════════════════════════════

  1. ¿Qué suelen captar las primeras capas de una CNN frente a las más
     profundas?
  2. Usa una analogía (lupas, detectores, “de simple a complejo”).
  3. ¿Por qué “poner más capas” no garantiza mejor modelo?


9.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  ┌────

  └────


10 Pregunta 9 — Análisis: elige arquitectura
════════════════════════════════════════════

  Elige *Perceptrón (o lineal simple)* / *MLP* / *CNN* y justifica en
  *una* frase:

  1. Tabla de alumnos: promedio, faltas, horas de estudio → ¿aprueba?
  2. Clasificar el color de un semáforo en una fotografía.
  3. Clases en el plano que *no* se separan con una recta.
  4. ¿Usarías CNN para autocompletar código o una secuencia larga de
     texto? ¿Sí/no y qué alternativa del curso mencionarías?


10.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  ┌────

  └────


11 Pregunta 10 — Análisis: mirada de proyecto
═════════════════════════════════════════════

  1. Train accuracy altísima y validation baja: ¿qué sospechas? ¿Qué dos
     preguntas le harías al equipo en la defensa?
  2. ¿Por qué más neuronas o más capas no sustituyen un buen
     planteamiento del problema y buenos datos?
  3. Escribe *tres* preguntas orales (tuyas) para verificar que
     distinguen perceptrón, MLP y CNN.


11.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  ┌────

  └────
