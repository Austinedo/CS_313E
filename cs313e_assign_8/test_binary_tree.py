#  File: TestBinaryTree.py

#  Description: Binary Tree with extra functions

#  Student Name: Austine Do

#  Student UT EID: ahd589

#  Partner Name: Ahyeon Ko

#  Partner UT EID: ak42464

#  Course Name: CS 313E

#  Unique Number: 52590

#  Date Created: 10/22/23

#  Date Last Modified: 10/25/23

"""
Used for standard input and files
"""
import sys


class Node():
    """Class Node"""
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

    def print_node(self, level=0):
        if self.rchild != None:
            self.rchild.print_node(level + 1)

        print(' ' * 3 * level + '->', self.data)

        if self.lchild != None:
            self.lchild.print_node(level + 1)

    def get_height(self):
        """
        Returns the height of the entire tree
        """
        if self.lchild is not None and self.rchild is not None:
            return 1 + max(self.lchild.get_height(), self.rchild.get_height())
        elif self.lchild is not None:
            return 1 + self.lchild.get_height()
        elif self.rchild is not None:
            return 1 + self.rchild.get_height()
        else:
            return 1


class Tree():
    """Class Binary Search Tree"""
    def __init__(self):
        self.root = None

    def print(self, level=0):
        """
        Prints the binary search tree
        Including a level parameter changes the spacing
        """
        self.root.print_node(level)

    def get_height(self):
        """
        Returns the total height of the binary search tree
        """
        return self.root.get_height()

    def insert(self, data):
        """
        Inserts a Node with 'data' into the BST and validates the BST
        """
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        else:
            parent = self.root
            curr = self.root
            # finds location to insert new node
            while curr is not None:
                parent = curr
                if data < curr.data:
                    curr = curr.lchild
                else:
                    curr = curr.rchild
            # inserts new node based on comparision to parent node
            if data < parent.data:
                parent.lchild = new_node
            else:
                parent.rchild = new_node
            return

    def range(self):
        """
        Returns the range of the values in a BST of integers
        """
        if self.root is None:
            return None

        current = self.root
        # finding the max
        while current.rchild is not None:
            current = current.rchild
        max_value = current.data
        # finding the min
        current = self.root
        while current.lchild is not None:
            current = current.lchild
        min_value = current.data

        return max_value - min_value

    def get_level(self, level):
        """
        Returns a list of nodes at a given level from left to right
        """
        if self.root is None or level < 0:
            return []

        result = []
        queue = [(self.root, 0)]

        while queue:
            current_node, current_level = queue.pop(0)
            # if the current node is at the specified level then add to results
            if current_level == level:
                result.append(current_node)

            if current_node.lchild is not None:
                queue.append((current_node.lchild, current_level + 1))
            if current_node.rchild is not None:
                queue.append((current_node.rchild, current_level + 1))

        return result

    def left_side_view(self):
        """
        Returns the list of the nodes you see from the left side
        of a BST in order from top to bottom of tree
        """
        if self.root is None:
            return []

        result = []
        level = 0
        while level != self.root.get_height():
            current_level_list = self.get_level(level)
            result.append(current_level_list.pop(0).data)
            level += 1

        return result

    def sum_leaf_nodes_recursive(self, node):
        """
        Helper function for 'sum_leaf_nodes' that finds all
        the leaves in the tree recursively and returns the sum of the
        leaves
        """
        if node is None:
            return 0
        if node.lchild is None and node.rchild is None:
            return node.data

        return (self.sum_leaf_nodes_recursive(node.lchild) +
                self.sum_leaf_nodes_recursive(node.rchild))

    def sum_leaf_nodes(self):
        """
        Returns the sum of the values of all leaves in the tree
        """
        if self.root is None:
            return 0
        return self.sum_leaf_nodes_recursive(self.root)


def make_tree(data):
    """
    Constructs the BST with values from 'data'
    """
    tree = Tree()
    for value in data:
        tree.insert(value)
    return tree


# Develop your own main function or test cases to be able to develop.
# Our tests on the Gradescop will import your classes and call the methods.

def main():
    """
    Main function for testing BST class and functions in BST class
    """
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line)) 	# converts elements into ints
    tree1 = make_tree(tree1_input)
    tree1.print(tree1.get_height())

    print("Tree range is: ",   tree1.range())
    print("Tree left side view is: ", tree1.left_side_view())
    print("Sum of leaf nodes is: ", tree1.sum_leaf_nodes())
    print("##########################")

# Another Tree for test.
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line)) 	# converts elements into ints
    tree2 = make_tree(tree2_input)
    tree2.print(tree2.get_height())

    print("Tree range is: ",   tree2.range())
    print("Tree left side view is: ", tree2.left_side_view())
    print("Sum of leaf nodes is: ", tree2.sum_leaf_nodes())
    print("##########################")
# Another Tree
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line)) 	# converts elements into ints
    tree3 = make_tree(tree3_input)
    tree3.print(tree3.get_height())

    print("Tree range is: ",   tree3.range())
    print("Tree left side view is: ", tree3.left_side_view())
    print("Sum of leaf nodes is: ", tree3.sum_leaf_nodes())
    print("##########################")


if __name__ == "__main__":
    main()
