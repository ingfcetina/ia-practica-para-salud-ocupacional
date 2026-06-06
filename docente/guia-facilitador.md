# Guía para facilitar el taller

Esta guía ayuda a dictar el taller de una hora sin convertirlo en una clase de instalación o sintaxis.

## Objetivo docente

Al finalizar, estudiantes y profesionales deberían poder:

- explicar un problema profesional en lenguaje claro;
- pedir ayuda a una IA sin entregar datos sensibles;
- revisar críticamente una respuesta generada;
- entender un ejemplo mínimo de Python aplicado a datos sintéticos;
- mostrar una página web interactiva sencilla como prototipo didáctico.

## Preparación antes de la clase

### Herramientas

Ten listo al menos un equipo de demostración con:

- navegador web;
- acceso a ChatGPT web, Claude o una herramienta equivalente;
- editor de texto o entorno de código;
- Python instalado;
- dependencias instaladas:

```bash
pip install pandas matplotlib
```

Si Python falla durante la sesión, no detengas el taller: muestra el código, la salida esperada y vuelve al método.

### Materiales del vault

Empieza desde [[00-empezar-aqui/mapa-del-vault|Mapa del vault]].

Archivos clave:

- [[docente/guion-taller-una-hora|Guion del taller de una hora]]
- [[01-conceptos-clave/limites-riesgos-etica|Límites, riesgos, ética y privacidad]]
- [[02-practicas-guiadas/practica-01-analizar-ausentismo|Práctica 1: analizar ausentismo]]
- [[04-herramientas-ia/chatgpt-web|ChatGPT web]]
- [[04-herramientas-ia/claude|Claude]]
- [[04-herramientas-ia/codex|Codex]]
- [[05-mini-proyectos/pagina-web-presentacion|Página web interactiva para una presentación]]

## Método recomendado

Usa esta secuencia en cada ejemplo:

```text
Problema profesional → datos seguros → prompt claro → prototipo → revisión humana → mejora
```

## Manejo de preguntas difíciles

| Pregunta | Respuesta sugerida |
|---|---|
| ¿Esto reemplaza a una persona profesional? | No. La IA ayuda a explorar, resumir, prototipar y automatizar. La responsabilidad profesional sigue siendo humana. |
| ¿Puedo pegar historias clínicas? | No en herramientas públicas. Usa datos sintéticos, agregados o anonimizados, y respeta políticas institucionales. |
| ¿El código de la IA siempre funciona? | No. Debe probarse, revisarse y simplificarse. |
| ¿Necesito saber programar antes? | No para empezar. Sí necesitas aprender a describir el problema, revisar resultados y avanzar paso a paso. |

## Cierre sugerido

Termina con esta idea:

> La habilidad central no es memorizar código. Es aprender a formular problemas, proteger datos, pedir ayuda con precisión y validar resultados con criterio profesional.

## Relacionado

- [[00-empezar-aqui/mapa-del-vault|Mapa del vault]]
- [[06-recursos/prompts|Banco de prompts]]
