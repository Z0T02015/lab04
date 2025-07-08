class Vertex:
    def __init__(self, key):
        self.id = key
        self.adjList = {}
        self.visited = False
        self.distance = -1
        self.previous = None
    def addNeighbor(self, nbr, weight=0):
        self.adjList[nbr] = weight
    def getAdjLists(self):
        return self.adjList.keys()
    def getId(self):
        return self.id
    def getWeight(self, nbr):
        return self.adjList[nbr]
    def setDistance(self, dist):
        self.distance = dist
    def getDistance(self):
        return self.distance
    def setPrevious(self, prev):
        self.previous = prev
    def setVisited(self):
        self.visited = True
class Graph:
    def __init__(self):
        self.vertices = {}
    def addVertex(self, key, dist=-1):
        vertex = Vertex(key)
        vertex.setDistance(dist)
        self.vertices[key] = vertex
        return vertex

    def getVertex(self, n):
        return self.vertices.get(n)

    def addEdge(self, f, t, weight=0):
        if f not in self.vertices:
            self.addVertex(f)
        if t not in self.vertices:
            self.addVertex(t)
        self.vertices[f].addNeighbor(self.vertices[t], weight)

    def getVertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())

    def getEdges(self):
        edges = []
        for v in self.vertices.values():
            for w in v.getAdjLists():
                edges.append((v.getId(), w.getId(), v.getWeight(w)))
        return edges