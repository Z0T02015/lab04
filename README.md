## Paso 6: Creación y fusión de rama

Se creó una rama nueva llamada `mejora-grafo` con el comando:

    git checkout -b mejora-grafo

En dicha rama, se agregó una línea de impresión en el archivo `grafo_lista.py` para evidenciar una modificación:

    print("¡Hola desde la rama mejora-grafo!")

Luego se hizo commit de los cambios y se fusionó con la rama `main` usando:

    git checkout main
    git merge mejora-grafo

La fusión fue exitosa sin conflictos.

## Paso 7: Simulación de conflicto

Se simuló un conflicto de Git trabajando con dos ramas distintas:

1. En `rama-conflicto-a`, se modificó la línea `print(...)` en el archivo `grafo_lista.py`.
2. En `rama-conflicto-b`, se modificó esa misma línea pero con un texto diferente.
3. Al intentar fusionar `rama-conflicto-a` sobre `rama-conflicto-b`, Git detectó un conflicto.
4. Se resolvió el conflicto editando manualmente el archivo, dejando la versión final:

    print("Conflicto resuelto: ganamos todos")

5. Luego se finalizó la fusión con `git add` y un nuevo commit.

Este paso demuestra cómo resolver conflictos de fusión colaborando (o simulándolo en solitario).