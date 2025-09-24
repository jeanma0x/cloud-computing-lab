# Laboratorio práctico: GitHub - Repositorios, Ramas, Pull Requests y GitHub Actions

## 🎯 Objetivo del lab

En este laboratorio configuraremos un repositorio en GitHub, trabajaremos con ramas, haremos un Pull Request y configuraremos una acción automática con GitHub Actions.

## Fases del Laboratorio

### Fase 1: Creamos un repositorio en GitHub ✅

**Pasos que seguiremos:**

1. Ingresamos a [https://github.com](https://github.com)
2. Hacemos clic en **"New Repository"**
3. **Nombre que usaremos:** `cloud-computing-lab`
4. **Opciones que seleccionaremos:**
   - ✅ Inicializamos con `README.md`
   - ✅ Seleccionamos una licencia (por practicidad, no la usamos en este lab)

### Fase 2: Clonamos el repositorio en local 

**Comandos que ejecutamos:**

```bash
git clone https://github.com/jeanma0x/cloud-computing-lab.git
cd mi-primer-repo
```

**Editaremos el README.md y añadiremos:**

```markdown
# Mi primer repositorio
Este es un repositorio de prueba para el curso de Cloud Computing.
```

**Subiremos los cambios:**

```bash
git add README.md
git commit -m "Actualización inicial del README"
git push origin main
```

### Fase 3: Creamos y trabajamos en una rama 🌿

**Crearemos una nueva rama y agregaremos funcionalidad:**

```bash
git checkout -b new-feature
echo "print('Hola desde mi rama!')" > app.py
git add app.py
git commit -m "Agrego app.py con mensaje"
git push origin nueva-funcionalidad
```

### Fase 4: Creamos un Pull Request (PR) 🔀

**Pasos que seguiremos en GitHub:**

1. Iremos a **GitHub → Nuestro Repositorio → pestaña "Pull requests"**
2. Haremos clic en **"New pull request"**
3. Seleccionaremos:
   - **Base:** `main`
   - **Compare:** `new-feature`
4. **Crearemos el PR** (opcional: pediremos revisión)
5. **Fusionaremos el PR** (merge)

### Fase 5: Configuramos GitHub Actions (CI básico) ⚙️

**Crearemos la estructura de directorios:**

```
cloud-computing-lab/
├── .github/
│   └── workflows/
│       └── ci.yml
├── app.py
├── README.md
```

**Contenido que agregaremos al archivo `.github/workflows/ci.yml`:**

```yaml
name: CI básico

on:
  push:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout repo
        uses: actions/checkout@v3
        
      - name: Configurar Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.x"
          
      - name: Ejecutar script
        run: python app.py
```

**Subiremos los cambios:**

```bash
git add .github/workflows/ci.yml
git commit -m "Agregar workflow de GitHub Actions"
git push origin main
```

## Resultado que obtendremos

Al completar este laboratorio tendremos:

- ✅ **Repositorio creado** en GitHub
- ✅ **Cambios subidos** desde local al repositorio
- ✅ **Rama creada** y **Pull Request fusionado**
- ✅ **Workflow de GitHub Actions** ejecutado automáticamente
- ✅ **Logs visibles** en la pestaña Actions de GitHub

## Estructura final del proyecto

```
cloud-computing-lab/
├── .github/
│   └── workflows/
│       └── ci.yml
├── app.py
├── README.md
```

## Verificamos el trabajo que hicimos

### Repositorio GitHub
- [ ] Hemos creado el repositorio `cloud-computing-lab`
- [ ] Hemos actualizado README.md con descripción
- [ ] Hemos seleccionado la licencia MIT

### Trabajo con ramas
- [ ] Hemos creado la rama `new-feature`
- [ ] Hemos agregado el archivo `app.py` con el código Python
- [ ] Hemos realizado commits correctamente

### Pull Request
- [ ] Hemos creado PR desde `new-feature` hacia `main`
- [ ] Hemos fusionado el PR exitosamente
- [ ] Hemos integrado la rama en `main`

### GitHub Actions
- [ ] Hemos creado el archivo `ci.yml` en `.github/workflows/`
- [ ] El workflow se ha ejecutado automáticamente
- [ ] Vemos el status ✅ verde en la pestaña Actions
- [ ] Vemos el output `"Hola desde mi rama!"` en los logs

## Comandos que estuvimos utilizando

```bash
# Veremos estado del repositorio
git status

# Veremos historial de commits
git log --oneline

# Veremos ramas disponibles
git branch -a

# Cambiaremos entre ramas
git checkout nombre-rama

# Veremos diferencias antes de commit
git diff
```

## Conceptos que aprendimos

- **Repository**: Espacio de almacenamiento para nuestro proyecto
- **Branch**: Línea de desarrollo independiente que creamos
- **Pull Request**: Propuesta para fusionar cambios que hacemos
- **GitHub Actions**: Automatización de workflows que configuramos
- **CI (Continuous Integration)**: Integración continua de código que implementamos


---

**Curso:** Cloud Computing  
**Laboratorio:** GitHub y GitHub Actions  # Última modificación: Tue Sep 23 18:11:27 CST 2025
