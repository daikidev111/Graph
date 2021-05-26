from queue import Queue


class Graph:
    def __init__(self, V):
        # array for the adjacency list
        self.vertices = [None] * len(V)

        for i in range(len(V)):
            self.vertices[i] = Vertex(V[i])

    def add_edges(self, edges, prices):
        for edge in edges:
            u = edge[0]
            v = edge[1]
            ratio = edge[2]
            w = edge[2] * prices[v]
            current_edge = Edge(u, v, w, ratio)
            current_vertex = self.vertices[u]
            current_vertex.add_edge(current_edge)

    def __str__(self):
        output = ""
        for vertex in self.vertices:
            output = output + "Vertex" + str(vertex) + "\n"
        return output


class Vertex:
    def __init__(self, liquor_id):
        self.liquor_id = liquor_id
        self.edges = []
        self.discovered = False
        self.visited = False
        self.litre = 1

    def add_edge(self, edge):
        self.edges.append(edge)


class Edge:
    def __init__(self, u, v, w, ratio):
        self.u = u
        self.v = v
        self.w = w
        self.ratio = ratio

    def __str__(self):
        return_string = str(self.u) + "," + str(self.v) + "," + str(self.w) + "," + str(self.ratio)
        return return_string


def best_trades(prices, starting_liquid, max_trades, townspeople):
    # initialize graph

    # count how many vertices there are
    edges = []
    vertex_list = []
    for i in range(len(townspeople)):
        edges += townspeople[i]

    for edge in edges:
        if not edge[0] in vertex_list:
            vertex_list.append(edge[0])
        if not edge[1] in vertex_list:
            vertex_list.append(edge[1])

    # initialize a graph
    graph = Graph(vertex_list)

    # now add edges
    graph.add_edges(edges, prices)

    # graph
    return BellmanFord(graph.vertices, starting_liquid, max_trades, [10, 5, 1, 0.1])


def BellmanFord(graph, source, max_trades, prices):
    dist = [float("Inf")] * len(graph)
    dist[source] = 0
    predecessor = [None] * len(graph)

    # finding the starting point of the graph
    for vertex in graph:
        if vertex.liquor_id == source:
            source = vertex

    discovered_queue = Queue()
    discovered_queue.put(source)

    while max_trades >= 0:
        vertex = discovered_queue.get()
        for edge in vertex.edges:
            litre = vertex.litre
            u = edge.u
            v = edge.v
            litre = litre * edge.ratio
            w = edge.w
            price = prices[vertex.liquor_id]
            print(price)

        if dist[u] != float("Inf") and dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
    print(dist)


if __name__ == '__main__':
    prices = [10, 5, 1, 0.1]
    starting_liquid = 0
    max_trades = 6
    townspeople = [[(0, 1, 4), (2, 3, 30)], [(1, 2, 2.5), (2, 0, 0.2), (2, 2, 1)]]
    print(best_trades(prices, starting_liquid, max_trades, townspeople))
