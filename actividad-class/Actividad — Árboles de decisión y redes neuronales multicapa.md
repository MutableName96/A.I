# Actividad — Árboles de decisión y redes neuronales multicapa

Responda cada pregunta de manera clara y justificada.  
En las preguntas de análisis no basta con indicar qué algoritmo utilizaría; deberá explicar por qué considera que esa alternativa es adecuada para el problema planteado.

---

## Parte I. Conceptos y definiciones

### Pregunta 1
¿Qué es un árbol de decisión y cuál es su objetivo principal dentro de un problema de clasificación?

> **Respuesta:**  
    Un arbol de desicion es un algoritmo que nos permite saber en base a else ifs los caminos posibles de un problema ya que cada nodo es una pregunta sobre alguna dimencion y cada rama son las posibles respuestas a esa pregunta llevandonos asi hasta las hojass con su prediccion u otra desicion final
---

### Pregunta 2
Explique con sus propias palabras los siguientes elementos de un árbol de decisión:
- **Nodo raíz:**  La pregunta central de en que todos los datos se dividen
- **Nodo interno:** pregunta que se evalua sobre alguna caracteristica
- **Rama:**  los caminos que podria tomar 
- **Hoja:**  las predicciones 

---

### Pregunta 3
¿Qué es una red neuronal multicapa y qué función cumplen las siguientes capas?
- **Capa de entrada:**  Recibe los datos y los distribuye a la capa oculta
- **Capa oculta:**  Aqui se empieza el modelo a trabajar para ajustar sus pesos y econtrar patrones en bases a las caracteristicas que ecuentre
- **Capa de salida:** Aqui es donde se le da una interpretaccion a los datos de la capa anterior para dar una salida calculando funciones como el error y donde se realiza el backpropagacion hacia las capas aanteriores para ajustar las predicciones

---

### Pregunta 4
¿Qué representan los pesos y los sesgos dentro de una red neuronal?  
Explique también por qué sus valores cambian durante el entrenamiento.

> **Respuesta:**
los pesos nos indican que tanta importancia tiene esa caracteristicas en la neurona y el sesgo es un contrapeso que ayuda a la salida a dezplasarse   
> 

---

### Pregunta 5
¿Cuál es la principal diferencia entre la forma en que aprende un árbol de decisión y la forma en que aprende una red neuronal multicapa?  
Explique qué elementos aprende cada modelo.

> **Respuesta:**  
La principal diferencia es que una red neuranal endrente las epocas
> 

---

## Parte II. Análisis y aplicación

### Pregunta 6
Una institución bancaria desea desarrollar un sistema que detecte posibles compras fraudulentas.  
El sistema dispone de información como:
- Monto de la compra.
- Hora de la operación.
- Ciudad donde se realizó.
- Tipo de establecimiento.
- Número de compras realizadas durante el día.
- Historial de compras del cliente.

Analice las ventajas y desventajas de utilizar un árbol de decisión y una red neuronal multicapa.  
¿Cuál utilizaría y por qué?

> **Respuesta:**  
> 

---

### Pregunta 7
Una escuela quiere detectar estudiantes que presentan riesgo de reprobar una materia.  
Se conocen variables como:
- Asistencia.
- Calificaciones.
- Tareas entregadas.
- Participación.
- Número de materias reprobadas anteriormente.

Suponga que un árbol de decisión y una red neuronal obtienen prácticamente la misma precisión.  
¿Qué otros factores tomaría en cuenta para elegir uno de los dos modelos? Justifique su respuesta.

> **Respuesta:**  
> 

---

### Pregunta 8
Un hospital desarrolla un sistema para determinar qué pacientes necesitan atención prioritaria utilizando:
- Edad.
- Temperatura.
- Presión arterial.
- Frecuencia cardiaca.
- Síntomas.
- Antecedentes médicos.

Una red neuronal obtiene mejores resultados que un árbol de decisión, pero resulta más difícil explicar cómo obtuvo su respuesta.  
¿Considera que la mayor precisión es suficiente para elegir la red neuronal?  
Analice las consecuencias que podría tener esta decisión.

> **Respuesta:**  
> 

---

### Pregunta 9
Una empresa de reparto quiere predecir si un pedido llegará tarde considerando:
- Distancia.
- Tráfico.
- Clima.
- Hora del día.
- Cantidad de pedidos.
- Experiencia del repartidor.

Para determinado pedido:
- El **árbol de decisión** indica: *Llegará a tiempo*.
- La **red neuronal** indica: *Probablemente llegará tarde*.

¿Cómo determinaría cuál de los dos modelos está realizando una mejor predicción?  
Explique qué información adicional debería analizar.

> **Respuesta:**  
> 

---

### Pregunta 10
Una empresa desarrolla dos sistemas para decidir si una persona puede recibir un crédito:
1. El primer sistema utiliza un **árbol de decisión** y permite explicar claramente por qué una solicitud fue rechazada.
2. El segundo utiliza una **red neuronal multicapa** y obtiene mejores resultados de predicción, pero es más difícil explicar sus decisiones.

Si usted fuera responsable del proyecto:
- ¿Cuál de los dos modelos utilizaría?
- ¿Qué ventajas tendría su elección?
- ¿Qué riesgos tendría?
- ¿Consideraría posible utilizar ambos modelos dentro del mismo sistema?  
Justifique ampliamente su respuesta.

> **Respuesta:**  
> 

---

## Conclusión / Reflexión final

A partir de los ejercicios anteriores, explique brevemente la siguiente afirmación:

> *"No existe un algoritmo de Inteligencia Artificial que sea el mejor para todos los problemas."*

Relacione su respuesta con los siguientes conceptos:
- **Precisión**
- **Interpretabilidad**
- **Cantidad de datos**
- **Complejidad del problema**
- **Consecuencias de una decisión incorrecta**

> **Respuesta:**  
>