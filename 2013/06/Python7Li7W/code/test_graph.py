from graph import Graph

from unittest import TestCase


class TestGraph(TestCase):
    def test_neighbors(self):
        g = Graph()
        g.add_edge(12, 3)
        self.assertIn(3, g[12])
