from queue import Queue


class Graph:
    def __init__(self, V_count):
        # array for the adjacency list
        self.vertices = [None] * V_count

        for i in range(V_count):
            print(i)
            self.vertices[i] = Vertex(i)

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
        # TODO should I assign liquor id here ? 1
        self.id = id
        self.edges = []
        self.discovered = False
        self.visited = False
        self.distance = 0
        # self.predecessor = None do we need this??

    def add_edge(self, edge):
        self.edges.append(edge)

    # def __str__(self):
    #     return_string = str(self.id)
    #     return return_string


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


def best_trades(prices, starting_liquid, max_trades, townspeople):
    # initialize graph

    # count how many vertices there are
    v_count = 0
    edges = []
    for i in range(len(townspeople)):
        v_count += len(townspeople[i])
        edges += townspeople[i]
    print(edges)

    # initialize a graph
    graph = Graph(v_count)

    # now add edges
    graph.add_edges(edges)

    return bellman_ford_test(graph.vertices, starting_liquid, max_trades) # vertices has been added but named as graph


def initialize(graph, source):
    d = {}
    p = {}

    # TODO: need to input liquor id instead of the vertex itself
    for node in graph:
        d[node] = float('Inf')
        p[node] = None
    d[source] = 0
    return d, p


def bellman_ford(graph, source, max_trades):
    d, p = initialize(graph, source)
    for i in range(max_trades):  # i = |v| - 1
        for vertex in graph:
            for edge in vertex.edges:
                print("current point " + str(edge.u))
                print(" next direction " + str(edge.v))

                print("weight is " + str(graph[edge.u].edges))

                print("weight is " + str(graph[edge.u].edges[edge.v].w))
                # relax(edge, edge.u, edge.v, graph, d, p)

    return d, p


def bellman_ford_test(graph, source, max_trades):
    d, p = initialize(graph, source)
    source = graph[source]
    source.distance = 0
    discovered_queue = Queue()
    discovered_queue.put(source)
    res = []

    while discovered_queue._qsize() > 0:
        u = discovered_queue.get()
        u.visited = True
        res.append(u)
        for edge in u.edges:
            # looping through the vertex's edges
            relax(edge, edge.u, edge.v, graph, d, p)
            v = edge.v  # v is directed vertex

            v = graph[v]  # moving to the vertex V

            # check if the vertex is not visited and discovered
            if not v.discovered and not v.visited:  # if the vertex is not discovered yet then append
                discovered_queue.put(v)  # append it in the queue
                # v.distance = u.distance + 1
                v.discovered = True


def relax(edge, node, neighbour, graph, d, p):
    if d[graph[node]] < edge.w:  # b has inf > -1
        # Record this lower distance
        d[graph[neighbour]] = d[graph[node]] + graph[node].edges[neighbour - 1].w
        p[neighbour] = graph[node]  # record the predecessor


if __name__ == '__main__':
    prices = [10, 5, 1, 0.1]
    starting_liquid = 0
    max_trades = 6
    townspeople = [[(0, 1, 4), (2, 3, 30)], [(1, 2, 2.5), (2, 0, 0.2), (2, 2, 1)]]
    best_trades(prices, starting_liquid, max_trades, townspeople)
