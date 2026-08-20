# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

This is a small collection of standalone learning exercises ("Ejercicios"), not a single application. There is no build system, package manager, or test suite — each exercise is a self-contained file (or small set of files) meant to be run/opened directly.

## Structure

- `Python/ejercicio1.py` — a command-line calculator. Prompts for an operation (1-7: suma, resta, multiplicación, división, división entera, módulo, potencia) and two numbers, then prints the result. Guards division/modulo by zero.
- `html/index.html` + `html/styles.css` — a browser version of the same calculator. The calculation logic (`calcular()`) lives inline in a `<script>` tag at the bottom of `index.html`, mirroring the Python `if/elif` branches. The "Suma" option is special-cased in the UI to allow summing an arbitrary list of numbers (dynamically added rows) rather than just two.

## Running the exercises

- Python exercise: `python Python\ejercicio1.py` (interactive prompts on stdin).
- HTML exercise: open `html/index.html` directly in a browser (no server or build step needed).

## Conventions to preserve when editing

- Code and UI text are in Spanish; keep new exercises/strings consistent with that.
- The HTML version's `calcular()` switch statement is meant to stay logically parallel to the Python `if/elif` chain (same operation numbering: 1=suma, 2=resta, 3=multiplicación, 4=división, 5=división entera, 6=módulo, 7=potencia). When changing behavior in one, check whether the other needs the same change.
- Division/modulo-by-zero must be guarded in both versions before returning/printing a result.
