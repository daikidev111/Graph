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
        self.distance = 0
        self.litre = 1
        # self.predecessor = None do we need this??

    def add_edge(self, edge):
        self.edges.append(edge)

    # def __str__(self):
    #     return_string = str(self.id)
    #     return return_string


class Edge:
    def __init__(self, u, v, w, ratio):
        # u is the liquor to be traded
        # v is the liquor to be received
        # w is the ratio
        self.u = u
        self.v = v
        self.w = w
        self.ratio = ratio

    def __str__(self):
        return_string = str(self.u) + "," + str(self.v) + "," + str(self.w) + "," + str(self.ratio)
        return return_string

    def set_price(self, price):
        print(self.w)


def best_trades(prices, starting_liquid, max_trades, townspeople):
    # initialize graph

    # count how many vertices there are
    edges = []
    for i in range(len(townspeople)):
        edges += townspeople[i]

    # initialize a graph
    graph = Graph(edges)

    # now add edges
    graph.add_edges(edges, prices)

    # return bellman_ford_test(graph.vertices, starting_liquid, max_trades)  # vertices has been added but named as
    # graph
    return bellman(graph.vertices, starting_liquid, max_trades)


def bellman(graph, source, max_trades):
    d = {}
    for node in graph:
        d[node.liquor_id] = float('Inf')

    dist = [float("Inf")] * len(d)
    dist[source] = 1


    for _ in range(max_trades):
        for vertex in graph:
            print("liquor id is: " + str(vertex.liquor_id))
            for edge in vertex.edges:
                u = edge.u
                v = edge.v
                w = edge.w
                vertex.litre = vertex.litre * edge.ratio
                print(vertex.litre)
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

    print(dist)

    # TODO: make the weight be ratio
    # TODO: ratio * litre of the bottle


if __name__ == '__main__':
    prices = [10, 5, 1, 0.1]
    starting_liquid = 0
    max_trades = 6
    townspeople = [[(0, 1, 4), (2, 3, 30)], [(1, 2, 2.5), (2, 0, 0.2), (2, 2, 1)]]
    print(best_trades(prices, starting_liquid, max_trades, townspeople))
