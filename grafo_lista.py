# -------- Vertex (Nodo) --------
class Vertex:
    def __init__(self, key):
        self.id = key
        self.adjList = {}  # Diccionario: vecino -> peso

    def addNeighbor(self, nbr, weight=0):
        self.adjList[nbr] = weight

    def getAdjLists(self):
        return self.adjList.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.adjList[nbr]

# -------- Graph (Lista de adyacencia) --------
class Graph:
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex

    def getVertex(self, n):
        return self.vertices.get(n, None)

    def addEdge(self, f, t, weight=0):
        if f not in self.vertices:
            self.addVertex(f)
        if t not in self.vertices:
            self.addVertex(t)
        self.vertices[f].addNeighbor(self.vertices[t], weight)

    def getVertices(self):
        return self.vertices.keys()

    def getEdges(self):
        edges = []
        for v in self.vertices.values():
            for w in v.getAdjLists():
                vid = v.getId()
                wid = w.getId()
                weight = v.getWeight(w)
                edges.append((vid, wid, weight))
        return edges

# -------- PRUEBA (main) --------
if __name__ == '__main__':
    g = Graph()

    for i in range(6):
        g.addVertex(i)

    g.addEdge(0, 1, 5)
    g.addEdge(0, 5, 2)
    g.addEdge(1, 2, 4)
    g.addEdge(2, 3, 9)
    g.addEdge(3, 4, 7)
    g.addEdge(3, 5, 3)
    g.addEdge(4, 0, 1)
    g.addEdge(5, 4, 8)
    g.addEdge(5, 2, 1)

    print("Aristas del grafo:")
    for v in g.vertices.values():
        for w in v.getAdjLists():
            print(f"( {v.getId()} , {w.getId()} , {v.getWeight(w)} )")         
print("Modificado por rama-conflicto-a")