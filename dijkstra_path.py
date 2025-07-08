from graph.impl_adj_list import Vertex, Graph
import heapq
from itertools import count

# Dijkstra's shortest path
def dijkstra(G, source, destination):
    source.setDistance(0)

    counter = count()
    unvisitedQueue = [(v.getDistance(), next(counter), v) for v in G]
    heapq.heapify(unvisitedQueue)

    while unvisitedQueue:
        _, __, current = heapq.heappop(unvisitedQueue)
        current.setVisited()

        for neighbor in current.adjList:
            if neighbor.visited:
                continue
            newDist = current.getDistance() + current.getWeight(neighbor)

            if newDist < neighbor.getDistance():
                neighbor.setDistance(newDist)
                neighbor.setPrevious(current)
                print(f"Updated: {current.getId()} → {neighbor.getId()} = {newDist}")
            else:
                print(f"Not updated: {current.getId()} → {neighbor.getId()} = {neighbor.getDistance()}")

        # Vaciar y reconstruir la cola
        while unvisitedQueue:
            heapq.heappop(unvisitedQueue)
        unvisitedQueue = [(v.getDistance(), next(counter), v) for v in G if not v.visited]
        heapq.heapify(unvisitedQueue)

# Función para mostrar el camino más corto
def shortest(v, path):
    if v.previous:
        path.append(v.previous.getId())
        shortest(v.previous, path)
    return

# MAIN
if __name__ == '__main__':
    g = Graph()
    g.addVertex('a')
    g.addVertex('b')
    g.addVertex('c')
    g.addVertex('d')
    g.addVertex('e')

    g.addEdge('a', 'b', 4)
    g.addEdge('a', 'c', 1)
    g.addEdge('c', 'b', 2)
    g.addEdge('b', 'e', 4)
    g.addEdge('c', 'd', 4)
    g.addEdge('d', 'e', 4)

    source = g.getVertex('a')
    destination = g.getVertex('e')

    print("Distancias actualizadas con Dijkstra:")
    dijkstra(g, source, destination)

    print("\nDistancias desde 'a':")
    for v in g:
        print(f"{source.getId()} to {v.getId()} --> {v.getDistance()}")

    path = [destination.getId()]
    shortest(destination, path)
    print("\nEl camino más corto de 'a' a 'e' es:", ' → '.join(path[::-1]))