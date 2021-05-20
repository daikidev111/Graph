class Graph:
    def __init__(self, V):
        # array for the adjacency list
        self.vertices = [None] * len(V)

        for i in range(len(V)):
            self.vertices[i] = Vertex(V[i])

    def add_edges(self, edges):
        for edge in edges:
            u = edge[0]
            v = edge[1]
            w = edge[2]
            current_edge = Edge(u, v, w)
            current_vertex = self.vertices[u]
            current_vertex.add_edge(current_edge)

    def __str__(self):
        output = ""
        for vertex in self.vertices:
            output = output + "Vertex" + str(vertex) + "\n"
        return output


class Vertex:
    def __init__(self, id):
        self.id = id
        self.edges = []
        self.discovered = False
        self.visited = False
        self.distance = 0
        self.predecessor = None

    def add_edge(self, edge):
        self.edges.append(edge)

    def __str__(self):
        return_string = str(self.id)
        return return_string


class Edge:
    def __init__(self, u, v, w):
        # u is the liquor to be traded
        # v is the liquor to be received
        # w is the ratio
        self.u = u
        self.v = v
        self.w = w

    def __str__(self):
        return_string = str(self.u) + "," + str(self.v) + "," + str(self.w)
        return return_string


if __name__ == '__main__':
    vertices = [1, 2, 3, 4, 5]
    g = Graph(V=vertices)
    print(g)

    edges = []
    edges.append((3, 1, 5))  # vertex 3 to 1 with w = 5
    edges.append((1, 2, 1))
    edges.append((3, 2, -5))
    edges.append((3, 4, 322))
    g.add_edges(edges)

