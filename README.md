# Ejercicios de Python — Aprendiz SENA

Repositorio personal para aprender Python paso a paso, tema por tema.

## Estructura

```
Ejercicios/
├── python/
│   ├── 00_practica_git/               Archivos usados para practicar Git (commits, conflictos)
│   ├── 01_fundamentos/                print, input, variables, tipos de datos, operadores
│   ├── 02_strings/                    Cadenas, índices, slicing, f-strings
│   ├── 03_condicionales/              if / elif / else
│   ├── 04_ciclos/                     while, for, range, break, continue
│   ├── 05_listas_tuplas_diccionarios/ Colecciones de datos
│   ├── 06_funciones/                  def, parámetros, return
│   ├── 07_archivos_y_excepciones/     open(), try / except
│   ├── 08_poo/                        Clases y objetos
│   └── proyectos/                     Programas completos que juntan varios temas
│       └── calculadora/
└── html/                              Versión web de la calculadora
```

Cada carpeta tiene su propio `README.md` con lo que se aprende ahí y ejercicios sugeridos.

## Cómo ejecutar un ejercicio

Desde la terminal de VS Code, en la raíz del repositorio:

```bash
python python/02_strings/03_f_strings.py
```

## Reglas para nombrar archivos

- Todo en minúsculas, palabras separadas con `_` (guion bajo): `par_impar.py`.
- Sin espacios, tildes ni guiones (`-`): Python no puede importar `f-string.py`.
- No usar nombres de módulos de Python (`string.py`, `random.py`, `math.py`), porque "tapan" al módulo real.
- Numerar los ejercicios para que queden en orden: `01_...`, `02_...`.

## Progreso

- [x] 01 Fundamentos
- [x] 02 Strings
- [ ] 03 Condicionales
- [ ] 04 Ciclos
- [ ] 05 Listas, tuplas y diccionarios
- [ ] 06 Funciones
- [ ] 07 Archivos y excepciones
- [ ] 08 Programación orientada a objetos
- [x] Proyecto: calculadora
