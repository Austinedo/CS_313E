#  File: Adjacency.py
#  Description: Converts an edge list into an adjacency matrix
#  Student Name: Austine Do
#  Student UT EID: ahd589
#  Course Name: CS 313E
#  Unique Number: 52590

def edge_to_adjacency(edge_list):
    nodes = set()
    for edge in edge_list:
        nodes.add(edge[0])
        nodes.add(edge[1])
    
    sorted_nodes = sorted(nodes)
    node_to_index = {node: i for i, node in enumerate(sorted_nodes)}
    num_nodes = len(node_to_index)

    matrix = [[0] * num_nodes for _ in range(num_nodes)]

    for edge in edge_list:
        start_node_index = node_to_index[edge[0]]
        end_node_index = node_to_index[edge[1]]
        weight = edge[2]

        matrix[start_node_index][end_node_index] = weight

    return matrix

# ------ DO NOT CHANGE BELOW HERE ------ #
import ast

def main():
    matrix = edge_to_adjacency(ast.literal_eval(input()))

    print('\n'.join([' '.join([str(cell) for cell in row]) for row in matrix]))

if __name__ == "__main__":
    main()
