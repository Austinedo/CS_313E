import sys

class Link:
    def __init__(self, data, next_link=None):
        self.data = data
        self.next = next_link

    def print_link_data(self):
        print(self.data)

    def __str__(self):
        return str(self.data) + '-->' + str(self.next)

class CircularList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_link = Link(data)
        

    def find(self, data):
        pass

    def delete(self, data):
        pass

    def delete_after(self, start, n):
        pass

    def __str__(self):
        pass

def main():
    # read number of soldiers
    line = sys.stdin.readline()
    line = line.strip()
    num_soldiers = int(line)

    # read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    start_counter = int(line)

    # read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int(line)

     # your code

if __name__ == '__main__':
    main()