**Introducción: ¿Qué es Prolog y el paradigma lógico?**

En esta práctica se exploró Prolog, uno de los lenguajes de programación más representativos del paradigma lógico, utilizado ampliamente en inteligencia artificial, sistemas expertos, resolución automática de problemas y modelado de conocimiento. A diferencia de lenguajes imperativos como Java, C o Python —donde el programador debe especificar paso a paso cómo resolver un problema, ya que Prolog se basa en describir qué es verdadero mediante hechos y reglas, dejando que el motor lógico del lenguaje determine cómo encontrar una solución. Esta forma de pensar desplaza el enfoque tradicional de la programación y permite construir sistemas que razonan de manera declarativa.

El funcionamiento de Prolog se apoya en tres conceptos fundamentales: unificación, recursión y backtracking. La unificación permite comparar estructuras lógicas y vincular variables; la recursión permite procesar estructuras complejas como listas, árboles o grafos; y el backtracking conduce a Prolog a explorar alternativas automáticamente, volviendo atrás cuando una posible solución no funciona. Gracias a estos mecanismos, Prolog es capaz de resolver problemas de búsqueda, planificación, deducción y simulación con una base de conocimiento relativamente pequeña.

**Instalación y entorno de trabajo**

Según TutorialsPoint: para Windows se sugiere GNU Prolog (versión 1.4.5 en su ejemplo) como entorno de Prolog. 

Pasos típicos:
Descargar el ejecutable desde el sitio oficial. 
Ejecutar el instalador, elegir directorio, etc.
Una vez instalado, puedes lanzar el intérprete de Prolog o cargar archivos .pl. 
Ejemplo de archivo “Hello World”:
write('Hello World').

en la consola de Prolog produce: Hello World. 

**Nota práctica:** Hay que asegurar de que el intérprete esté apuntando al directorio correcto donde se guarda el programas, y recordar siempre que cada cláusula/fact termina con un punto (.).

**¿Cómo funciona Prolog? Mecanismos clave**
**Hechos, reglas y consultas**

**Hechos:** afirmaciones que son incondicionalmente verdaderas. Ejemplo: cat(tom). 

**Reglas:** implican condiciones. Se usa :- para “si”. Ejemplo:

grandfather(X, Y) :- father(X, Z), parent(Z, Y).

Esto indica: “X es abuelo de Y si X es padre de Z y Z es padre/madre de Y”. 

**Consultas:** preguntas al sistema, por ejemplo ?- grandfather(jack, bob).

La base de conocimiento es el conjunto de **hechos + reglas**. 

**Unificación y variables**

Las variables comienzan con letra mayúscula o **(_)**. Ej: X, Y. 

**Unificación:** Prolog intenta hacer “coincidir” términos, enlazando variables con valores de modo que la igualdad quede satisfecha. Por ejemplo, X = 5 unifica X con 5. 

**Atomos, números, estructuras:** Prolog maneja diferentes tipos de “objetos de datos”. 

**Recursión**

En Prolog, la recursión es un mecanismo común para repetir o procesar estructuras (listas, árboles, etc.). Por ejemplo, se puede definir un predicado que se llama a sí mismo con argumentos “más pequeños” hasta una condición base. 

Ejemplo:

predecessor(X, Z) :- parent(X, Z).
predecessor(X, Z) :- parent(X, Y), predecessor(Y, Z).

Esto define “predecesor” recursivamente. 

**3.4 Backtracking**

El backtracking (retroceso) es un mecanismo interno de Prolog por el cual, al intentar resolver una consulta, si una rama de búsqueda falla, el sistema vuelve atrás (“deshace” elecciones) para probar alternativas. 

Por ejemplo: si tienes varias reglas que podrían aplicarse, Prolog probará la primera, si conduce al fallo, retrocede y prueba la siguiente. 

Este mecanismo permite que Prolog encuentre todas las soluciones posibles (hasta que el usuario deje de pedir más) o compruebe que no hay más.

**“Different” y “Not”**

En el tutorial se menciona el predicado \== para indicar que dos términos no son iguales. Ejemplo: X \== Y verifica que X y Y no unifiquen. 

También se puede usar la negación por fallo (\+) en los sistemas Prolog para especificar que algo no es cierto porque no puede demostrarse. (Aunque el tutorial de TutorialsPoint lo menciona como “Different and Not”).

**Qué cosas se pueden aprender con Prolog / para qué sirve**

* Manejo de estructuras de datos lógicas: listas, árboles, grafos.
* Modelado de conocimiento: hechos, relaciones, reglas lógicas.
* Resolución automática de consultas, inferencia lógica.
* Recursión, backtracking: técnicas de búsqueda algorítmica.
* Aplicaciones en IA, procesamiento de lenguaje natural, sistemas expertos, bases de datos lógicas.
* Cambiando la mentalidad al pasar de “voy a dar instrucciones” a “voy a declarar lo que es verdadero” y dejar que el sistema lo resuelva.

**Cómo usarlo: pasos básicos de un programa Prolog**

1. Abrir el intérprete de Prolog.
2. Crear un archivo .pl con tus hechos y reglas.
3. Consultar ese archivo (por ejemplo en GNU Prolog: [miPrograma].). 
4. Formular consultas/predicados para que Prolog devuelva respuestas.
5. Usar variables para preguntas generales, y ; (punto y coma) para pedir la siguiente solución. 
6. En algunos entornos puedes usar trace. para ver cómo Prolog hace la búsqueda y backtracking. Ejemplo en el tutorial del árbol familiar. 

**TEMAS DE LA TERCERA SESIÓN**

Estructuras de datos y recursión
Backtracking
Diferente y no
Estudio de caso: Árbol
Programas básicos
Mínimo y máximo
Circuitos resistivos
Segmentos de recta Torre de Hanoi
Lista enlazados
El mono y el plátano

**Prolog - Programas básicos**
En el siguiente capítulo, discutiremos ejemplos básicos de prólogo para −
Encuentra el mínimo máximo de dos números
Encuentra la resistencia equivalente de un circuito resistivo
Verifique si un segmento de línea es horizontal, vertical u oblicuo

**Estudio de caso: Árbol**

En la guía se muestra un ejemplo de árbol (estructura jerárquica) y cómo recorrerla usando recursión. 

**Por ejemplo:** representar element(buch, [titulo='Peer Gynt'], [ … ]) como árbol en Prolog. 

Puedes definir predicados como “es antepasado de” que recorren el árbol de padres a hijos, etc.

En el contexto de la práctica, podrías mostrar un pequeño árbol genealógico o de datos, definir los predicados correspondientes (padre, madre, hijo, antepasado) y hacer consultas.

**Máximo y mínimo de dos números** MaxyMin.p1
Aquí veremos un programa Prolog, que puede encontrar el mínimo de dos números y el máximo de dos números. Primero, crearemos dos predicados, find_max(X,Y,Max). Esto toma los valores X e Y y almacena el valor máximo en el Máx. Similarmente find_min(X,Y,Min) toma los valores X e Y y almacena el valor mínimo en la variable Min.

Programa
find_max(X, Y, X) :- X >= Y, !.
find_max(X, Y, Y) :- X < Y.

find_min(X, Y, X) :- X =< Y, !.
find_min(X, Y, Y) :- X > Y.

Salida

| ?- find_max(100,200,Max).
Max = 200
yes

| ?- find_max(40,10,Max).
Max = 40
yes

| ?- find_min(40,10,Min).
Min = 10
yes

| ?- find_min(100,200,Min).
Min = 100
yes

**Circuitos de resistencia y resistivos** Circuitos.p1
En esta sección veremos cómo escribir un programa prolog que nos ayudará a encontrar la resistencia equivalente de un circuito resistivo.

Tenemos que encontrar la resistencia equivalente de esta red. Al principio, intentaremos obtener el resultado a mano y luego intentaremos ver si el resultado coincide con la salida del prólogo o no.

Sabemos que hay dos reglas 

Si R1 y R2 están en serie, entonces la resistencia equivalente Re = R1 + R2.
Si R1 y R2 están en paralelo, entonces la resistencia equivalente Re = (R1 * R2)/(R1 + R2).

Aquí las resistencias de 10 ohmios y 40 ohmios están en paralelo, luego eso está en serie con 12 ohmios, y la resistencia equivalente de la mitad inferior es paralela con 30 ohmios. Así que intentemos calcular la resistencia equivalente.

R3 = (10 * 40)/(10 + 40) = 400/50 = 8 ohmios
R4 = R3 + 12 = 8 + 12 = 20 ohmios
R5 = (20 * 30)/(20 + 30) = 12 ohmios

Programa
series(R1,R2,Re) :- Re is R1 + R2.
parallel(R1,R2,Re) :- Re is ((R1 * R2) / (R1 + R2)).

Salida

| ?- parallel(10,40,R3).
R3 = 8.0
yes

| ?- series(8,12,R4).
R4 = 20
yes

| ?- parallel(20,30,R5).
R5 = 12.0
yes

| ?- parallel(10,40,R3),series(R3,12,R4),parallel(R4,30,R5).
R3 = 8.0
R4 = 20.0
R5 = 12.0
yes

**Segmentos de línea horizontales y verticales** SGD.P1
Hay tres tipos de segmentos de línea: horizontales, verticales u oblicuos. Este ejemplo verifica si un segmento de línea es horizontal, vertical u oblicuo.

Para líneas horizontales, los valores de las coordenadas y de dos puntos finales son los mismos.
Para líneas verticales, los valores de las coordenadas x de dos puntos finales son los mismos.
Para líneas oblicuas،las coordenadas (x,y) de dos puntos finales son diferentes.
Ahora veamos cómo escribir un programa para comprobar esto.

Programa
vertical(seg(point(X,_),point(X,_))).

horizontal(seg(point(_,Y),point(_,Y))).

oblique(seg(point(X1,Y1),point(X2,Y2)))
   :-X1 \== X2,
      Y1 \== Y2.
Salida

| ?- vertical(seg(point(10,20), point(10,30))).
yes

| ?- vertical(seg(point(10,20), point(15,30))).
no

| ?- oblique(seg(point(10,20), point(15,30))).
yes

| ?- oblique(seg(point(10,20), point(15,20))).
no

| ?- horizontal(seg(point(10,20), point(15,20))).
yes

**Prolog - Problema de las Torres de Hanoi** TDH.p1
El problema de las Torres de Hanoi es un famoso rompecabezas para mover N discos desde la clavija/torre de origen a la clavija/torre de destino utilizando la clavija intermedia como clavija de sujeción auxiliar. Hay dos condiciones que se deben seguir al resolver este problema.

* Un disco más grande no se puede colocar sobre un disco más pequeño.
* Sólo se puede mover un disco a la vez.

Para resolver esto, tenemos que escribir un procedimiento move(N, Source, Target, auxiliar). Aquí será necesario desplazar N número de discos desde la clavija de origen a la clavija de destino, manteniendo la clavija auxiliar como intermedia.

Por ejemplo, move(3, origen, destino, auxiliar).

* Mueva el disco superior del origen al destino
* Mueva el disco superior de la fuente al auxiliar
* Mueva el disco superior del objetivo al auxiliar
* Mueva el disco superior del origen al destino
* Mueva el disco superior del auxiliar a la fuente
* Mueva el disco superior del auxiliar al objetivo
* Mueva el disco superior del origen al destino

Programa
move(1,X,Y,_) :-
   write('Move top disk from '), write(X), write(' to '), write(Y), nl.
move(N,X,Y,Z) :-
   N>1,
   M is N-1,
   move(M,X,Z,Y),
   move(1,X,Y,_),
   move(M,Z,Y,X).
Salida

| ?- move(4,source,target,auxiliary).
Move top disk from source to auxiliary
Move top disk from source to target
Move top disk from auxiliary to target
Move top disk from source to auxiliary
Move top disk from target to source
Move top disk from target to auxiliary
Move top disk from source to auxiliary
Move top disk from source to target
Move top disk from auxiliary to target
Move top disk from auxiliary to source
Move top disk from target to source
Move top disk from auxiliary to target
Move top disk from source to auxiliary
Move top disk from source to target
Move top disk from auxiliary to target

true ?

(31 ms) yes

**Prolog - Listas enlazadas** le.p1
Los siguientes capítulos describen cómo generar/crear listas enlazadas utilizando estructuras recursivas.

La lista enlazada tiene dos componentes, la parte entera y la parte de enlace. La parte del enlace contendrá otro nodo. El final de la lista tendrá nulo en la parte del enlace.

En prolog, podemos expresar esto usando nodo(2, nodo(5, nodo(6, nulo))).

**Nota:** La lista más pequeña posible es nula y todas las demás listas contendrán nulo como "siguiente" del nodo final. En la terminología de listas, el primer elemento suele denominarse cabeza de la lista, y el resto de la lista se llama cola parte. Por lo tanto, el encabezado de la lista anterior es 2 y su cola es el nodo de la lista (5, nodo (6, nulo)).

También podemos insertar elementos en la parte delantera y trasera

Programa
add_front(L,E,NList) :- NList = node(E,L).

add_back(nil, E, NList) :-
   NList = node(E,nil).
   
add_back(node(Head,Tail), E, NList) :-
   add_back(Tail, E, NewTail),
   NList = node(Head,NewTail).

Salida

| ?- add_front(nil, 6, L1), add_front(L1, 5, L2), add_front(L2, 2, L3).
L1 = node(6,nil)
L2 = node(5,node(6,nil))
L3 = node(2,node(5,node(6,nil)))
yes

| ?- add_back(nil, 6, L1), add_back(L1, 5, L2), add_back(L2, 2, L3).
L1 = node(6,nil)
L2 = node(6,node(5,nil))
L3 = node(6,node(5,node(2,nil)))
yes

| ?- add_front(nil, 6, L1), add_front(L1, 5, L2), add_back(L2, 2, L3).
L1 = node(6,nil)
L2 = node(5,node(6,nil))
L3 = node(5,node(6,node(2,nil)))
yes

**Prolog - Problema del mono y el plátano** mono.p1
En este ejemplo de prólogo, veremos un problema muy interesante y famoso: el problema del mono y el plátano.

**Planteamiento del problema**
Supongamos que el problema es el que se indica a continuación 

* Un mono hambriento está en una habitación y está cerca de la puerta.
* El mono está en el suelo.
* Se han colgado plátanos del centro del techo de la habitación.
* Hay un bloque (o silla) presente en la habitación cerca de la ventana.
* El mono quiere el plátano, pero no puede alcanzarlo.
* 
Entonces, ¿cómo puede el mono conseguir los plátanos?
Entonces, si el mono es lo suficientemente inteligente, puede llegar al bloque, arrastrarlo hasta el centro, treparlo y conseguir el plátano. A continuación se presentan algunas observaciones en este caso 

* El mono puede alcanzar el bloque si ambos están al mismo nivel. En la imagen de arriba podemos ver que tanto el mono como el bloque están en el suelo.
* Si la posición del bloque no está en el centro, entonces el mono puede arrastrarlo hacia el centro.
* Si tanto el mono como el bloque están en el suelo y el bloque está en el centro, entonces el mono puede trepar al bloque. Entonces se cambiará la posición vertical del mono.
* Cuando el mono está en el bloque y el bloque está en el centro, entonces el mono puede conseguir los plátanos.

Ahora veamos cómo podemos resolver esto usando Prolog. Crearemos algunos predicados de la siguiente manera 
Tenemos algunos predicados que se moverán de un estado a otro, al realizar acciones.

* Cuando el bloque está en el medio y el mono está encima del bloque y el mono no tiene el plátano (es decir no tiene estado), luego usando el grasp acción, cambiará de no tiene Estado a have estado.
* Desde el suelo, puede moverse a la parte superior del bloque (es decir. encima estado), realizando la acción escalar.
* El push o arrastrar La operación mueve el bloque de un lugar a otro.
* El mono puede moverse de un lugar a otro usando caminar o mover cláusulas.

Otro predicado será canget(). Aquí pasamos un estado, por lo que esto realizará un movimiento de predicado de un estado a otro usando diferentes acciones, luego realizará canget() en el estado 2. Cuando hayamos llegado al estado âtiene>, esto indica -tiene plátano. Detendremos la ejecución.

Programa
move(state(middle,onbox,middle,hasnot),
   grasp,
   state(middle,onbox,middle,has)).
move(state(P,onfloor,P,H),
   climb,
   state(P,onbox,P,H)).
move(state(P1,onfloor,P1,H),
   drag(P1,P2),
   state(P2,onfloor,P2,H)).
move(state(P1,onfloor,B,H),
   walk(P1,P2),
   state(P2,onfloor,B,H)).
canget(state(_,_,_,has)).
canget(State1) :-
   move(State1,_,State2),
   canget(State2).
Salida

| ?- canget(state(atdoor, onfloor, atwindow, hasnot)).

true ?

yes
| ?- trace
.
The debugger will first creep -- showing everything (trace)
yes

{trace}
| ?- canget(state(atdoor, onfloor, atwindow, hasnot)).
      1 1 Call: canget(state(atdoor,onfloor,atwindow,hasnot)) ?
      2 2 Call: move(state(atdoor,onfloor,atwindow,hasnot),_52,_92) ?
      2 2 Exit:move(state(atdoor,onfloor,atwindow,hasnot),walk(atdoor,_80),state(_80,onfloor,atwindow,hasnot)) ?
      3 2 Call: canget(state(_80,onfloor,atwindow,hasnot)) ?
      4 3 Call: move(state(_80,onfloor,atwindow,hasnot),_110,_150) ?
      4 3 Exit: move(state(atwindow,onfloor,atwindow,hasnot),climb,state(atwindow,onbox,atwindow,hasnot)) ?
      5 3 Call: canget(state(atwindow,onbox,atwindow,hasnot)) ?
      6 4 Call: move(state(atwindow,onbox,atwindow,hasnot),_165,_205) ?
      6 4 Fail: move(state(atwindow,onbox,atwindow,hasnot),_165,_193) ?
      5 3 Fail: canget(state(atwindow,onbox,atwindow,hasnot)) ?
      4 3 Redo: move(state(atwindow,onfloor,atwindow,hasnot),climb,state(atwindow,onbox,atwindow,hasnot)) ?
      4 3 Exit: move(state(atwindow,onfloor,atwindow,hasnot),drag(atwindow,_138),state(_138,onfloor,_138,hasnot)) ?
      5 3 Call: canget(state(_138,onfloor,_138,hasnot)) ?
      6 4 Call: move(state(_138,onfloor,_138,hasnot),_168,_208) ?
      6 4 Exit: move(state(_138,onfloor,_138,hasnot),climb,state(_138,onbox,_138,hasnot)) ?
      7 4 Call: canget(state(_138,onbox,_138,hasnot)) ?
      8 5 Call:   move(state(_138,onbox,_138,hasnot),_223,_263) ?
      8 5 Exit: move(state(middle,onbox,middle,hasnot),grasp,state(middle,onbox,middle,has)) ?
      9 5 Call: canget(state(middle,onbox,middle,has)) ?
      9 5 Exit: canget(state(middle,onbox,middle,has)) ?
      7 4 Exit: canget(state(middle,onbox,middle,hasnot)) ?
      5 3 Exit: canget(state(middle,onfloor,middle,hasnot)) ?
      3 2 Exit: canget(state(atwindow,onfloor,atwindow,hasnot)) ?
      1 1 Exit: canget(state(atdoor,onfloor,atwindow,hasnot)) ?
      
true ?