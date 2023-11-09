import unittest
from example_022_minimum_spanning_tree_Kruskal_algo import Graph


class TestKruskalAlgorithm(unittest.TestCase):
    def setUp(self):
        # Test Case 1: Empty Graph
        self.graph1 = Graph(0)
        # no edges in an empty graph so there cannot be a MST
        self.expected_output1 = []
        
        # Test Case 2: Graph with a single vertex
        self.graph2 = Graph(1)
        # no edges in a graph with a single vertex so there cannot be a MST
        self.expected_output2 = []

        # Test Case 3: Normal Graph with MST
        self.graph3 = Graph(7)
        self.graph3.add_edge(0, 1, 30)
        self.graph3.add_edge(0, 6, 10)
        self.graph3.add_edge(1, 4, 13)
        self.graph3.add_edge(1, 2, 15)
        self.graph3.add_edge(2, 3, 12)
        self.graph3.add_edge(3, 4, 16)
        self.graph3.add_edge(3, 5, 20)
        self.graph3.add_edge(4, 5, 21)
        self.graph3.add_edge(5, 6, 22)
        # MST solution for this valid graph
        self.expected_output3 = [[0, 6, 10], [2, 3, 12], [1, 4, 13], [1, 2, 15], [3, 5, 20], [5, 6, 22]]

        # Test Case 4: Disconnected Graph
        self.graph4 = Graph(6)
        self.graph4.add_edge(0, 1, 2)
        self.graph4.add_edge(0, 2, 10)
        self.graph4.add_edge(1, 2, 5)
        self.graph4.add_edge(3, 4, 20)
        self.graph4.add_edge(3, 5, 10)
        self.graph4.add_edge(4, 5, 7)
        # No MST for a disconnected graph
        self.expected_output4 = [] 


    def test_kruskal_mst(self):
        # Compute the minimum spanning tree using Kruskal's algorithm
        self.assertEqual(self.graph3.kruskal_algo(), self.expected_output3)

    def test_kruskal_mst_empty_graph(self):
        # Test with an empty graph
        self.assertEqual(self.graph1.kruskal_algo(), self.expected_output1)

    def test_kruskal_mst_single_vertex(self):
        # Test with a graph with a single vertex
        self.assertEqual(self.graph2.kruskal_algo(), self.expected_output2)

    def test_kruskal_mst_disconnected_graph(self):
        # Test with a disconnected graph
        self.assertEqual(self.graph4.kruskal_algo(), self.expected_output4)

if __name__ == '__main__':
    unittest.main()
