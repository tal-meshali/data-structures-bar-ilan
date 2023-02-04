import Python.Graph
import numpy as np


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


class Printer():
    def __init__(self):
        self.matrix = np.ndarray((3, 3))
        self.matrix.fill(-1)
        self.col = 0
        self.row = 0

    def increment_row(self):
        self.row += 1

    def increment_col(self):
        self.col += 1

    def add_element(self, i, j, elem):
        if i > self.matrix.shape[0] - 1:
            row = np.ndarray((i - self.matrix.shape[0] + 1, self.matrix.shape[1]))
            row.fill(-1)
            self.matrix = np.append(self.matrix, row, axis=0)
        if j > self.matrix.shape[1] - 1:
            col = np.ndarray((self.matrix.shape[0], j - self.matrix.shape[1] + 1))
            col.fill(-1)
            self.matrix = np.append(self.matrix, col, axis=1)
        self.matrix[i, j] = elem

    def print(self):
        print("MST using Kruskal's algorithm:")
        for i in range(self.matrix.shape[0]):
            noted = False
            for j in range(self.matrix.shape[1]):
                c = self.matrix[i, j]
                if noted:
                    if c < 0:
                        noted = False
                    else:
                        print("--", sep='', end='')
                if c >= 0:
                    noted = True
                    s = ""
                    if j < self.matrix.shape[1] - 1:
                        if c < 10 and self.matrix[i, j + 1] != -1:
                            s = "-"
                    print(int(c), s, sep='', end='')
                else:
                    print("    ", sep='', end='')
            print("\n", end='')
            if i != self.matrix.shape[0] - 1:
                for j in range(self.matrix.shape[1]):
                    c = self.matrix[i + 1, j]
                    if c > 0:
                        print("|\n", end='')
                        break
                    else:
                        print("    ", end='')


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
    return list(nodes.values())[0].find()


def print_MST(root, printer, level=0, layer=0):
    if root.children:
        for child in root.children:
            print_MST(child, printer, printer.row, layer + 1)
    else:
        printer.add_element(level, layer, root.get_value())
        printer.increment_row()
    printer.add_element(level, layer, root.get_value())
    if layer == 0:
        return printer


def main():
    graph = Python.Graph.Graph()
    V = []
    for i in range(14):
        V.append(Python.Graph.Vertex(i, graph))
    V[0].connect([V[1], V[2], V[3]], [5, 3, 4])
    V[1].connect(V[6], 1)
    V[5].connect([V[2], V[3]], [7, 1])
    V[7].connect([V[5], V[9], V[6]], [2, 1, 2])
    V[4].connect([V[3], V[8]], [6, 3])
    V[8].connect(V[9], 4)
    V[13].connect([V[4], V[8], V[7]], [1, 5, 3])
    V[10].connect([V[8], V[9]], [2, 4])
    V[11].connect([V[4], V[10]], [3, 7])
    V[12].connect([V[3], V[11], V[4]], [6, 2, 4])
    t = Kruskal_MST(graph)
    print_MST(t, Printer()).print()


main()
