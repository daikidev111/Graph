# this is the adjacency list
from Queue import Queue


class Graph:
    def __init__(self, V):
        # array for the adjacency list
        self.vertices = [None] * len(V)

        for i in range(len(V)):
            print(V)
            self.vertices[i] = Vertex(V[i])

    def __str__(self):
        output = ""
        for vertex in self.vertices:
            output = output + "Vertex" + str(vertex) + "\n"
        return output

    def bfs(self, source):
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
                if not v.discovered:  # if the vertex is not discovered yet then append
                    discovered.append(v)
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


    def dijkastra(self, source):
        source.distance = 0
        discovered = MinHeap()  # make it minheap()
        discovered.append(source.distance, 0) # append(key, data)
        while len(discovered) > 0:
            # break out of the loop once it has nothing to be discovered anymore
            u = discovered.pop(0)  # serve for queue
            u.visited = True # means I have visited, distance is finalized
            # perform edge relaxation
            for edge in u.edges:
                # looping through the vertex's edges
                v = edge.v  # v is directed vertex
                # distance is still /inf
                if not v.discovered:  # if the vertex is not discovered yet then append
                    v.discovered = True
                    v.distance = u.distance + edge.w
                    v.previous = u
                    discovered.append(v.distance, v)

                    # TODO implement the backtracking

                # in heap, but not finalized
                elif v.visited == False:
                    # if u found a shorter one, change it (edge relaxation)
                    if v.distance > u.distance + edge.w:
                        #update distance
                        v.distance = u.distance + edge.w
                        v.previous = u
                        #TODO update Heap
                        discovered.update(v, v.distance) # update vertex v in heap, with distance v.distance; perform rise





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
