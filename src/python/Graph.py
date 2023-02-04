class Edge(object):
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

    def get_other(self, other):
        if self.u == other:
            return self.v
        if self.v == other:
            return self.u

    def get_weight(self):
        return self.weight

    def get_sides(self):
        return self.u, self.v


class Vertex(object):
    def __init__(self, name, graph):
        self.connections = dict()
        self.graph = graph
        self.name = name
        self.graph.set_vertex(self)

    def connect_vertex(self, other, weight):
        edge = Edge(self, other, weight)
        self.connections[other.name] = edge
        other.connections[self.name] = edge
        self.graph.add_edge(edge)

    def connect(self, others, weights):
        if type(others) == Vertex:
            self.connect_vertex(others, weights)
        else:
            for other, weight in zip(others, weights):
                self.connect_vertex(other, weight)

    def vertex_from_edge(self, other):
        return self.connections[other].get_other(self)

    def disconnect(self, other):
        for neighbor in self.connections.keys():
            if self.vertex_from_edge(neighbor) == other:
                edge = self.connections[other.name]
                other.connections.pop(self.name)
                self.graph.E.remove(edge)
                return edge.weight

    def get_value(self):
        return self.name


class Graph(object):
    def __init__(self):
        self.E = set()
        self.V = set()

    def set_vertex(self, vertex):
        self.V.add(vertex)

    def add_vertex(self, vertex, connections, weights):
        self.V.add(vertex)
        for connection, weight in (connections, weights):
            vertex.connect(connection, weight)

    def add_edge(self, edge):
        self.E.add(edge)

    def remove_vertex(self, vertex):
        for key in vertex.connections.keys():
            vertex.disconnect(vertex.connections[key].get_other(vertex))
        self.V.remove(vertex)

    def sort_edges(self):
        edges = list(self.E)
        edges.sort(key=Edge.get_weight)
        return edges



