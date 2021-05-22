from queue import Queue


class Graph:
    def __init__(self, V):
        # array for the adjacency list
        self.vertices = [None] * len(V)

        res = []
        for i in range(len(V)):
            res.append(Vertex(V[i][0]))
            res.append(Vertex(V[i][1]))

        self.vertices = res

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
    def __init__(self, liquor_id):
        self.liquor_id = liquor_id
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
    edges = []
    for i in range(len(townspeople)):
        edges += townspeople[i]

    # initialize a graph
    graph = Graph(edges)

    # now add edges
    graph.add_edges(edges)

    # return bellman_ford_test(graph.vertices, starting_liquid, max_trades)  # vertices has been added but named as
    # graph
    return bellman_ford_test(graph.vertices, starting_liquid, max_trades, prices)


def initialize(graph, source):
    d = {}
    p = {}

    for node in graph:
        d[node.liquor_id] = float('Inf')
        p[node.liquor_id] = None
    d[source] = 0
    return d, p


def bellman_ford_test(graph, source, max_trades):
    d, p = initialize(graph, source)

    source = graph[source]

    source.distance = 0
    discovered_queue = Queue()
    discovered_queue.put(source)

    while discovered_queue._qsize() > 0:
        u = discovered_queue.get()
        u.visited = True

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
    return d, p


def relax(edge, node, neighbour, graph, d, p):
    if d[node] < edge.w:  # b has inf > -1
        # Record this lower distance
        d[neighbour] = d[node] + edge.w
        p[neighbour] = node  # record the predecessor
