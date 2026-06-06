# MOC Python desde cero

tags: #moc #python #principiantes

Esta sección es para aprender Python con calma, desde ejemplos pequeños y visibles. No está pensada para memorizar sintaxis, sino para entender qué hace el código y cómo usarlo con datos sintéticos de salud ocupacional.

Si vienes de las prácticas guiadas, esta sección funciona como una explicación más lenta de lo que ocurre “por debajo”.

## Cómo usar esta sección

Sigue este orden:

```text
1. Abrir el archivo o resultado sin programar
2. Ejecutar el script ya preparado
3. Observar qué aparece en pantalla o qué archivo se genera
4. Leer el código explicado línea por línea
5. Pedir a la IA una explicación adicional
6. Cambiar una sola cosa pequeña
7. Validar que todo sigue funcionando
```

No avances si no sabes qué archivo estás usando o qué resultado esperas ver.

## Orden recomendado

1. [[03-python-desde-cero/leer-datos-csv|Leer datos CSV]]
   - Aprendes qué es un CSV, dónde está y cómo Python lo lee.

2. [[03-python-desde-cero/limpiar-datos|Limpiar datos]]
   - Aprendes a revisar valores vacíos y textos con espacios sobrantes.

3. [[03-python-desde-cero/graficar-resultados|Graficar resultados]]
   - Aprendes a contar categorías y guardar un gráfico.

4. [[03-python-desde-cero/generar-informes|Generar informes]]
   - Aprendes a convertir indicadores agregados en un informe base prudente.

## Tiempo sugerido

| Nota | Tiempo aproximado |
|---|---:|
| Leer datos CSV | 20-30 min |
| Limpiar datos | 20-30 min |
| Graficar resultados | 25-35 min |
| Generar informes | 25-35 min |

Puedes hacer una nota por sesión. No es necesario hacer todo en un solo día.

## Antes de empezar

Revisa primero:

- [[00-empezar-aqui/instalacion-y-preparacion|Instalación y preparación]]
- [[00-empezar-aqui/reglas-de-privacidad|Reglas de privacidad]]
- [[06-recursos/datasets-ejemplo|Datasets de ejemplo]]

## Comandos base

Cuando una nota diga “ejecuta el script”, usa el comando según tu sistema.

### Windows

```bash
python scripts/nombre_del_script.py
```

Si `python` no funciona:

```bash
py scripts/nombre_del_script.py
```

### macOS

```bash
python3 scripts/nombre_del_script.py
```

## Si no puedes ejecutar código todavía

Puedes seguir aprendiendo:

- abre los CSV en Excel, Numbers o Google Sheets;
- mira las imágenes ya generadas en `assets/imagenes/`;
- abre `outputs/informe_base.md`;
- lee el código y pide a la IA que lo explique línea por línea;
- vuelve a ejecutar cuando tengas Python listo.

## Regla de seguridad

En todos los ejercicios:

- usa datos sintéticos;
- no pegues datos reales identificables en IA;
- no concluyas causas solo por ver un número o gráfico;
- no conviertas resultados en decisiones sobre personas.

## Recursos relacionados

- [[06-recursos/datos-abiertos-colombia|Datos abiertos de Colombia]]
- [[scripts/README|Scripts de ejemplo]]
- [[assets/notebooks/README|Notebooks de ejemplo]]
- [[02-practicas-guiadas/practica-01-analizar-ausentismo|Práctica 1: analizar ausentismo]]
