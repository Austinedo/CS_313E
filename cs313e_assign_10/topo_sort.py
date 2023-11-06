"""
Topological Sort Implementation

  File: topo_sort.py
  Description: This program first checks if the given graph has a cycle
               in it and if does not then runs a topological sort on the
               given graph

  Student Name: Austine Do
  Student UT EID: ahd589

  Partner Name: Ahyeon Ko
  Partner UT EID: ak42464

  Course Name: CS 313E
  Unique Number: 52590
  Date Created: 11/4/23
  Date Last Modified: 11/8/23

"""

import sys

class Stack:
    """
    Stack class; you can use this for your search algorithms
    """
    def __init__(self):
        self.stack = []

    def push(self, item):
        """
        Add an item to the top of the stack
        """
        self.stack.append(item)

    def pop(self):
        """
        Remove an item from the top of the stack
        """
        return self.stack.pop()

    def peek(self):
        """
        Check the item on the top of the stack
        """
        return self.stack[-1]

    def is_empty(self):
        """
        Check if the stack if empty
        """
        return len(self.stack) == 0

    def size(self):
        """
        Return the number of elements in the stack
        """
        return len(self.stack)


class Queue:
    """
    Queue class; you can use this for your search algorithms
    """
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """
        Add an item to the end of the queue
        """
        self.queue.append(item)

    def dequeue(self):
        """
        Remove an item from the beginning of the queue
        """
        return self.queue.pop(0)

    def peek(self):
        """
        Checks the item at the top of the Queue
        """
        return self.queue[0]

    def is_empty(self):
        """
        Check if the queue is empty
        """
        return len(self.queue) == 0

    def size(self):
        """
        Return the size of the queue
        """
        return len(self.queue)

class Vertex:
    """Vertex Class"""
    def __init__(self, label):
        self.label = label
        self.visited = False

    def was_visited(self):
        """Determine if a vertex was visited"""
        return self.visited

    def get_label(self):
        """Determine the label of the vertex"""
        return self.label

    def __str__(self):
        """String representation of the vertex"""
        return str(self.label)


class Graph:
    """A Class to represent a Graph."""
    def __init__(self):
        self.vertices = []  # a list of vertex objects
        self.adj_mat = []  # adjacency matrix of edges

    def has_vertex(self, label):
        """Check if a vertex is already in the graph"""
        n_vert = len(self.vertices)
        for i in range(n_vert):
            if label == (self.vertices[i]).get_label():
                return True
        return False

    def get_index(self, label):
        """Given a label get the index of a vertex"""
        n_vert = len(self.vertices)
        for i in range(n_vert):
            if label == (self.vertices[i]).get_label():
                return i
        return -1

    def add_vertex(self, label):
        """Add a Vertex with a given label to the graph"""
        if self.has_vertex(label):
            return

        # add vertex to the list of vertices
        self.vertices.append(Vertex(label))

        # add a new column in the adjacency matrix
        n_vert = len(self.vertices)
        for i in range(n_vert - 1):
            (self.adj_mat[i]).append(0)

        # add a new row for the new vertex
        new_row = []
        for i in range(n_vert):
            new_row.append(0)
        self.adj_mat.append(new_row)


    def add_directed_edge(self, start, finish, weight=1):
        """Add weighted directed edge to graph"""
        self.adj_mat[start][finish] = weight

    def add_undirected_edge(self, start, finish, weight=1):
        """Add weighted undirected edge to graph"""
        self.adj_mat[start][finish] = weight
        self.adj_mat[finish][start] = weight

    def get_adj_unvisited_vertex(self, vertex):
        """Return an unvisited vertex adjacent to vertex v (index)"""
        for i in range(len(self.vertices)):
            if (self.adj_mat[vertex][i] > 0) and (
                    not (self.vertices[i]).was_visited()):
                return i
        return -1

    def get_adj_vertexes(self, vertex):
        """Return an adjacent vertex to vertex v (index)"""
        verts = []
        n_vert = len(self.vertices)
        for i in range(n_vert):
            if self.adj_mat[vertex][i] > 0:
                verts.append(i)
        return verts

    def get_adj_back_forth_vertex(self, vertex):
        """get back adj vertex."""
        verts = []
        n_vert = len(self.vertices)
        for i in range(n_vert):
            if (self.adj_mat[vertex][i] > 0) or (self.adj_mat[i][vertex] > 0):
                verts.append(i)
        return verts


    def dfs(self, vertex):
        """
        Do the depth first search in a graph from vertex v (index)
        and returns if the graph is cyclic (True) or acyclic (False)
        """
        # create the Stack
        the_stack = Stack()

        # cycle check
        cyclic = False

        # mark the vertex v as visited and push it on the stack
        self.vertices[vertex].visited = True
        # print(self.Vertices[v])
        the_stack.push(vertex)

        # visit the other vertices according to depth
        while (not the_stack.is_empty()) and not cyclic:
            # get an adjacent unvisited vertex
            adj_vertex_index = self.get_adj_unvisited_vertex(the_stack.peek())
            # print(u)
            # print(theStack.__str__())
            adjacents = self.get_adj_vertexes(adj_vertex_index)
            # print(adjacents)
            if vertex in adjacents:
                # print(v)
                final_adjacents = self.get_adj_back_forth_vertex(vertex)
                # print(final_adjacents)
                # print(u)
                if adj_vertex_index in final_adjacents:
                    cyclic = True
            if adj_vertex_index == -1:
                adj_vertex_index = the_stack.pop()
            else:
                (self.vertices[adj_vertex_index]).visited = True
                the_stack.push(adj_vertex_index)


        # the stack is empty, let us reset the flags
        for node in self.vertices:
            node.visited = False

        return cyclic
        # determine if a directed graph has a cycle
        # this function should return a boolean and not print the result

# COMPLETE THIS FUNCTION
    def has_cycle(self):
        """
        Determines if the graph has a cycle. If returns 'False' then
        the graph is a Directed Acyclic Graph (DAG)
        """
        # loops through all vertices in the graph to check if an
        # index is in a cycle
        for index in range(len(self.vertices)):
            if self.dfs(index):
                return True
        return False


    def bfs(self, vertex):
        """Do the breadth first search in a graph"""
        the_queue = Queue()

        (self.vertices[vertex]).visited = True
        print(self.vertices[vertex])
        the_queue.enqueue(vertex)

        # visit the other vertices according to depth
        while not the_queue.is_empty():
            # get an adjacent unvisited vertex
            adj_vertex_index = self.get_adj_unvisited_vertex(the_queue.peek())
            if adj_vertex_index == -1:
                adj_vertex_index = the_queue.dequeue()
            else:
                (self.vertices[adj_vertex_index]).visited = True
                print(self.vertices[adj_vertex_index])
                the_queue.enqueue(adj_vertex_index)

        # the stack is empty, let us reset the flags
        for node in self.vertices:
            node.visited = False

    def delete_edge(self, from_vertex_label, to_vertex_label):
        """
        Delete an edge from the adjacency matrix
        Delete a single edge if the graph is directed
        Delete two edges if the graph is undirected
        """
        start = self.get_index(from_vertex_label)
        finish = self.get_index(to_vertex_label)
        if self.adj_mat[start][finish] == self.adj_mat[finish][start]:
            self.adj_mat[start][finish] = 0
            self.adj_mat[finish][start] = 0
        else:
            self.adj_mat[start][finish] = 0

    def delete_vertex(self, vertex_label):
        """
        Delete a vertex from the vertex list and all edges from and
        to it in the adjacency matrix
        """

        idx = self.get_index(vertex_label)
        for row in self.adj_mat:
            row.pop(idx)
        self.adj_mat.pop(idx)
        self.vertices.pop(idx)

# COMPLETE THIS FUNCTION
    def toposort(self):
        """
        Return a list of vertices after a topological sort
        this function should not print the list
        """
        topo_list = []
        stack = Stack()

        # Find a valid topological ordering of the graph
        for index in range(len(self.vertices)):
            if not self.vertices[index].was_visited():
                self.vertices[index].visited = True
                self.toposort_dfs(index, stack)

        # the stack is in topological order (bottom is first vertex
        # in topological sort and top is last vertex in the topological
        # sort)
        while not stack.is_empty():
            topo_list.append(self.vertices[stack.pop()].get_label())

        # resets the 'visited' flag for all vertices in the graph
        for vertex in self.vertices:
            vertex.visited = False

        return topo_list

    def toposort_dfs(self, vertex, stack):
        """
        A helper function for toposort() that uses recursive DFS to perform
        the topological sort
        """
        # Note: the base case is when there are no adjacent vertices
        #       so the for loop won't run
        for adj_vertex in self.get_adj_vertexes(vertex):
            if not self.vertices[adj_vertex].was_visited():
                self.vertices[adj_vertex].visited = True
                self.toposort_dfs(adj_vertex, stack)
        stack.push(vertex)

    def get_index2(self, label, vertices_copy):
        """Given a label get the index of a vertex"""
        for i in range(len(vertices_copy)):
            if label == (vertices_copy[i]).get_label():
                return i
        return -1

    def delete_vertex2(self, vertex_label, adj_mat_copy, vertices_copy):
        """delete vertex """
        idx = self.get_index2(vertex_label, vertices_copy)
        # print(self.adjMat[0])
        # print(self.Vertices)
        for row in adj_mat_copy:
            row.pop(idx)
        adj_mat_copy.pop(idx)
        vertices_copy.pop(idx)


def main():
    """A main function to run a test."""
    # create a Graph object
    the_graph = Graph()

    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    num_vertices = int(line)

    # read the vertices and insert them into the graph
    for _ in range(num_vertices):
        line = sys.stdin.readline()
        vertex = line.strip()
        the_graph.add_vertex(vertex)

    # read the number of edges
    line = sys.stdin.readline()
    line = line.strip()
    num_edges = int(line)

    # read the edges and insert them into the graph
    for _ in range(num_edges):
        line = sys.stdin.readline()
        line = line.strip()
        edge = line.split()
        # print(edge)
        start = the_graph.get_index(edge[0])
        finish = the_graph.get_index(edge[1])
        # print(start, finish)

        the_graph.add_directed_edge(start, finish, 1)

    # print(num_edges)
    # test if a directed graph has a cycle
    if the_graph.has_cycle():
        print("The Graph has a cycle.")
    else:
        print("The Graph does not have a cycle.")

    # test topological sort
    if not the_graph.has_cycle():
        vertex_list = the_graph.toposort()
        print("\nList of vertices after toposort")
        print(vertex_list)

if __name__ == "__main__":
    main()
