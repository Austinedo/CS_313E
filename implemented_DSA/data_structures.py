
"""STACK CLASS"""
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop()
        return None
    
    def peek(self):
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def __str__(self):
        return str(self.stack)


"""QUEUE CLASS"""
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)


"""SINGULARLY LINKED LIST"""
class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next = next_node

    def print_node_data(self):
        print(self.data)

    def __str__(self):
        return str(self.data) + '-->' + str(self.next)

class SingularlyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_last(self, data):
        new_node = Node(data)
        current = self.head
        
        # checks if the LinkedList is empty
        if current == None:
            self.head = new_node
            return
        
        # finds the last node in the LinkedList
        while current.next != None:
            current = current.next
        current.next = new_node

    def find_node(self, data):
        current = self.head
        
        # checks if the LinkedList is empty
        if current == None:
            return None
        
        # searches until the end of the LinkedList
        while current.data != data:
            if current.next == None:
                return None
            current = current.next
        
        return current

    def delete_node(self, data):
        current = self.head
        previous = self.head

        # check if the LinkedList is empty
        if self.head == None:
            return None
        
        # loop through the LinkedList to find node
        while current.data != data:
            if current.next == None:
                return None
            
            previous, current = current, current.next

        # removing node from LL and repairing the links
        if current == self.head:
            self.head = 

def main():
    print('This is the data structures module')

if __name__ == '__main__':
    main()