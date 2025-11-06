Objetivo

El objetivo que se quizo lograr en esta Practica 3, fue Instalar el entorno de desarrollo de Haskell mediante GHCup y comprender el funcionamiento de una aplicación web tipo “To-Do List” desarrollada con el lenguaje Haskell y el framework Scotty para tener la nocion de como funciona y para que sirve.

Introducción

Haskell es un lenguaje funcional puro que se caracteriza por su enfoque matemático en el desarrollo de software. En esta práctica se instala su entorno de desarrollo mediante GHCup y se ejecuta una aplicación de ejemplo basada en el framework Scotty, con el objetivo de familiarizarse con su sintaxis y el paradigma funcional.

Desarrollo

1. Instalación del entorno:
Se utilizó la herramienta GHCup desde PowerShell, la cual instaló los componentes principales:

GHC (compilador de Haskell)

Stack (gestor de proyectos)

Cabal (herramienta de compilación)

HLS (Haskell Language Server)

Se verificó la instalación mediante:

ghc --version
stack --version

2. Clonación del proyecto:
Se descargó el repositorio oficial con:

git clone https://github.com/steadylearner/Haskell.git

Y se accedió a:

cd Haskell/examples/blog/todo

3. Compilación y ejecución:
Con los siguientes comandos se compiló y ejecutó el proyecto:

stack build
stack run

4. Funcionamiento:
La aplicación levanta un servidor web en el puerto 3000.
Permite agregar, visualizar y eliminar tareas a través de una interfaz HTML básica.
Está desarrollada usando el framework Scotty, que implementa rutas del tipo:

get "/", post "/add", delete "/delete/:id"

Cada ruta ejecuta funciones que manipulan listas de tareas en memoria.

Resultados

Al realizar todos los pasos para la instalacion y ejecucion de Haskell, la aplicación se ejecutó correctamente en el entorno local, mostrando la página principal en http://localhost:3000 y permitiendo agregar nuevas tareas, con esto comprendí la estructura modular del proyecto y la naturaleza declarativa del lenguaje Haskell.

Conclusión

Haskell, aunque posee una sintaxis diferente a lenguajes imperativos, ofrece un paradigma potente y conciso para el desarrollo funcional. La aplicación TODO sirvió como introducción práctica para comprender conceptos como funciones puras, monadas IO y el uso de Stack para la gestión de proyectos.