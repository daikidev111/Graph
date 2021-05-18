# this is the adjacency list
from Queue import Queue


class Graph:
    def __init__(self, argv_vertices_count):
        # array for the adjacency list
        self.vertices = [None] * argv_vertices_count

        for i in range(argv_vertices_count):
            self.vertices[i] = Vertex(i)

    def __str__(self):
        output = ""
        for vertex in self.vertices:
            output = output + "Vertex" + str(vertex) + "\n"
        return output

    def add_edge(self, argv_edges):
        for edge in argv_edges:
            u = edge[0]
            v = edge[1]
            w = edge[2]
            current_edge = Edge(u, v, w)
            current_vertex = self.vertices[u]  # retrieve the vertex that starts from the u
            current_vertex.add_edge(current_edge)  # add extra edge to the vertex u



            # # if you want undirected graph...
            # # add u to v
            # current_edge = Edge(u, v, w)
            # current_vertex = self.vertices[u]  # retrieve the vertex that starts from the u
            # current_vertex.add_edge(current_edge)  # add extra edge to the vertex u
            #
            # # add v to u
            # current_edge = Edge(v, u, w)
            # current_vertex = self.vertices[v]  # retrieve the vertex that starts from the u
            # current_vertex.add_edge(current_edge)  # add extra edge to the vertex u

    def reset(self):
        # this is for reachability
        for vertex in self.vertices:
            vertex.discovered = False
            vertex.visited = False

    def bfs(self, source):
        self.reset()
        source = self.vertices[source]
        source.distance = 0 # to find shortest cycle
        discovered = []  # make it queue
        return_bfs = []
        discovered.append(source)
        while len(discovered) > 0:
            # break out of the loop once it has nothing to be discovered anymore
            u = discovered.pop(0)  # serve for queue
            u.visited = True
            return_bfs.append(u)
            for edge in u.edges:
                # looping through the vertex's edges
                v = edge.v  # v is directed vertex
                if source == v:
                    return len(return_bfs)

                v = self.vertices[v]
                if v.discovered:
                    print("Found cycle")
                if not v.discovered and not v.visited:  # if the vertex is not discovered yet then append
                    discovered.append(v)
                    v.distance = u.distance + 1 # this is to find a shortest cycle
                    v.discovered = True
        return return_bfs

    def bfs_distance(self, source):
        discovered = []  # make it queue
        discovered.append(source)
        while len(discovered) > 0:
            # break out of the loop once it has nothing to be discovered anymore
            u = discovered.pop(0)  # serve for queue
            u.visited = True
            for edge in u.edges:
                # looping through the vertex's edges
                v = edge.v  # v is directed vertex
                if not v.discovered:  # if the vertex is not discovered yet then append
                    discovered.append(v)
                    v.discovered = True
                    v.distance = u.distance + 1
                    v.previous = u
                    # TODO implement the backtracking

    def dfs(self, source):

        # discovered is a stack, so it follows LIFO
        # TODO: create stack that has push and pop methods
        discovered = []  # make it queue
        return_bfs = []
        discovered.append(source)  # assume append = push for now
        while len(discovered) > 0:
            # break out of the loop once it has nothing to be discovered anymore
            u = discovered.pop()  # serve for queue
            u.visited = True
            return_bfs.append(u)
            for edge in u.edges:
                # looping through the vertex's edges
                v = edge.v  # v is directed vertex
                if not v.discovered:  # if the vertex is not discovered yet then append
                    discovered.append(v)  # assume append = push for now
                    v.discovered = True
        return return_bfs

    def dfs_recursion(self, source):
        source.visited = True
        for next_vertex in source.edges:
            if not next_vertex.visited:
                self.dfs_recursion(next_vertex)


class Vertex:
    def __init__(self, id):
        self.id = id
        self.edges = []
        self.discovered = False
        self.visited = False
        self.distance = 0
        self.previous = None

    def __str__(self):
        return_string = str(self.id)
        for edge in self.edges:
            return_string = return_string + "\n with edges" + str(edge)
        return return_string

    def add_edge(self, edge):
        self.edges.append(edge)


class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

    def __str__(self):
        return_string = str(self.u) + "," + str(self.v) + "," + str(self.w)
        return return_string


    """
    Vertex0
     with edges[]
    Vertex1
     with edges[<__main__.Edge object at 0x101232b50>]
    Vertex2
     with edges[]
    Vertex3
     with edges[<__main__.Edge object at 0x101232bb0>, <__main__.Edge object at 0x101232af0>]
    Vertex4
     with edges[]
    """

if __name__ == '__main__':
    total_vertices = 5
    my_graph = Graph(total_vertices)
    print(my_graph)

    # how to insert edges
    edges = []
    edges.append((3, 1, 5))  # vertex 3 to 1 with w = 5
    edges.append((1, 2, 1))
    edges.append((3, 2, -5))
    edges.append((3, 4, 322))
    my_graph.add_edge(edges)
    print(my_graph)

    # run BFS
    bruh = my_graph.bfs(3)
    for vertex in bruh:
        print(vertex)

    """
     3
     with edges3,1,5
     with edges3,2,-5
    1
     with edges1,2,1
    2
    """

    # Reachability of a vertex
    for vertex in range(total_vertices):
        print(str(vertex) + "infected" + str(len(my_graph.bfs(vertex))))

