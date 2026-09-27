# Dino Crash EDA

## 1. Problema y dataset (Misión 1)
    
| ID | Pregunta de negocio / juego | ¿Una fila = qué? |
|---|---|---|
| P1 | ¿Morirá en el siguiente frame? | Un frame de una partida |
| P2 | ¿Cuántos puntos alcanzará esta partida al morir? | Una partida completa |
| P3 | ¿Qué tipo de obstáculo viene próximo? | Un frame o un evento |

### P1. ¿Morirá en el siguiente frame?

- Variable objetivo (Y): ¿qué columna sería? ¿tipo? (numérica, categórica, binaria).

    - crash | **binarica**
    

- Variables de entrada (X): lista mínimo 5 columnas que pedirías y por qué cada una.
    
    | Variable | Tipo | Descripción |
    | :--- | :--- | :--- |
    | `altura_dino` | **Numérica** | Determinar si la altura es suficiente para evitar colisionar con la hitbox de los obstáculos y calcular el tiempo de caída en base a la altura y la velocidad. |
    | `velocidad_obstaculo` | **Numérica** | Permite saber cuánto tiempo tardará el obstáculo en llegar a la posición del dinosaurio. |
    | `velocidad_caida` | **Numérica** | En el juego se puede aumentar la velocidad de caída agachándose; conocerla ayuda a predecir si caeremos sobre un obstáculo o si podemos evitar uno en el aire. |
    | `distancia_obstaculo` | **Numérica** | Ayuda a calcular el tiempo de impacto junto con la velocidad del obstáculo, determinando si está demasiado lejos o cerca al momento de saltar. |
    | `tamaño_obstaculo` | **Numérica** | Los obstáculos varían en tamaño; algunos requieren un salto anticipado o tardío, o ajustar la velocidad si vienen combinados, además de indicar si ya se superaron por completo. |
    | `agachado_dino` | **Binaria** | Indica el estado del dinosaurio (agachado o de pie) para esquivar aves a media altura; además, agacharse en el aire incrementa la velocidad de caída. |

- Granularidad: ¿necesitas un frame cada 16 ms, cada salto, o un resumen por partida?  
    
    decir que se ocupa un frame cada 16ms si hace referencia a el tiempo entre cada frame en una monitor de 60 hz no creo que fuera lo correcto porque excluimos monitorez de menor o mayor tasa de actualizacion pero si lo tomamos como tasa fija podria ser algo a considerar como solucion para evitar caer en perder datos si resumimos por partida porque entonces como sabremos si un cactus esta por matarnos, y si lo analizamos por cada salto como sabriamos si caeremos sobre el cactus si mientras caemos no podemos calcular el frame 

- Tamaño mínimo razonable: ¿cuántas filas o partidas harían falta para confiar? Argumenta.
    
    Como el objetivo es conseguir el maximo puntuaje ocupariamos unas de el puntuaje mas alto para que el modelo sepa reaccionar a varios ecenarios que se generan asi como tambien algunas con puntuajes bajos para que el modelo pueda diferenciar cuando muere y cuando el crash este en 0 porque si no pusieramos las de puntuaje bajo o donde muramos el modelo no sabria si ya perdio 
    
- Riesgo si el dataset está mal definido: un error de diseño y su consecuencia.

    podriamos tener un modelo que juegue tan bien en partidas altas donde la velocidad es muy alta pero pierda siempre con los obstaculos mas sencillos o si entramos el modelo con un target incorrecto como si ya murio el dinosaurio lo estariamos entrenando para detectar que el dinosaurio choco terminando la partida en lugar de evitar el peligro

### P2. ¿Cuántos puntos alcanzará esta partida al morir?

- Variable objetivo (Y): ¿qué columna sería? ¿tipo? (numérica, categórica, binaria).
    - score | **numerica**

- Variables de entrada (X): lista mínimo 5 columnas que pedirías y por qué cada una.    
        
    | Variable | Tipo | Descripción |
    | :--- | :--- | :--- |
    | `tiempo_reaccion` | **Numérica** | Cuánto tiempo tarda el modelo en reaccionar ante un nuevo obstáculo desde que aparece; ayuda a indicar si está rindiendo en partidas avanzadas o si entra en pánico ante nuevos obstáculos. |
    | `exactitud` | **Numérica** | Permite medir qué tan ajustados o perfectos son los saltos antes de una colisión para esquivar según el tamaño del obstáculo. |
    | `precision` | **Numérica** | Indica la consistencia del salto entre obstáculo y obstáculo, o si ante el mismo tipo de obstáculo presenta variaciones. |
    | `experiencia` | **Numérica** | Cantidad de partidas jugadas; a mayor número de intentos aumenta la probabilidad de un puntaje alto, aunque no garantiza superar los primeros compases. |
    | `saltos_innecesarios` | **Numérica** | Frecuencia con la que salta antes de tiempo o sin justificación, reflejando patrones de comportamiento propios de un jugador novato. |

- Granularidad: ¿necesitas un frame cada 16 ms, cada salto, o un resumen por partida?
    
    aunque podria ser util calcular frame por frame podriamos decir que si en algun momento tendriamos gran cantidad de datos con un mismo target entonces el modelo podria cofundirse y si calculamos por cada salto entonces perderiamos informacion valiosa entre los frames que nos permitaria calcular el tiempo de reaccion entonces la mejor opcion seria un resumen por partida 

- Tamaño mínimo razonable: ¿cuántas filas o partidas harían falta para confiar? Argumenta.
    
    dependiendo de la complejidad del modelo se ocuparia por lo muy muy menos unos mas de 500 a 1000 ecenarios donde en estos haya ecenearios donde haya partidas altas en base a datos de entrada presisos o con cierto patron para partidas altas y otro donde pueda ver que con otros patrones fuera de ese rango se puede obtener un puntuaje nulo o mas bajo porque buenos jugadores pueden cometer errores que los hagan perder con puntuajes bajos pero con tiempos de reaccion cerca de los altos 


- Riesgo si el dataset está mal definido: un error de diseño y su consecuencia.
    
    intentar usar la distancia_recorrida como variable de entrada estariamos diciendole al modelo cuanta distancia recorrera en la partida en lugar que predisca entonces no serviria de nada nuestro modelo.
    A su vez si eliminaramos variables de entrada el modelo consideraria que una experiencia alta es puntuajes altos cuando siempre no o tiempo de reacion buenos sin una experiencia previa no llegara lejos

### P3. ¿Qué tipo de obstáculo viene próximo?

- Variable objetivo (Y): ¿qué columna sería? ¿tipo? (numérica, categórica, binaria).
    - obstaculo | **categoria**
- Variables de entrada (X): lista mínimo 5 columnas que pedirías y por qué cada una.
    | Variable | Tipo | Descripción |
    | :--- | :--- | :--- |
    | `frecuencia_aparicion` | **Numérica** | Qué tan común es que aparezca un obstáculo, identificando cuáles son los más recurrentes y cuáles los menos habituales. |
    | `points_actuales` | **Numérica** | Ciertos obstáculos solo se generan al alcanzar cierto puntaje; según los puntos acumulados varía la probabilidad de aparición de cada tipo. |
    | `ultimo_obstaculo` | **Categórica** | Tipo del obstáculo inmediatamente anterior; no es común ver grandes sucesiones idénticas, por lo que ayuda a predecir el siguiente patrón. |
    | `distancia_segura` | **Numérica** | Espacio mínimo garantizado tras superar un obstáculo antes de generar el siguiente, evitando escenarios imposibles de superar. |
    | `velocidad_actual` | **Numérica** | Afecta directamente la frecuencia con la que se alcanzan los obstáculos; conocerla permite estimar el intervalo de llegada de las amenazas. |

- Granularidad: ¿necesitas un frame cada 16 ms, cada salto, o un resumen por partida?

    para este caso seria cada frame cada sierto tiempo aunque existe la posibilidad de tener frames donde no se generanran obstaculos nuevos tendriamos filas sin valor por lo que seria mejor tomar un frame por cada vez que el juego pasa un obstaculo con eso se podria decir que sabriamos cuando el motor generara un nuevo obstaculo porque si tomaramos por salto puede que en el ecenario ya hayan 2 obstaculos en lugar de calcular cada obstaculo y si nos vamos por resumen por partida solo calculariamos en todo caso un obstaculo y no nos sirve porque en una partida se generan n cantidad de obstaculos y no es unico solo 

- Tamaño mínimo razonable: ¿cuántas filas o partidas harían falta para confiar? Argumenta.

    se ocuparian una gran cantidad de filas estimando mas de 1000 por ecenario porque el juego permite combinacion de obstaculos y algunas veces repetidos en cantidades pequeñas asi como habra partidas que abajo de cierto puntuaje no genera aves y por lo que seria ideal que el modelo tuviera accesos a una gran cantidad de ejemplos de generaciones para que ecuentre un patron de generacion y si esto no es posible en base a propabilidades lo defina 

- Riesgo si el dataset está mal definido: un error de diseño y su consecuencia.
   
    si no consideramos que siertos obstaculos aparecen con puntuajes altos el modelo intentaria predecir obstaculos que nunca apareceran en puntuajes bajos alucinando la info 

# 2. Diccionario y muestra (Misión 2)
    Interceptaste un borrador de telemetría. Revisa si alcanza para P1 o si le falta algo.

| Columna | Tipo sugerido | Descripción breve |
| :--- | :--- | :--- |
| `session_id` | **Entero** | ID de partida |
| `frame` | **Entero** | Índice del frame en la partida |
| `time_ms` | **Entero** | Tiempo desde que empezó la partida |
| `score` | **Entero** | Puntuación en pantalla |
| `speed` | **Numérico** | Velocidad del escenario |
| `obstacle_type` | **Categórica** | `none`, `cactus_small`, `cactus_large`, `bird` |
| `dist_obstacle` | **Numérico** | Distancia al próximo obstáculo (px) |
| `jump` | **Binaria (0/1)** | ¿El dino está saltando? |
| `died` | **Binaria (0/1)** | 1 solo en el último frame de la sesión |

* Muestra para analizar (10 filas — sesión 7)

| frame | timems | score | speed | obstacletype | distobstacle | jump | died |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 6.0 | `none` | 180 | 0 | 0 |
| 40 | 640 | 8 | 6.4 | `none` | 165 | 0 | 0 |
| 80 | 1280 | 16 | 6.8 | `cactussmall` | 55 | 1 | 0 |
| 81 | 1296 | 16 | 6.8 | `cactussmall` | 38 | 1 | 0 |
| 82 | 1312 | 16 | 6.8 | `cactussmall` | 12 | 0 | 1 |
| 0 | 0 | 0 | 6.0 | `none` | 200 | 0 | 0 |
| 120 | 1920 | 24 | 7.2 | `bird` | 48 | 1 | 0 |
| 200 | 3200 | 40 | 8.0 | `none` | 150 | 0 | 0 |
| 280 | 4480 | 56 | 8.8 | `cactuslarge` | 22 | 0 | 1 |
| 50 | 800 | 10 | 6.5 | `cactussmall` | 90 | 0 | 0 |

**(Filas 1–5: misma sesión que termina en frame 82; filas 6–9: otras sesiones resumidas.)**

1. ¿Qué patrón ves en la fila donde died=1 (frame 82)?

    R. el dino no salto a pesaar de que el obstaculo estaba muy cerca porque el dino acababa de caer de el anterior obstaculo por lo que no pudo saltar

2. ¿=score= es buena variable para predecir muerte en el siguiente frame? ¿Por qué sí o no?

    R. no porque nos muestra el score que llevamos en el ultimo frame no si en el siguiente moriremos no es como que haya un indicador o el score se reinicie a 0 ahi talves podria servirnos

3. ¿Falta alguna columna crítica para P1? (pista: altura del dino, agachado, lag de reacción del jugador…)

    R. La mas obvia es si el dino esta agachado porque hay obstaculos que saltando moriremos y sera necesario agacharnos asi como con que velocidad estamos cayendo porque esta es variable

4. ¿=died= tal como está definida sirve para P1 o solo describe el final de la partida? 

    R. solo describe el final de la partida porque solo se cambia cuando el dino ya choco nunca nos dira si en el siguiente frame morira solo nos indica el pasado por lo que para P1 no nos sirve


## 3. Checklist EDA (Misión 3)

    Un dataset “bonito en papel” puede esconder trampas. El EDA responde esto antes de elegir modelo.

| # | Pregunta EDA | ¿Qué buscas? | Si la respuesta es mala, ¿qué modelo evitas o qué haces? |
| :-: | :--- | :--- | :--- |
| **1** | ¿Cuántas observaciones hay? | Tamaño N, partidas | Evitar modelos complejos con pocos datos (riesgo de sobreajuste). |
| **2** | ¿Hay valores faltantes? | % NA por columna | Algunos modelos no toleran NA; imputar valores o descartar registros. |
| **3** | ¿La clase objetivo está balanceada? (P1) | % muerte vs no-muerte por frame | Métrica accuracy engañosa; considerar F1, ponderar clases o submuestrear. |
| **4** | ¿Hay fugas de información (leakage)? | ¿$Y$ incluye el futuro? | Cualquier modelo dará una métrica “perfecta” en validación falsa; rediseñar features. |
| **5** | ¿Variables correlacionadas? | `score` vs `timems` | Regresión inestable por multicolinealidad; eliminar redundancia. |
| **6** | ¿Distribución de `speed`? | ¿Sube siempre? ¿Tope máximo? | Cuidado con modelos que asumen linealidad infinita. |
| **7** | ¿Outliers? | `distobstacle` negativo, saltos imposibles | Limpiar y filtrar anomalías antes de entrenar. |
| **8** | ¿Datos i.i.d.? | ¿Los frames de la misma sesión son independientes? | Realizar split Train/Test por sesión (partida), no por fila suelta. |
| **9** | ¿Estacionariedad? | ¿Misma distribución al inicio y al final? | Un modelo global puede fallar en partidas largas; segmentar por fases. |
| **10** | ¿Sesgo de muestreo? | ¿Solo jugadores expertos? ¿Solo móvil? | Generalización dudosa; recolectar perfiles y entornos variados. |

**Elige tres preguntas del checklist y respóndelas como si tuvieras el dataset completo del dino (hipótesis razonables).**

     

1. p2-¿Hay valores faltantes?
     
     R. En el juego del dinosaurio dependiendo de tus variables de entrada podriamos decir que si pueden existir faltantes como cuando no hay obstaculos entonces variables como distancia del obstaculo o ancho de el mismo son nulas

     se podria arrreglar estados que nos indiquen que no hay nada como poner en tipo de objeto ninguno o en temas de altura como 0 para intentar que el modelo no se rompa o simplemente evitando usar modelos inadecuados

2. p9-¿Estacionariedad? 
    
    R. Los datos son cambiantes no son estacionarios al inicio solo hay cactus y la velocidad es baja despues la velocidad aumenta y nuevos obstaculos salen no es lo mismo una partida antes de las aves que una despues
    
    La solucion seria evitar modelos lineales que esperqn estacionariedad en los datos

    3. p10-¿Sesgo de muestreo?

    R. Es muy probable porque si tomamos las pruebas para monitorez de hz fija puede alterarse despues con diferentes asi como si tomamos partidas de solo novatos que no hacen mas de 400 puntos y viciversa con expertos 

    Lo mejor para esto seria reunir una muestra balanceada aunque puede haber infinita cantidad de condiciones se podria generalizar en base de nuestro target para obtener resultados balanceados

**Para la pregunta 8 (i.i.d.): explica por qué mezclar frames de la misma partida en entrenamiento y prueba es un error.** 
Es un error porque en el juego del dino si hay dependencia entre filas el frame 100 es necesario en el contecto del 101 para saber que esta pasando si sacas un frame a entrenamiento y el siguiente a prueba, el modelo solo esta memorizando la partida en lugar de aprender a jugar

**Da un ejemplo concreto de data leakage usando score o time_ms en P1.**

Por ejemplo si metieramos time_ms y que cuando choco el reloj se para en seco, el modelo va a aprender que reloj parado equivale a choque o si se pone en 0.
Asi solo se aprende que si el reloj se para perdiste no te ayuda a esquivar

o si al score usaramos algo como score_final le estamos diciendo al modelo que ya sabemos el score resultante antes de que juegue en una partida real nadie sabe cuál será el puntaje final antes de perder

## 4. Interpretación de resúmenes (Misión 4)
    Te pasan resúmenes estadísticos en lugar de código. Debes sacar conclusiones.

* Resumen estadístico (50 partidas, ~12 000 frames)

| Variable | Media | Mediana | Mín | Máx | Comentario del analista previo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `score` (por frame) | 28 | 18 | 0 | 120 | Cola larga hacia la derecha |
| `speed` | 8.5 | 8.2 | 6.0 | 13.0 | Sube con el tiempo de partida |
| `dist_obstacle` | 95 | 88 | 5 | 220 | Muertes suelen con dist < 20 |
| `died` (por frame) | — | — | — | — | Solo 50 unos en todo el dataset |

* Conteos de `obstacle_type` (todos los frames)

| Tipo | % aprox. |
| :--- | :---: |
| `none` | 54% |
| `cactussmall` | 20% |
| `cactuslarge` | 15% |
| `bird` | 11% |

- ¿El problema P1 (muerte en siguiente frame) está desbalanceado? Cuantifica con los números dados

    de todos esos frames solo hay 50 que nos pudieron haber servido para predecir muertes y los demas solo el dino esta vivo 

    $50 frames / 12,000 frames \approx 0.42\%$ esto es de echo es un porcentaje engañoso de acierto (99%) aunque el dino pierda siempre.

- ¿Qué implica eso para la métrica que usarías? (accuracy vs precision/recall/F1).

    si usaramos exactitud estamos hablando de que el dino se moriria en todos los casos debemos usar las otras metricas para saber si si esta detectando las posibles muertes a tiempo 

- ¿=distobstacle= parece útil como predictor? Argumenta con la fila de muertes.

    es de los valores mas utiles ya que la tabla nos da un dato muy relevante que es "Muertes suelen ser dist < 20" entonces aqui si hay un patron que el modelo podria aprender   

- ¿La distribución de score sugiere regresión simple o necesitas transformación / otro enfoque?

    seria usar otro enfoque porque los datos nos indican que la mayoría pierde rápido con puntuaciones bajas y muy pocas partidas tienen un puntuaje alto

## 5. Elección de modelo (Misiones 5–6)

    El mando quiere una guía para no elegir modelos de moda sin datos que los soporten.

* Tabla guía: Elección de modelo según hallazgos del EDA

| Si tu EDA encuentra… | Tipo de problema | Modelos razonables | Modelos poco razonables (y por qué) |
| :--- | :--- | :--- | :--- |
| **$Y$ binaria, tabular, $N$ mediano** | Clasificación | Regresión logística, árbol de decisión, Random Forest | Red profunda sin más datos (alto riesgo de *overfitting*). |
| **$Y$ binaria muy desbalanceada** | Clasificación | Mismo + `class_weight`, ajuste de umbral, SMOTE (con cuidado) | Modelos evaluados con *Accuracy* como única métrica (falso sentido de éxito). |
| **$Y$ numérica (score final)** | Regresión | Regresión lineal, árbol regresor, Ridge/Lasso | Clasificador binario (pierde la escala y magnitud del puntaje). |
| **$Y$ categórica multiclase (tipo obstáculo)** | Clasificación multiclase | Regresión logística multinomial, Random Forest | Regresión lineal sobre códigos 1, 2, 3 (asume orden o distancia numérica artificial). |
| **Secuencia de frames por sesión** | Serie / secuencia | *Feature engineering* (ventanas/lags) + clasificador; LSTM/GRU si hay volumen alto | Ignorar el orden temporal (tratar los frames como muestras i.i.d.). |
| **Relación clara y lineal, pocas variables** | Interpretable | Regresión logística / lineal | *Ensemble* opaco y complejo sin necesidad real. |
| **Muchas variables categóricas** | Tabular | Árboles de decisión, codificación *ordinal / one-hot* | Modelos basados en distancia euclidiana cruda sobre variables categóricas. |

---

* Tu Tarea: Propuesta de modelo por escenario

Para cada escenario del inicio:

| Escenario | Tras tu EDA, ¿qué fila de la guía aplica? | Modelo que propondrías | 2 condiciones del dataset que deben cumplirse |
| :---: | :--- | :--- | :--- |
| **P1** | | | |
| **P2** | | | |
| **P3** | | | |