# Clase 8: Skills, Agentes, Loops, Harness

## Resumen

En la Clase 7 vimos los fundamentos del prompting. Hoy transformamos prompts sueltos en **componentes reutilizables versionados como código** (Skills), introducimos el **ciclo del agente** (Think→Act→Observe) y conocemos el **harness** que protege al agente en producción.

## Objetivos de Aprendizaje

1. **Comprender** por qué y cómo reutilizar prompts como Skills versionados.
2. **Estructurar** un Skill con YAML metadata + prompt template + examples.
3. **Implementar** control de versiones para prompts usando Git.
4. **Introducir** el loop del agente (Think→Act→Observe).
5. **Conocer** el harness básico: límites, retry, logging.

## Agenda (70 min + 20 min)

| Fase | Tiempo | Contenido |
|------|--------|-----------|
| Introducción | 5 min | El problema del prompt suelto |
| Anatomía de un Skill | 10 min | YAML + prompt + examples |
| Control de versiones | 10 min | Git para prompts |
| El Loop del Agente | 15 min | Think → Act → Observe |
| Harness básico | 10 min | Límites, retry, logging |
| Práctica | 20 min | Crear 3 skills y versionarlos |

## Contenido

- [apuntes.md](apuntes.md) — Teoría completa
- [glosario.md](glosario.md) — Términos en lenguaje simple
- [practica.md](practica.md) — Ejercicio práctico
- [recursos.md](recursos.md) — Material complementario

## Próxima Clase

**Clase 9: Function Calling / Tool Use.** Conectaremos un LLM a herramientas externas mediante function calling.
