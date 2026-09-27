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
    | `tamano_obstaculo` | **Numérica** | Los obstáculos varían en tamaño; algunos requieren un salto anticipado o tardío, o ajustar la velocidad si vienen combinados, además de indicar si ya se superaron por completo. |
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
- Tamaño mínimo razonable: ¿cuántas filas o partidas harían falta para confiar? Argumenta.
- Riesgo si el dataset está mal definido: un error de diseño y su consecuencia.

### P3. ¿Qué tipo de obstáculo viene próximo?

- Variable objetivo (Y): ¿qué columna sería? ¿tipo? (numérica, categórica, binaria).
- Variables de entrada (X): lista mínimo 5 columnas que pedirías y por qué cada una.
- Granularidad: ¿necesitas un frame cada 16 ms, cada salto, o un resumen por partida?
- Tamaño mínimo razonable: ¿cuántas filas o partidas harían falta para confiar? Argumenta.
- Riesgo si el dataset está mal definido: un error de diseño y su consecuencia.

# 2. Diccionario y muestra (Misión 2)

## 3. Checklist EDA (Misión 3)
(respuestas a 3 preguntas + leakage + i.i.d.)

## 4. Interpretación de resúmenes (Misión 4)
(desbalance, métricas, dist_obstacle)

## 5. Elección de modelo (Misiones 5–6)
(tabla P1/P2/P3 + contraejemplos)