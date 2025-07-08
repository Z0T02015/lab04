from graph.impl_adj_list import Vertex, Graph
from basic.impl_queue import Queue

def BFSTraversal(g, s):
    start = g.getVertex(s)
    start.setDistance(0)
    start.setPrevious(None)
    vertQueue = Queue()
    vertQueue.enQueue(start)
    while vertQueue.size() > 0:
        currentVert = vertQueue.deQueue()
        print("Visited:", currentVert.getId())
        for nbr in currentVert.getAdjLists():
            if nbr.visited == False:
                nbr.visited = True
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPrevious(currentVert)
                vertQueue.enQueue(nbr)
        currentVert.visited = True
def BFS(g):
    for v in g:
        if v.visited == False:
            BFSTraversal(g, v.getId())

if __name__ == '__main__':
    g = Graph()
    g.addVertex('a')
    g.addVertex('b')
    g.addVertex('c')
    g.addVertex('d')
    g.addVertex('e')
    g.addVertex('f')
    g.addVertex('g')
    g.addVertex('h')

    g.addEdge('a', 'b', 1)
    g.addEdge('b', 'h', 1)
    g.addEdge('b', 'c', 1)
    g.addEdge('c', 'd', 1)
    g.addEdge('c', 'e', 1)
    g.addEdge('h', 'e', 1)
    g.addEdge('e', 'g', 1)
    g.addEdge('e', 'f', 1)

    print("Graph data:")
    for row in g.getEdges():
        print(f"{row[0]} -> {row[1]} : {row[2]}")

    print("\nBFS Traversal:")
    BFS(g)

    print("\nDistancias desde el inicio:")
    for v in g:
        print(f"id: {v.getId()}, distancia: {v.getDistance()}")