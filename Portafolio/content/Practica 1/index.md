Introducción

Los lenguajes de programación son la herramienta fundamental para la construcción de software, ya que permiten expresar soluciones a problemas de manera estructurada y comprensible tanto para las personas como para la computadora. Cada lenguaje está conformado por un conjunto de elementos esenciales que definen su funcionamiento y su forma de interacción con el hardware y la memoria del sistema.

En esta práctica se busca identificar dichos elementos básicos dentro de una aplicación desarrollada en el lenguaje C, tomando como ejemplo un sistema de administración de biblioteca. A lo largo del análisis se reconocen conceptos como el uso de nombres e identificadores, los marcos de activación generados en las llamadas a funciones, los bloques de alcance de las variables, la administración de memoria (estática, dinámica y automática), así como las expresiones, comandos y estructuras de control que dirigen el flujo de ejecución.

Asimismo, se exploran la definición y uso de subprogramas, tanto funciones como procedimientos, y los distintos tipos de datos que van desde los primitivos hasta estructuras compuestas como registros, listas enlazadas y enumeraciones. Con este ejercicio se busca reforzar la comprensión de la manera en que estos conceptos se manifiestan en un programa real, facilitando así el aprendizaje de los fundamentos de la programación estructurada.

Objetivo.

El objetivo de esta práctica es identificar los elementos fundamentales de los lenguajes de programación: nombres, marcos de activación, bloques de alcance, administración de memoria, expresiones, comandos, control de secuencia como lo es; selección, iteración y recursión, subprogramas, y tipos de datos.

Resultados.

1. Nombres
Son los identificadores que se utilizan para variables, funciones, estructuras y tipos definidos:
•	Variables: static_var, bss_var, bookCount, memberCount, choice.
•	Funciones: addBook, displayBooks, issueBook, returnBook, etc.
•	Tipos: book_t, member_t, genre_t.

2. Marcos de activación (Activation Records)
Cada vez que se llama a una función, se crea un marco de activación en el stack, donde se almacenan:
•	Parámetros formales (book_t **library, int* count en addBook).
•	Variables locales (new_book en addBook, current_book en issueBook).
•	Dirección de retorno (para volver al punto de llamada).
Ejemplo:
Cuando se ejecuta addBook, se crea un marco de activación en el stack con todas sus variables automáticas, y al terminar se destruye.

3. Bloques de alcance (Scope Blocks)
•	Globales: bss_var, static_var, tipos struct, enum, funciones definidas fuera de main.
•	Locales: variables dentro de funciones (new_book en addBook, bookFound en issueBook).
•	Bloques internos: dentro de estructuras de control (for (int i = 0; i < issued_count; i++) → la variable i sólo existe en ese bloque).

4. Administración de memoria
El programa muestra distintos tipos de almacenamiento:
•	Estático: static int static_var = 0; (segmento de datos).
•	BSS: int bss_var; (global no inicializada).
•	Stack (automáticas): book_t *library = NULL; en main.
•	Heap (dinámica):
o	malloc(sizeof(book_t)) en addBook.
o	realloc en issueBook y returnBook.
o	free en freeLibrary y freeMembers.

Además, se lleva control con funciones de apoyo (incrementHeapAllocations, incrementHeapDeallocations, displayMemoryUsage).

5. Expresiones
Operaciones que devuelven valores:
•	Aritméticas: bookFound->quantity--, memberFound->issued_count++.
•	Comparaciones: if (current->id == bookID).
•	Conversiones: (genre_t)genre.

6. Comandos (Statements)
Son las instrucciones que se ejecutan:
•	Asignaciones: new_book->id = ...;
•	Llamadas a funciones: displayMemoryUsage();
•	Sentencias de control: if, while, for, switch.

7. Control de secuencia
•	Selección:
o	if (bookFound && memberFound) {...} else {...}.
o	switch (choice) en el menú principal.
•	Iteración:
o	while (current_book) {...} para recorrer la lista enlazada.
o	for (int i = 0; i < issued_count; i++) {...}.
•	Recursión:
o	displayBooksRecursive que se llama a sí misma hasta recorrer toda la lista.

8. Subprogramas
Todas las funciones definidas en el código son subprogramas:
•	Procedimientos: addBook, addMember, issueBook (no devuelven un valor).
•	Funciones: genreToString, findBookById (sí devuelven valor).

9. Tipos de datos
•	Primitivos: int, char, float (implícito en scanf/printf).
•	Compuestos:
o	struct book_t, struct member_t.
o	Listas enlazadas (a través del puntero *next).
•	Enumeraciones: enum genre_t para representar géneros de libros.
•	Punteros: book_t *library, member_t *members, int *issued_books.
