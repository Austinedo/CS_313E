import unittest
from typing import List, Tuple
from example_023_minimum_spanning_tree_Prims_algo import Graph, Vertex

class TestPrimsAlgorithm(unittest.TestCase):
    
    def setUp(self):
        # Test Case 1: Empty Graph
        self.graph1 = Graph()
        # no edges in an empty graph
        self.expected_output1 = []
        
        # Test Case 2: Graph with a single vertex
        self.graph2 = Graph()
        self.graph2.add_vertex(range(1))
        # no edges in a graph with a single vertex
        self.expected_output2 = []

        # Test Case 3: Normal Graph with MST
        self.graph3 = Graph()
        self.graph3.add_verticies(range(7))
        self.graph3.add_undirected_edge(0, 1, 30)
        self.graph3.add_undirected_edge(0, 6, 10)
        self.graph3.add_undirected_edge(1, 4, 13)
        self.graph3.add_undirected_edge(1, 2, 15)
        self.graph3.add_undirected_edge(2, 3, 12)
        self.graph3.add_undirected_edge(3, 4, 16)
        self.graph3.add_undirected_edge(3, 5, 20)
        self.graph3.add_undirected_edge(4, 5, 21)
        self.graph3.add_undirected_edge(5, 6, 22)
        self.expected_output3 = [(0, 6, 10), (6, 5, 22), (5, 3, 20), (3, 2, 12), (2, 1, 15), (1, 4, 13)]

        # Test Case 4: Disconnected Graph
        self.graph4 = Graph()
        self.graph4.add_verticies(range(6))
        self.graph4.add_undirected_edge(0, 1, 2)
        self.graph4.add_undirected_edge(0, 2, 10)
        self.graph4.add_undirected_edge(1, 2, 5)
        self.graph4.add_undirected_edge(3, 4, 20)
        self.graph4.add_undirected_edge(3, 5, 10)
        self.graph4.add_undirected_edge(4, 5, 7)
        self.expected_output4 = [] 

    
    def test_prims_algorithm_with_graph1(self):
        # Empty Graph
        self.assertEqual(self.graph1.prims(), self.expected_output1)
        
    def test_prims_algorithm_with_graph2(self):
        # Graph with a single vertex
        self.assertEqual(self.graph2.prims(), self.expected_output2)
    
    def test_prims_algorithm_with_graph3(self):
        # Normal Graph with a MST
        self.assertEqual(self.graph3.prims(), self.expected_output3)
    
    def test_prims_algorithm_with_graph4(self):
        # Disconnected Graph
        self.assertEqual(self.graph4.prims(), self.expected_output4)

if __name__ == '__main__':
    unittest.main()
