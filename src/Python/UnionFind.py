import Python.Graph


class UnionFindNode(object):
    def __init__(self, value):
        self.children = []
        self.father = self
        self.value = value
        self.size = 1

    def union(self, other):
        self_father = self.find()
        other_father = other.find()
        if self_father != other_father:
            if self_father.size >= other_father.size:
                if other != other_father:
                    other.switch_parents()
                self.update_size(other.size)
                self.children.append(other)
                other.set_father(self)
                return self, other
            else:
                if self != self_father:
                    self.switch_parents()
                other.update_size(self.size)
                other.children.append(self)
                self.set_father(other)
                return other, self
        return self, other

    def find(self):
        while self.father != self:
            self = self.father
        return self

    def switch_parents(self):
        if self.father.father != self.father:
            self.children.append(self.father)
            self.father.switch_parents()
        else:
            self.children.append(self.father)
        self.size = self.father.size
        self.father.set_father(self)
        self.father.children.remove(self)

    def update_size(self, value):
        if self.father != self:
            self.size += value
            self.father.update_size(value)
        self.size += value

    def set_father(self, father):
        self.father = father

    def get_value(self):
        return self.value

    def get_size(self):
        return self.size


def Kruskal_MST(graph):
    edges = graph.sort_edges()
    nodes = dict()
    for vertex in graph.V:
        nodes[vertex.get_value()] = UnionFindNode(vertex.get_value())
    while edges:
        edge = edges[0]
        u, v = edge.get_sides()
        nodes[u.get_value()].union(nodes[v.get_value()])
        edges.pop(0)




def main():
    graph = Python.Graph.Graph()
    V = []
    for i in range(10):
        V.append(Python.Graph.Vertex(i, graph))
    V[0].connect([V[1], V[2], V[3]], [5, 3, 4])
    V[1].connect(V[6], 1)
    V[5].connect([V[2], V[3]], [7, 1])
    V[7].connect([V[5], V[9], V[6]], [2, 1, 2])
    V[4].connect([V[3], V[8]], [6, 3])
    V[8].connect(V[9], 4)
    Kruskal_MST(graph)


main()
