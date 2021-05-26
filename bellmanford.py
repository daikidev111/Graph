# Step 1: For each node prepare the destination and predecessor (initialization) i = 0
def initialize(graph, source):
    d = {}  # Stands for destination
    p = {}  # Stands for predecessor
    for node in graph:
        d[node] = float('Inf')  # We start admitting that the rest of nodes are very very far
        p[node] = None
    d[source] = 0  # For the source we know how to reach
    return d, p


def relax(node, neighbour, graph, d, p):

    # If the distance between the node and the neighbour is lower than the one I have now
    print(node)
    print(graph)
    print(" weight is: " + str(graph[node][neighbour]))
    if d[neighbour] > d[node] + graph[node][neighbour]:  # b has inf > -1
        # Record this lower distance
        d[neighbour] = d[node] + graph[node][neighbour]
        p[neighbour] = node  # record the predecessor


def bellman_ford(graph, source):
    d, p = initialize(graph, source)
    for i in range(len(graph) - 1):  # i = |v| - 1
        if i == 0:
            for u in graph:
                for v in graph[u]:  # v is the direction to the next node from the source node
                    relax(u, v, graph, d, p)  # Lets relax it

    # Step 3: check for negative-weight cycles
    for u in graph:
        for v in graph[u]:
            assert d[v] <= d[u] + graph[u][v]

    return d, p



def test():
    graph = {
        'a': {'b': -1, 'c': 4},
        'b': {'c': 3, 'd': 2, 'e': 2},
        'c': {},
        'd': {'b': 1, 'c': 5},
        'e': {'d': -3}
    }

    d, p = bellman_ford(graph, 'a')
    print(d, p)

    assert d == {
        'a': 0,
        'b': -1,
        'c': 2,
        'd': -2,
        'e': 1
    }

    assert p == {
        'a': None,
        'b': 'a',
        'c': 'b',
        'd': 'e',
        'e': 'b'
    }


if __name__ == '__main__': test()
