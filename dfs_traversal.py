from graph.impl_adj_list import Vertex, Graph

def dfs(g, currentVert, visited):
    visited[currentVert] = True
    print("Traversal:", currentVert.getId())
    for nbr in currentVert.getAdjLists():
        if nbr not in visited:
            dfs(g, nbr, visited)

def DFSTraversal(g):
    visited = {}
    for currentVert in g:
        if currentVert not in visited:
            dfs(g, currentVert, visited)

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

    print("\nDFS Traversal:")
    DFSTraversal(g)