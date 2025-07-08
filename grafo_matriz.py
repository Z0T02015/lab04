class Vertex:
    def __init__(self, node):
        self.id = node

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

class Graph:
    def __init__(self, numVertices, cost=-1):
        self.adjMatrix = [[cost for _ in range(numVertices)] for _ in range(numVertices)]
        self.numVertices = numVertices
        self.vertices = []
        for i in range(numVertices):
            newVertex = Vertex(i)
            self.vertices.append(newVertex)

    def setVertex(self, vtx, id):
        if 0 <= vtx < self.numVertices:
            self.vertices[vtx].setId(id)

    def getVertexIndex(self, n):
        for i in range(self.numVertices):
            if n == self.vertices[i].getId():
                return i
        return -1

    def getVertex(self, index):
        return self.vertices[index]

    def addEdge(self, frm, to, cost=0):
        if self.getVertexIndex(frm) != -1 and self.getVertexIndex(to) != -1:
            idx_frm = self.getVertexIndex(frm)
            idx_to = self.getVertexIndex(to)
            self.adjMatrix[idx_frm][idx_to] = cost
            self.adjMatrix[idx_to][idx_frm] = cost  # undirected

    def getVertices(self):
        return [self.vertices[i].getId() for i in range(self.numVertices)]

    def printMatrix(self):
        print("=== Matriz de Adyacencia ===")
        for row in self.adjMatrix:
            print(row)

    def getEdges(self):
        edges = []
        for v in range(self.numVertices):
            for u in range(self.numVertices):
                if self.adjMatrix[u][v] != -1:
                    vid = self.vertices[v].getId()
                    uid = self.vertices[u].getId()
                    edges.append((uid, vid, self.adjMatrix[u][v]))
        return edges

# ------------------ PRUEBA ------------------
if __name__ == '__main__':
    G = Graph(6)
    G.setVertex(0, 'a')
    G.setVertex(1, 'b')
    G.setVertex(2, 'c')
    G.setVertex(3, 'd')
    G.setVertex(4, 'e')
    G.setVertex(5, 'f')

    print('Datos del grafo:')
    G.addEdge('a', 'e', 10)
    G.addEdge('a', 'c', 20)
    G.addEdge('c', 'b', 30)
    G.addEdge('b', 'e', 40)
    G.addEdge('e', 'd', 50)
    G.addEdge('f', 'e', 60)

    G.printMatrix()

    print("\n Aristas:")
    for edge in G.getEdges():
        print(edge)