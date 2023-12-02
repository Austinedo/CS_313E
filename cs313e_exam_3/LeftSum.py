#  File: LeftSum.py

#  Description: Get the left sum of the BST

#  Student Name: Austine Do

#  Student UT EID: ahd589

#  Course Name: CS 313E

#  Unique Number: 52590


import sys

class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty(self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size(self):
        return (len(self.queue))

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):
  def __init__ (self):
    self.root = None

  # insert data into the tree
  def insert (self, data):
    new_node = Node (data)

    if (self.root == None):
      self.root = new_node
      return
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (data < current.data):
          current = current.lchild
        else:
          current = current.rchild

      # found location now insert node
      if (data < parent.data):
        parent.lchild = new_node
      else:
        parent.rchild = new_node

  # ***There is no reason to change anything above this line***
  def get_height(self):
      if self.root is None:
         return 0
      
      height = 0
      queue = Queue()
      queue.enqueue(self.root)
      
      while not queue.is_empty():
          level_size = queue.size()
          for _ in range(level_size):
              node = queue.dequeue()
              if node.lchild:
                  queue.enqueue(node.lchild)
              if node.rchild:
                  queue.enqueue(node.rchild)
          height += 1
      
      return height

  def get_level(self, level):
      if self.root is None or level < 0:
          return []

      result = []
      queue = Queue()
      queue.enqueue((self.root, 0))

      while not queue.is_empty():
          node, current_level = queue.dequeue()

          if current_level == level:
              result.append(node.data)
          elif current_level > level:
              break

          if node.lchild:
              queue.enqueue((node.lchild, current_level + 1))
          if node.rchild:
              queue.enqueue((node.rchild, current_level + 1))

      return result

  # Returns an integer for the left sum of the BST
  def get_left_sum(self):
      left_sum = 0
      level = 0
      queue = Queue()
      queue.enqueue(self.root)

      while not queue.is_empty():
          level_size = queue.size()
          for i in range(level_size):
              node = queue.dequeue()
              if i == 0:
                  left_sum += node.data
              if node.lchild:
                  queue.enqueue(node.lchild)
              if node.rchild:
                  queue.enqueue(node.rchild)
          level += 1

      return left_sum

# ***There is no reason to change anything below this line***

def main():
    # Create tree
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree_input = list (map (int, line))    # converts elements into ints

    tree = Tree()
    for i in tree_input:
      tree.insert(i)

    print(tree.get_left_sum())

if __name__ == "__main__":
  main()
