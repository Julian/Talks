from collections import defaultdict


class Graph(object):
    def __init__(self):
        self.adjacency = defaultdict(set)

    def __getitem__(self, v):
        return self.adjacency[v]

    def add_edge(self, from_vertex, to_vertex):
        self.adjacency[from_vertex].add(to_vertex)
