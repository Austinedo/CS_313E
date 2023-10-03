"""
  File: work.py
  Description: This program helps Chris find the minimum lines of code
               he needs to write in order to complete the program in
               the morning if after each time he drinks a cup of coffee
               he stays awake for a short amount of time and writes less
               lines of code

  Student Name: Austine Do
  Student UT EID: ahd589

  Partner Name: Ahyeon Ko
  Partner UT EID: ak42464

  Course Name: CS 313E
  Unique Number: 52590

  Date Created: 9/29/23
  Date Last Modified: 10/4/23
"""

import sys
import time


def sum_series(min_lines, productivity_factor, num_coffee=0):
    """
    Input: min_lines: an integer representing the minimum lines of code and
           productivity_factor: an integer representing the productivity factor
    Output: computes the sum of the series (v + v // k + v // k**2 + ...)
            and returns the sum of the series
    """
    if min_lines // (productivity_factor ** num_coffee) <= 0:
        return 0

    return ( min_lines // (productivity_factor ** num_coffee) +
            sum_series(min_lines, productivity_factor, num_coffee+1) )

def linear_search(total_lines, productivity_factor):
    """
    Input: total_lines: an integer representing the total number of lines of code
           productivity_factor: an integer representing the productivity factor
    Output: returns min_lines: the minimum lines of code to write using linear search
    """
    for min_lines in range(0, total_lines):
        if sum_series(min_lines, productivity_factor) >= total_lines:
            return min_lines
    return total_lines

def binary_search(total_lines, productivity_factor):
    """
    Input: total_lines: an integer representing the total number of lines of code
           productivity_factor an integer representing the productivity factor
    Output: returns result: the minimum lines of code to write using binary search
    """
    low, high = 1, total_lines
    result = 0

    while low <= high:
        mid = (low + high) // 2
        sum_current = sum_series(mid, productivity_factor)

        if sum_current >= total_lines:
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result


def main():
    """main function"""
  # read number of cases
    line = sys.stdin.readline()
    line = line.strip()
    num_cases = int(line)

    i = 0
    while i < num_cases:
        line = sys.stdin.readline()
        line = line.strip()
        inp = line.split()
        num_of_lines_code = int(inp[0])
        prod_factor = int(inp[1])

        start = time.time()
        print("Binary Search: " + str(binary_search(num_of_lines_code, prod_factor)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()

        start = time.time()
        print("Linear Search: " + str(linear_search(num_of_lines_code, prod_factor)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()
        print()
        i += 1

if __name__ == "__main__":
    main()
