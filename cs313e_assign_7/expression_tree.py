#  File: expressionTree.py

#  Description: creates an expression tree that represents a
#               mathematical expression from a valid infix
#               expression and provides operations

#  Student Name: Austine Do

#  Student UT EID: ahd589

#  Partner Name: Ahyeon Ko

#  Partner UT EID: ak42464

#  Course Name: CS 313E

#  Unique Number: 52590

#  Date Created: 10/15/23

#  Date Last Modified: 10/18/23

"""
Used for standard input and files
"""
import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack:
    """Class Stack"""
    def __init__(self):
        self.stack = []

    def push(self, data):
        """
        Pushes data onto the top of the stack
        """
        self.stack.append(data)

    def pop(self):
        """
        Removes and returns the data from top of the stack
        """
        if not self.is_empty():
            return self.stack.pop()
        return None
    # added this function to the stack class
    def peek(self):
        """
        Returns the data from top of the stack
        """
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        """
        Returns if the stack is empty
        """
        return len(self.stack) == 0

class Node:
    """Class Node"""
    def __init__ (self, data = None, l_child = None, r_child = None):
        self.data = data
        self.l_child = l_child
        self.r_child = r_child

class Tree:
    """Class Expression Tree"""
    def __init__ (self):
        self.root = None

    def create_tree (self, expr):
        """
        Input: a string mathematical expression
        Output: an expression tree
        """
        operator_stack = Stack() # stack only for parentheses and operators
        node_stack = Stack()     # stack for nodes (should only contain numbers)

        tokens = expr.split() # str -> list w/o space characters

        for token in tokens:
            # if the token is a number
            if token not in operators and token != '(' and token != ')':
                node_stack.push(Node(token))
            # if the token is an operator
            elif token in operators:
                while(not operator_stack.is_empty() and operator_stack.peek() in operators and
                    self.operator_eval(token, operator_stack.peek())):
                    right_node = node_stack.pop()
                    left_node = node_stack.pop()
                    operator = operator_stack.pop()
                    new_node = Node(operator, left_node, right_node)
                    node_stack.push(new_node)
                operator_stack.push(token)
            # if the token is a opening parentheses
            elif token == '(':
                operator_stack.push(token)
            # if the token is a closing parentheses
            elif token == ')':
                while operator_stack.peek() != '(':
                    right_node = node_stack.pop()
                    left_node = node_stack.pop()
                    operator = operator_stack.pop()
                    new_node = Node(operator, left_node, right_node)
                    node_stack.push(new_node)
                operator_stack.pop()

        # if there are operators remaining in the operator_stack
        while not operator_stack.is_empty():
            right_node = node_stack.pop()
            left_node = node_stack.pop()
            operator = operator_stack.pop()
            new_node = Node(operator, left_node, right_node)
            node_stack.push(new_node)

        self.root = node_stack.pop()

    def operator_eval(self, op1, op2):
        """
        Description: `create_tree` helper function
        Input: 2 operators
        Output: returns a boolean based on the order
                of operations of the 2 operators
        """
        order_of_operations = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '//': 2,
            '%': 2,
            '**': 3,
        }
        return order_of_operations[op1] <= order_of_operations[op2]

    def evaluate(self, node):
        """
        Input: Node in the tree
        Output: returns the value of the expression tree
        """
        if node.data not in operators:
            return float(node.data)

        left = self.evaluate(node.l_child)
        right = self.evaluate(node.r_child)

        expression = f'{left} {node.data} {right}'

        return float(eval(expression))

    def pre_order(self, node):
        """
        Returns the prefix order of the expression tree
        """
        if node is None:
            return ''

        prefix_notation = ''
        prefix_notation += node.data + ' '
        prefix_notation += self.pre_order(node.l_child)
        prefix_notation += self.pre_order(node.r_child)
        return prefix_notation

    def post_order(self, node):
        """
        Returns the postfix order of the expression
        """
        if node is None:
            return ''
        postfix_notation = ''
        postfix_notation += self.post_order(node.l_child)
        postfix_notation += self.post_order(node.r_child)
        postfix_notation += node.data + ' '
        return postfix_notation

# you should NOT need to touch main, everything should be handled for you
def main():
    """Main function"""
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()

    tree = Tree()
    tree.create_tree(expr)

    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()
