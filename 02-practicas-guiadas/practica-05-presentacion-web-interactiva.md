# Práctica 5: presentación web interactiva

tags: #practica #web #presentacion #principiantes

En esta práctica vas a abrir una página web simple incluida en el vault y entender cómo puede usarse como material de capacitación.

No necesitas saber programar para el primer paso. Solo vas a abrir un archivo HTML con doble clic.

## Objetivo de aprendizaje

Al terminar podrás:

- encontrar un archivo HTML dentro del repositorio;
- abrirlo en el navegador;
- probar una interacción básica;
- identificar qué partes del archivo se pueden reemplazar;
- pedir a la IA una adaptación segura y simple.

## Qué es un archivo HTML

Un archivo HTML es una página web. Normalmente se abre con un navegador como Chrome, Edge, Firefox o Safari.

En este vault tienes este archivo:

```text
assets/checklist_interactivo.html
```

## Paso 1: encontrar el archivo

1. Abre la carpeta del repositorio.
2. Entra a la carpeta `assets`.
3. Busca el archivo:

```text
checklist_interactivo.html
```

4. Haz doble clic sobre el archivo.
5. Debe abrirse en tu navegador.

Si no se abre:

- haz clic derecho;
- elige **Abrir con**;
- selecciona Chrome, Edge, Firefox o Safari.

## Paso 2: probar la página

Cuando se abra la página:

1. Lee el título.
2. Lee la advertencia de privacidad.
3. Responde algunas preguntas del checklist.
4. Presiona el botón **Calcular cumplimiento**.
5. Observa el porcentaje y la recomendación.

Pregunta para pensar:

```text
¿Esta herramienta recolecta datos personales?
```

Respuesta esperada: no. Es un ejemplo local y didáctico.

## Paso 3: entender qué partes tiene

La página combina tres partes:

| Parte | Qué hace |
|---|---|
| HTML | Organiza título, texto, preguntas y botón. |
| CSS | Define colores, tamaño, espaciado y apariencia. |
| JavaScript | Calcula el porcentaje y muestra la recomendación. |

No tienes que dominar todo. Solo identifica que cada parte cumple una función.

## Paso 4: abrir el archivo para editarlo

Para modificarlo:

1. Haz clic derecho sobre `assets/checklist_interactivo.html`.
2. Elige **Abrir con**.
3. Usa un editor de texto.
   - En Windows puede ser Bloc de notas, VS Code o Cursor.
   - En macOS puede ser TextEdit, VS Code o Cursor.
4. Si usas TextEdit en macOS, asegúrate de editar como texto plano.

Recomendación: antes de modificar, haz una copia:

```text
checklist_interactivo_copia.html
```

## Paso 5: qué puedes cambiar sin romper todo

Busca esta parte dentro del archivo:

```javascript
const preguntas = [
  "El área de trabajo está libre de obstáculos visibles",
  "Los elementos de protección personal requeridos están disponibles",
  "Las rutas de evacuación están señalizadas y despejadas",
  "Los residuos se encuentran separados según el protocolo",
  "El personal conoce a quién reportar un incidente o condición insegura",
];
```

Puedes cambiar solo las frases entre comillas.

Ejemplo:

```javascript
const preguntas = [
  "La silla permite apoyar la espalda",
  "La pantalla está a una altura cómoda",
  "Hay pausas activas durante la jornada",
  "El espacio de trabajo está ordenado",
  "La iluminación es suficiente para la tarea",
];
```

Importante:

- no borres los corchetes `[` y `]`;
- no borres las comillas;
- deja una coma después de cada frase excepto si la IA te indica otra cosa;
- cambia una cosa a la vez y prueba.

## Paso 6: pedirle a la IA que lo adapte

Prompt recomendado:

```text
Quiero adaptar una página HTML de checklist para una capacitación de ergonomía.
No sé programar.
Te voy a pegar el archivo completo.
Cambia solo las preguntas y los textos visibles.
Mantén un solo archivo HTML.
No agregues librerías externas.
No recolectes datos personales.
Explica exactamente qué cambiaste.
```

Prompt para pedir explicación:

```text
Explícame este archivo HTML como si yo nunca hubiera programado.
Divide la explicación en HTML, CSS y JavaScript.
Dime qué partes puedo cambiar con bajo riesgo.
```

## Paso 7: validar antes de usar en clase

Marca esta lista:

- [ ] El archivo abre con doble clic.
- [ ] El botón calcula el porcentaje.
- [ ] Las preguntas son claras.
- [ ] No hay nombres ni datos reales.
- [ ] La recomendación no culpa ni sanciona.
- [ ] La actividad se puede explicar en menos de 5 minutos.

## Si algo se rompe

| Problema | Qué hacer |
|---|---|
| La página se ve en blanco | Vuelve a la copia original o pide a la IA revisar el archivo completo. |
| El botón no funciona | Revisa si borraste comillas, comas o corchetes en `const preguntas`. |
| Aparecen símbolos raros | Guarda el archivo como UTF-8 si el editor lo permite. |
| No sabes qué cambiaste | Compara con la copia original. |

## Producto final

Al terminar deberías tener:

- una página HTML abierta en navegador;
- preguntas adaptadas a un tema;
- una actividad breve para capacitación;
- una advertencia clara de privacidad.

## Relacionado

- [[05-mini-proyectos/pagina-web-presentacion|Página web interactiva para una presentación]]
- [[05-mini-proyectos/checklist-inteligente|Checklist inteligente]]
- [[04-herramientas-ia/claude-code-y-codex|Usar este vault con Claude Code y Codex]]
