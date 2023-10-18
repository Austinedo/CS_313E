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

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None
    # added this function to the stack class
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

class Node:
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree():
    def __init__ (self):
        self.root = None
    
    # this function takes in the input string expr and 
    # creates the expression tree
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

    # `create_tree` helper function
    # compares the order of operations for 2 operators
    # input: 2 operators
    # output: op1 <= op2 
    def operator_eval(self, op1, op2):
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


    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate(self, aNode):
        if aNode.data not in operators:
            return float(aNode.data)

        left = self.evaluate(aNode.lChild)
        right = self.evaluate(aNode.rChild)

        if aNode.data == '+':
            return left + right
        elif aNode.data == '-':
            return left - right
        elif aNode.data == '*':
            return left * right
        elif aNode.data == '/':
            return left / right
        elif aNode.data == '//':
            return left // right
        elif aNode.data == '%':
            return left % right
        elif aNode.data == '**':
            return left ** right

    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order(self, aNode):
        if aNode is None:
            return ''

        prefix_notation = ''
        prefix_notation += aNode.data + ' '
        prefix_notation += self.pre_order(aNode.lChild)
        prefix_notation += self.pre_order(aNode.rChild)
        return prefix_notation

    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):
        if aNode is None:
            return ''
        postfix_notation = ''
        postfix_notation += self.post_order(aNode.lChild)
        postfix_notation += self.post_order(aNode.rChild)
        postfix_notation += aNode.data + ' '
        return postfix_notation

# you should NOT need to touch main, everything should be handled for you
def main():
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
