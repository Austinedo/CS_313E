"""
In-Class Activity 0 solution
Class: C S 313E: Elements of Software Engineering
Run:
python3 change_values.py < input.txt
3 1 0 3
"""

import math
import sys

def change_values(my_a: int, my_b: int, my_c: int, my_d: int):
    """Changes the values depending on ... """
    if my_b % 2 != 0:
        my_b, my_a = my_a, my_b

    try:
        if math.ceil(math.log2(my_c)) == math.floor(math.log2(my_c)):
            my_c, my_d = my_d, my_c
    except ValueError:
        pass

    if (my_a + my_b + my_c) == my_d:
        my_d = my_a

    return [my_a, my_b, my_c, my_d]

# You can add any helper function if needed.

def main():
    """A main function to read input data.
    No need to change this function
    But feel free to change this if needed.
    """
    data = sys.stdin.read()

    data_list = data.split('\n')
    data_list.remove('')
    data_list = [int(i) for i in data_list]

    # There are 4 values inside this list
    data_list_mutated = change_values(*data_list)
    print(*data_list_mutated)

if __name__ == '__main__':
    main()
