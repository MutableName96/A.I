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
La principal diferencia es que una red neuranal son que aqui tenemos las epocas que nos permiten ir ajustando nuestras predicciones en cada epoca
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
    un arbol de decisiones seria mas rapido para decidir si una transaccion es fraude o no y asu vez nos podria mostrar el proceso que llevo para saber si es fraude o no aunque es mas rigido ante cambios a su ves las redes neuronales multicapa nos resolveria estos cambios pero el volumen de datos de entrada tendria que ser mayor para que pueda dar resultados precisos.
    Yo en lo personal optaria arbol de desicion ya que es mas facil y eficiente detectar compras anormalas con estos datos

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
Tomaria en cuenta el costo de cada modelo en primero para poder saber el que tiene un costo operacionl mas grande, asu vez,  su adaptabilidad frente a nuevos cambios si en algun futuro la administracion quisiera hacer cambios en sus estrategias y tal vez el mas importante seria la interpretaccion de los datos ya que las redes neuronales al ser de caja negra no podria decirnos la razon por la que el alumno estaria reprobando esta info es valiosa para educadores para ajustar sus estrategias de aprendizaje .

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
En este caso preferia la precision, por el tema delicado de salvarguardar vidas que tienen mayor necesidad de ser atendidos, si bien es verdad que seria muy util saber en base a que necesitan atencion la mayor presicion nos permitiria atender la mayor cantidad de personas en riesgo sacrificando talvez velocidad de atencion ya que al poder tener mejor explicacion de el porque un paciente necesita atencion la logica diria que serian tratados de forma mas rapida pero esto al fin y acabo es desicion de un medico no del sistema. 

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
Se deberia analiza el nivel de confianza o probabilidad de cada predicción y el desempeño histórico de ambos modelos bajo condiciones similares. ya que no sabemos si uno esta considerando uno u otro no para que el resultado sea diferente, y pues el que este realizando mejor prediccion se veria una vez cuando la entrega pase y se vea que paso si sí si o sí no, para ver cual acerto
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
Depende de lo que quisiera hacer, si ayudar al cliente a que entienda     exactamente el porque de su rechazo o arriesgarnos a que no se nos pague aun cuando el modelo decidio que si se le deberia dar un credito o simplemente queremos mejores resultados con nuestros jefes o para la empresa podriamos obtar por no dar tantas explicaciones y que el numero dados de creditos sean menor o con clientes mas selectos excluyendo a gente que si pagarian perdiendo estos clientes   

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
Bueno si es verdad que hasta sierto punto tenemos una similitud con los modelos en algunos ecenarios pero es verdad que no son buenos para todos los ecenarios porque en problemas en que podemos optar por sacrificar presicion porque no es tan grande problema o la consecuencia de hacer sacrificios a problemas donde concebir un solo sacrificio puede llevar a problemas mayores,y tambien aunque un modelo sea mejor con su presicion de datos no sitrve de nada si no podemos interpretarlos como en el ejemplo de la escuela si el objetivo es ayudar a los alumnos subseptibles a reprobar es importante saber el por que porque se tienen que hacer cambios en el rumbo que se lleva porque por algo van reprobando y no nos serviria de nada solo saber que vamos a tener un indice alto de reprobados, no todos pueden permitirse tener una gran cantidad de datos para empezar tomando el ejemplo anterior de la escuela no es lo mismo el historial de una materia de la primera unidad a la ultima unidad de un alumno o el primer año al ultimo año de escuela , asu vez, modelos con mayor presicion necesitan mas datos para empezar a dar predicciones acertadas cosas que en problemas nuevos o mas complejos hay pocos o muy aleatorios con gran diferencia entre dato y dato, y tomar una mala de eleccion por un modelo mal entrenado puede afectar en nuestro mundo real  
>