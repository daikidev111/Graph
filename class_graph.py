# this is the adjacency list

class Graph:
    def __init__(self, V):
        # # array for the adjacency list
        # self.vertices = [None] * len(V)
        #
        # for i in range(len(V)):
        #     self.vertices[i] = Vertex(V[i])

        # adjacency matrix
        self.matrix = [None] * len(V)
        for i in range(len(V)):
            self.matrix[i] = [None] * len(V)

    def __str__(self):
        output = ""
        for vertex in self.vertices:
            output = output + "Vertex" + str(vertex) + "\n"
        return output


class Vertex:
    def __init__(self, id):
        self.id = id
        self.edges = []

    def __str__(self):
        return_string = str(self.id)
        return return_string


class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w


if __name__ == '__main__':
    vertices = [1, 2, 3, 4, 5]
    g = Graph(V=vertices)
    print(g)