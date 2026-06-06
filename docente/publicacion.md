# Checklist de publicación del repositorio

Usa esta lista antes de publicar el vault como repositorio público.

## Destino de publicación

Cuenta GitHub prevista: `ingfcetina` asociada a `ingfcetina@gmail.com`.

Nombre recomendado:

```text
ia-practica-para-salud-ocupacional
```

Otras opciones:

- `programar-con-ia-para-salud`
- `vault-ia-salud-ocupacional`
- `salud-ocupacional-ia-python`

## Link público para compartir

Repositorio principal:

```text
https://github.com/ingfcetina/ia-practica-para-salud-ocupacional
```

Ruta recomendada para estudiantes:

```text
https://github.com/ingfcetina/ia-practica-para-salud-ocupacional/blob/main/00-empezar-aqui/ruta-de-aprendizaje.md
```

Mensaje corto para docentes:

```text
Para empezar, entra al repositorio y abre la ruta de aprendizaje:
https://github.com/ingfcetina/ia-practica-para-salud-ocupacional/blob/main/00-empezar-aqui/ruta-de-aprendizaje.md

Sigue las notas en orden. Primero revisa privacidad y uso seguro de datos; luego instalación, conceptos, prácticas guiadas y Python desde cero. No uses datos reales identificables.
```

## Antes de publicar

- [ ] Revisar [[README|README]].
- [ ] Abrir [[00-empezar-aqui/mapa-del-vault|Mapa del vault]] en Obsidian.
- [ ] Confirmar que los datos en `assets/datos/` son sintéticos.
- [ ] Confirmar que no hay nombres reales de pacientes, trabajadores, empresas o instituciones.
- [ ] Probar `assets/checklist_interactivo.html` en un navegador.
- [ ] Ejecutar `python scripts/00_validar_datos.py`.
- [ ] Ejecutar o revisar los scripts de [[scripts/README|Scripts de ejemplo]].
- [ ] Confirmar que `assets/imagenes/` y `outputs/` contienen resultados de ejemplo actualizados.
- [ ] Elegir licencia.
- [ ] Inicializar git si todavía no existe.

## Licencia

Licencia elegida: **CC BY 4.0**.

Esto permite reutilizar, adaptar y compartir el material, incluso comercialmente, siempre que se dé atribución adecuada.

Archivo de licencia: [[LICENSE|Creative Commons Attribution 4.0 International]].

## Comandos sugeridos

```bash
git init
git add .
git commit -m "Create AI health workshop Obsidian vault"
```

Luego crea el repositorio público en GitHub y conecta el remoto:

```bash
git remote add origin https://github.com/<usuario>/ia-practica-para-salud-ocupacional.git
git branch -M main
git push -u origin main
```

## Revisión final

- [ ] El taller puede seguirse desde el mapa principal.
- [ ] Las notas usan links internos de Obsidian.
- [ ] Los ejemplos son simples y ejecutables.
- [ ] Las advertencias de privacidad aparecen antes de las prácticas guiadas.
- [ ] El repositorio no contiene estado local de herramientas.

## Relacionado

- [[00-empezar-aqui/como-usar-este-vault|Cómo usar este vault]]
- [[docente/guia-facilitador|Guía para facilitar el taller]]
