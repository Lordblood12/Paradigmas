REPORTE: Markdown, Git, GitHub, Hugo y GitHub Actions
1. **¿Qué es Markdown?**

Markdown es un lenguaje de marcado ligero que permite crear texto con formato utilizando una sintaxis sencilla y fácil de leer. Fue creado para facilitar la escritura de documentos que puedan convertirse fácilmente a HTML.

Su objetivo es permitir escribir contenido formateado sin necesidad de usar editores complejos.

**1.1 ¿Cómo se utiliza Markdown?**

Markdown se utiliza principalmente en:

Documentación técnica

Readme de repositorios en GitHub

Blogs estáticos (como los generados con Hugo)

Notas personales y organizacionales

Para escribir en Markdown solo necesitas un editor de texto (VS Code, Notepad++, etc.).

**1.2 Sintaxis básica de Markdown**

| Elemento           | Sintaxis                   |
| ------------------ | -------------------------- |
| Título 1           | `# Título`                 |
| Título 2           | `## Subtítulo`             |
| Negritas           | `**texto**`                |
| Cursiva            | `*texto*`                  |
| Listas con viñetas | `- elemento`               |
| Listas numeradas   | `1. elemento`              |
| Código en línea    | `` `código` ``             |
| Bloques de código  | ` `código` `               |
| Enlaces            | `[texto](https://url.com)` |
| Imágenes           | `![alt](imagen.png)`       |
| Citas              | `> texto citado`           |

Ejemplo:

# Mi Proyecto
Este es un **documento** en Markdown para describir mi proyecto.

## Características
- Fácil de usar
- Ligero
- Compatible con GitHub

**2. Git y GitHub**
**2.1 ¿Qué es Git?**

Git es un sistema de control de versiones que permite:

Registrar cambios en un proyecto

Volver a versiones anteriores

Trabajar en equipo sin sobrescribir archivos

Llevar control detallado de todo el código

Git funciona en tu computadora sin necesidad de internet.

**2.2 ¿Cómo se utiliza Git?**

Git se maneja principalmente mediante comandos en la terminal.

Flujo básico:

Crear o clonar un repositorio

Agregar archivos al control de versiones

Guardar cambios (commit)

Subirlos a un servidor como GitHub

**2.3 Comandos esenciales de Git**

Configuración inicial

git config --global user.name "Tu Nombre"
git config --global user.email "tuemail@correo.com"

Iniciar un repositorio

git init

Ver el estado de archivos

git status

Agregar archivos al área de preparación

git add .

Guardar cambios

git commit -m "Mensaje del commit"

Ver historial

git log

Conectar con un repositorio remoto

git remote add origin https://github.com/usuario/repositorio.git

Subir cambios a GitHub

git push -u origin main

**3. ¿Qué es GitHub?**

GitHub es una plataforma en la nube donde puedes almacenar repositorios Git. Funciona como:

Almacenamiento remoto

Herramienta de colaboración

Portafolio público de proyectos

Plataforma de despliegue de sitios estáticos

**3.1 ¿Cómo crear un repositorio en GitHub?**

Entra a GitHub → New Repository

Asigna un nombre

Elige público o privado

Crear repositorio

GitHub te mostrará las instrucciones para conectarlo con tu proyecto local.

3.2 Subir tu proyecto a GitHub

Inicia Git en tu carpeta:
git init

Conecta al repositorio en GitHub:
git remote add origin URL

Sube tus archivos:
git add .
git commit -m "Primer commit"
git push -u origin main

**4. ¿Qué es Hugo?**

Hugo es un generador de sitios estáticos extremadamente rápido. Permite crear:

Portafolios

Blogs

Documentaciones

Páginas institucionales

Usa plantillas en HTML y contenido en Markdown.

**4.1 ¿Cómo crear un sitio estático con Hugo?**
1. Instalar Hugo

En Windows:
choco install hugo-extended

2. Crear un nuevo sitio
hugo new site mi-sitio

3. Agregar un tema
git submodule add https://github.com/tema/hugo-tema.git themes/tema

Editar config.toml:
theme = "tema"

4. Crear contenido
hugo new posts/primer-post.md

5. Servir el sitio localmente
hugo server -D

6. Generar los archivos finales
hugo

5. Subir el sitio de Hugo a GitHub

Crea un repositorio Git en la carpeta del proyecto Hugo.

Sube todos los archivos (excepto public/ si usarás GitHub Actions).

Haz push a GitHub.

git add .
git commit -m "Sitio Hugo"
git push -u origin main

6. ¿Qué es GitHub Actions?

GitHub Actions es un sistema de automatización integrado en GitHub que permite:

Compilar proyectos

Ejecutar pruebas

Desplegar sitios automáticamente

Se configura mediante archivos YAML dentro de:
.github/workflows/

6.1 Configurar GitHub Actions para publicar un sitio Hugo en GitHub Pages

Crear archivo:
.github/workflows/hugo-deploy.yml

Añadir configuración básica:
name: Deploy Hugo site to GitHub Pages

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v2
        with:
          hugo-version: 'latest'
          extended: true

      - name: Build
        run: hugo --minify

      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        with:
          personal_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./public

Activar GitHub Pages en la configuración del repositorio:

Settings → Pages

Source → "Deploy from a branch"

Seleccionar la rama gh-pages

Tu sitio quedará disponible en:
https://usuario.github.io/repositorio

**Conclusión**

Este reporte presenta una visión completa sobre herramientas esenciales para el desarrollo moderno:

Markdown para documentación sencilla

Git para control de versiones

GitHub como almacenamiento y colaboración

Hugo para generar sitios estáticos

GitHub Actions para automatizar despliegues

Con este flujo, cualquier persona puede documentar, versionar, crear y publicar un sitio completo en la web de forma profesional.

Pagina estatica: https://lordblood12.github.io/Paradigmas/
