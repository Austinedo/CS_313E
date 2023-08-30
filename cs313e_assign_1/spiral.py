"""
  File: spiral.py
  Description: In this program we will be creating 2-D list
               that contains numbers that increment while
               spiraling outwards from the center of the 2-D
               list. This program will also calculate the sum
               of the sub-grid around a target value if said
               target value exists in the 2-D list.

  Student Name: Austine Do
  Student UT EID: ahd589

  Partner Name: Ahyeon Ko
  Partner UT EID: ak42464

  Course Name: CS 313E
  Unique Number: 52590
  Date Created: 8/26/23
  Date Last Modified: 8/29/23
"""

def create_spiral(dim):
    """
    Input: dim is an odd integer between 1 and 100
    Output: returns a 2-D list representing a spiral
    """
    spiral = [[0] * dim for i in range(dim)]

    center = dim // 2
    row, col = center, center

    current_num = 1
    direction_index = 0
    step_size = 1
    move_count = 0

    while current_num <= dim*dim:
        spiral[row][col] = current_num

        if direction_index == 0: # move right
            col += 1
        elif direction_index == 1: # move down
            row += 1
        elif direction_index == 2: # move left
            col -= 1
        elif direction_index == 3: # move up
            row -= 1

        current_num += 1
        move_count += 1

        if move_count == step_size:
            move_count = 0
            direction_index = (direction_index + 1) % 4
            if direction_index == 0 or direction_index == 2:
                step_size += 1

    return spiral

def sum_sub_grid(grid, val):
    """
    Input: grid a 2-D list containing a spiral of numbers
           val is a number within the range of numbers in
           the grid
    Output: sum_sub_grid returns the sum of the numbers
            (including val) surrounding the parameter val
            in the grid if val is out of bounds, returns 0
    """
    sub_grid_total = 0
    row, col = 0, 0

    if val not in range(1, len(grid) * len(grid) + 1):
        return 0 # this will return 0 if val is not found in the grid

    # finds the coordinates of the target value
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if val == grid[i][j]:
                row, col = i , j

    # sums the numbers adjacent to the target value
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if (0 <= i < len(grid)) and (0 <= j < len(grid)):
                sub_grid_total += grid[i][j]

    sub_grid_total -= val

    return sub_grid_total


def main():
    """
    A Main Function to read the data from input,
    run the program and print to the standard output.
    """

    # read the dimension of the grid and value from input file
    dim = int(input())

    # test that dimension is odd
    if dim % 2 == 0:
        dim += 1

    # create a 2-D list representing the spiral
    mat = create_spiral(dim)

    while True:
        try:
            sum_val = int(input())

            # find sum of adjacent terms
            adj_sum = sum_sub_grid(mat, sum_val)

            # print the sum
            print(adj_sum)
        except EOFError:
            break


if __name__ == "__main__":
    main()
