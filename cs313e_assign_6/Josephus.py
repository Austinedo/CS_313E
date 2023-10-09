"""Used for standard input and files"""
import sys

class Link:
    """Link Class for the Circularly Linked List"""
    def __init__(self, data, next_link=None):
        self.data = data
        self.next = next_link

    def print_link_data(self):
        '''
        Prints the data contained in the link
        '''
        print(self.data)

    def __str__(self):
        '''
        Returns the string representation of the Link
        '''
        return str(self.data)


class CircularList:
    """Circularly Linked List Class"""
    def __init__(self):
        self.head = None

    def insert(self, data):
        '''
        Inserts a new Link at the end of the list
        '''
        new_link = Link(data)

        if not self.head: # check if the list is empty
            self.head = new_link
            self.head.next = self.head # making it circular
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_link
            new_link.next = self.head # making it circular

    def find(self, data):
        '''
        Finds the data in the list and returns the Link
        that contains the data
        '''
        if not self.head: # check if the list is empty
            return None

        # loop to search the list
        current = self.head
        while True:
            if current.data == data:
                return current
            current = current.next
            # stop if we reach the head again
            if current == self.head:
                break

        return None

    def delete(self, data):
        '''
        Finds and deletes the Link containing the data, reconnects
        the appropriate Links, and returns the deleted Linked
        '''
        if not self.head: # check if the list is empty
            return None

        current = self.head
        previous = None

        while True:
            if current.data == data:
                # deleting in the middle of the list and reconnecting
                if previous:
                    previous.next = current.next
                # deleting at the head of the list and reconnecting
                elif previous and current == self.head:
                    previous.next = current.next
                    self.head = current.next
                else:
                    # if list is 1 element, deleting head
                    if current.next == self.head:
                        self.head = None
                    # searching for end of list, deleting, and reconnecting
                    else:
                        temp = self.head
                        while temp.next != self.head:
                            temp = temp.next
                        temp.next = self.head.next
                        self.head = self.head.next
                return current

            previous = current
            current = current.next
            if current == self.head:
                return None

    def delete_after(self, start, nth):
        '''
        Deletes the n-th Link starting from the given starting
        Link. Returns the data of the deleted Link AND returns
        the Link after the deleted Link
        '''
        if not self.head:
            return None, None

        current = self.head

        # finding the link with the 'start' value
        while True:
            if current.data == start: # if deleting from the start of the list
                break
            current = current.next
            if current == self.head: # if the starting value to delete from isn't found
                return None, None

        deleted_link = None
        deleted_link_next = None
        for _ in range(nth):
            deleted_link = current
            deleted_link_next = deleted_link.next
            current = current.next

        self.delete(deleted_link.data)

        return deleted_link.data, deleted_link_next

    def __str__(self):
        '''
        Returns the string representation of the Circularly
        Linked List
        '''
        if not self.head:
            return '[]'

        result = []
        current = self.head
        while True:
            result.append(current.data)
            current = current.next
            if current == self.head:
                break
        return str(result)

def main():
    """
    Main function
    """
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
    suicide_circle = CircularList()

    # append soldiers to the circle
    for i in range(num_soldiers):
        suicide_circle.insert(i+1)

    current = start_counter
    for _ in range(num_soldiers):
        killed, next_soldier = suicide_circle.delete_after(current, elim_num)
        print(killed)
        current = next_soldier.data


if __name__ == '__main__':
    main()
