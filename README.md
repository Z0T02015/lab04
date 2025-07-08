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


## Punto 1: Recorrido de Grafos con DFS

Se implementó el recorrido en profundidad (Depth First Search) sobre un grafo no dirigido con 8 vértices.

Archivo: `dfs_traversal.py`

Evidencia de salida (consola):

Traversal: a  
Traversal: b  
Traversal: h  
Traversal: e  
Traversal: g  
Traversal: f  
Traversal: c  
Traversal: d

## Punto 2: Recorrido de Grafos con BFS

Se implementó el recorrido en anchura (Breadth First Search) usando una estructura de cola.

Archivo: `bfs_traversal.py`

Evidencia:
- Orden de recorrido: a → b → h → c → e → d → g → f
- Se imprimieron las distancias desde el nodo `a` hacia todos los vértices.

## Punto 3: Ruta más corta sin peso

Se implementó un algoritmo de recorrido BFS para hallar la distancia mínima desde el nodo `'a'` a todos los demás nodos en un grafo **no ponderado**.

Archivo: `shortest_path_unweighted.py`

### Salida esperada: 

Se utilizó el mismo grafo que en los puntos anteriores.