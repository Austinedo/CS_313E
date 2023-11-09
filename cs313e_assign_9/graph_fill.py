#  File: graph_fill.py
#  Description: An image fill program that utilizes graphs,
#               BFS, and DFS to fill selected areas of an
#               image graph
#  Student Name: Austine Do
#  Student UT EID: ahd589
#  Partner Name: Ahyeon Ko
#  Partner UT EID: ak42464
#  Course Name: CS 313E
#  Unique Number: 52590
#  Date Created: 11/1/23
#  Date Last Modified: 11/3/23
"""
Used for standard input and files
"""
import os
import sys

# -----------------------PRINTING LOGIC, DON'T WORRY ABOUT THIS PART----------------------------

# this enables printing colors on Windows somehow
os.system("")

# code to reset the terminal color
RESET_CHAR = "\u001b[0m"

# color codes for the terminal
COLOR_DICT = {
    "black": "\u001b[30m",
    "red": "\u001b[31m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33m",
    "blue": "\u001b[34m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m"
}

# character code for a block
BLOCK_CHAR = "\u2588"

def colored(text, color):
    """
    Input: text is some string we want to write in a specific color
           color is the name of a color that is looked up in COLOR_DICT
    Output: returns the string wrapped with the color code
    """
    color = color.strip().lower()
    if not color in COLOR_DICT:
        raise Exception(color + " is not a valid color!")
    return COLOR_DICT[color] + text

def print_block(color):
    """
    Input: color is the name of a color that is looked up in COLOR_DICT
           prints a block (two characters) in the specified color
    """
    print(colored(BLOCK_CHAR, color)*2, end='')

# -----------------------PRINTING LOGIC, DON'T WORRY ABOUT THIS PART----------------------------


# Stack class; you can use this for your search algorithms
class Stack:
    '''
    Class Stack
    '''
    def __init__(self):
        self.stack = []

    def push(self, item):
        """
        Adds 'item' to the top of the stack
        """
        self.stack.append(item)

    def pop(self):
        """
        Removes an item from the top of the stack
        """
        return self.stack.pop()

    def peek(self):
        """
        Checks the item on the top of stack
        """
        return self.stack[-1]

    def is_empty(self):
        """
        Checks if the stack is empty
        """
        return len(self.stack) == 0

    def size(self):
        """
        Returns the number of elements in the stack
        """
        return len(self.stack)


class Queue:
    """
    Class Queue
    """
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """
        Appends 'item' to the end of the queue
        """
        self.queue.append(item)

    def dequeue(self):
        """
        Removes and returns the item from the beginning of the queue
        """
        return self.queue.pop(0)

    def peek(self):
        """
        Checks the item at the beginning of the Queue
        """
        return self.queue[0]

    def is_empty(self):
        """
        Checks if the queue is empty
        """
        return len(self.queue) == 0

    def size(self):
        """
        Returns the size of the queue
        """
        return len(self.queue)

# class for a graph node; contains x and y coordinates, a color, a list of edges and
# a flag signaling if the node has been visited (useful for search algorithms)
# it also contains a "previous color" attribute. This might be useful for
# your flood fill implementation.
class ColorNode:
    """
    Class ColorNode used for ImageGraph
    """
    def __init__(self, index, x_coord, y_coord, color):
        self.index = index
        self.color = color
        self.prev_color = color
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.edges = []
        self.visited = False

    # Input: node_index is the index of the node we want to create an edge to in the node list
    # adds an edge and sorts the list of edges
    def add_edge(self, node_index):
        """
        Input: node_index is the index of the node we want to create an edge to
               and appends this to the .edge list of the node
        """
        self.edges.append(node_index)

    # Input: color is the name of the color the node should be colored in;
    # the function also saves the previous color (might be useful for
    # your flood fill implementation)
    def visit_and_set_color(self, color):
        """
        Input: color is the name of the color the node should be colored in;
        The function also save the previous color (which may be useful for
        your flood fill implementation)
        """
        self.visited = True
        self.prev_color = self.color
        self.color = color

        print("Visited node " + str(self.index))


class ImageGraph:
    """
    Class ImageGraph that contains the graph for ColorNode
    """
    def __init__(self, image_size):
        self.nodes = []
        self.image_size = image_size

    def print_image(self):
        """
        Prints the image formed by the nodes on the command line
        """
        img = [["black" for i in range(self.image_size)] for j in range(self.image_size)]

        # fill img array
        for node in self.nodes:
            img[node.y_coord][node.x_coord] = node.color

        for line in img:
            for pixel in line:
                print_block(pixel)
            print()
        # print new line/reset color
        print(RESET_CHAR)

    def reset_visited(self):
        """
        Sets the visited flag on the ColorNode to False for
        all nodes in the graph
        """
        for node in self.nodes:
            node.visited = False

    def print_adjacency_matrix(self):
        """
        Prints the adjacency matrix for the graph
        """
        print("Adjacency matrix:")

        adj_matrix = [[0 for _ in range(len(self.nodes))] for _ in range(len(self.nodes))]

        for i, node in enumerate(self.nodes):
            for edge in node.edges:
                adj_matrix[i][edge] = 1

        for row in adj_matrix:
            print("".join(map(str, row)))

        # empty line afterwards
        print()

    # implement your bfs algorithm here. Call print_image() after coloring a node
    # Input: graph is the graph containing the nodes
    #   start_index is the index of the currently visited node
    #   color is the color to fill the area containing the current node with
    def bfs(self, start_index, color):
        """
        Performs a BFS on the ImageGraph and prints it to command line
        Input: start_index: refers to the ColorNode to begin the search
               color: the color to change the node to after visiting
        """
        # reset visited status
        self.reset_visited()
        # print initial state
        print("Starting BFS; initial state:")
        self.print_image()

        queue = Queue()
        start_node = self.nodes[start_index]
        previous_color = start_node.color
        queue.enqueue(start_node)

        while not queue.is_empty():
            current_node = queue.dequeue()
            if current_node.color == previous_color and not current_node.visited:
                current_node.visit_and_set_color(color)
                self.print_image()
            for neighbor_index in current_node.edges:
                neighbor = self.nodes[neighbor_index]
                if not neighbor.visited and neighbor.color == previous_color:
                    queue.enqueue(neighbor)

    # implement your dfs algorithm here. Call print_image() after coloring a node
    # Input: graph is the graph containing the nodes
    #   start_index is the index of the currently visited node
    #   color is the color to fill the area containing the current node with
    def dfs(self, start_index, color):
        """
        Performs a DFS on the ImageGraph and prints it to command line
        Input: start_index: refers to the ColorNode to begin the search
               color: the color to change the node to after visiting
        """
        # reset visited status
        self.reset_visited()
        # print initial state
        print("Starting DFS; initial state:")
        self.print_image()

        stack = Stack()
        start_node = self.nodes[start_index]
        previous_color = start_node.color
        stack.push(start_node)

        while not stack.is_empty():
            current_node = stack.pop()
            if current_node.color == previous_color and not current_node.visited:
                current_node.visit_and_set_color(color)
                self.print_image()

            for neighbor_index in current_node.edges:
                neighbor = self.nodes[neighbor_index]
                if not neighbor.visited and neighbor.color == previous_color:
                    stack.push(neighbor)


def create_graph(data):
    """
    Creates an ImageGraph object from the read in data
    """
    data_list = data.split("\n")

    # get size of image, number of nodes
    image_size = int(data_list[0])
    node_count = int(data_list[1])

    graph = ImageGraph(image_size)

    index = 2

    # create nodes
    for _ in range(node_count):
        # node info has the format "x,y,color"
        node_info = data_list[index].split(",")
        new_node = ColorNode(len(graph.nodes), int(node_info[0]), int(node_info[1]), node_info[2])
        graph.nodes.append(new_node)
        index += 1

    # read edge count
    edge_count = int(data_list[index])
    index += 1

    # create edges between nodes
    for _ in range(edge_count):
        # edge info has the format "fromIndex,toIndex"
        edge_info = data_list[index].split(",")
        # connect node 1 to node 2 and the other way around
        graph.nodes[int(edge_info[0])].add_edge(int(edge_info[1]))
        graph.nodes[int(edge_info[1])].add_edge(int(edge_info[0]))
        index += 1

    # read search info
    search_info = data_list[index].split(",")
    search_start = int(search_info[0])
    search_color = search_info[1]

    return graph, search_start, search_color


def main():
    """Main function"""
    # read input
    data = sys.stdin.read()

    graph, search_start, search_color = create_graph(data)

    # print matrix
    graph.print_adjacency_matrix()

    # run bfs
    graph.bfs(search_start, search_color)

    # reset by creating graph again
    graph, search_start, search_color = create_graph(data)

    # run dfs
    graph.dfs(search_start, search_color)


if __name__ == "__main__":
    main()
