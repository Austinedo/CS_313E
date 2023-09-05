"""
  File: spiral.py
  Description: 

  Student Name: Austine Do
  Student UT EID: ahd589

  Partner Name: Ahyeon Ko
  Partner UT EID: ak42464

  Course Name: CS 313E
  Unique Number: 52590
  Date Created: 9/3/23
  Date Last Modified: 9/6/23
"""

import sys


def merge_tuples(tuples_list):
    """
    Input: tuples_list is an unsorted list of tuples denoting intervals
    Output: a list of merged tuples sorted by the lower number of the
    interval
    """
    if not tuples_list:
        return []

    duplicate_of_tuples = sorted(tuples_list, key=lambda x: x[0]) # use sorted() instead of .sort()
    prev_len = len(duplicate_of_tuples)
    merged_list = []

    while duplicate_of_tuples:
        current_interval = duplicate_of_tuples.pop(0)
        # if the list is empty or the interval is not merge-able
        if not merged_list or current_interval[0] > merged_list[-1][1]:
            merged_list.append(current_interval)
        # merges the interval [ current_interval[0] <= merged_list[-1][1] ]
        else:
            merged_list[-1] = (merged_list[-1][0], max(current_interval[1], merged_list[-1][1]))

        if len(duplicate_of_tuples) == prev_len:
            break

        prev_len = len(tuples_list)

    return merged_list


def sort_by_interval_size(tuples_list):
    """
    Input: tuples_list is a list of tuples of denoting intervals
    Output: a list of tuples sorted by ascending order of the
    size of the interval if two intervals have the size then it will sort by the
    lower number in the interval
    """
    sorted_merged_list = sorted(tuples_list,
                                key=lambda interval: (interval[1]-interval[0], interval[0]))

    return sorted_merged_list


def main():
    """
    Open file intervals.in and read the data and create a list of tuples
    """
    sys.stdin.readline()

    tup_list = []
    tup_list = sys.stdin.readlines()

    tuples_list = []
    for m_tuple in tup_list:
        tup = m_tuple.split()
        tuples_list.append(tuple((int(tup[0]), int(tup[1]))))

    # merge the list of tuples
    merged = merge_tuples(tuples_list)

    # sort the list of tuples according to the size of the interval
    sorted_merge = sort_by_interval_size(merge_tuples(tuples_list))

    # write the output list of tuples from the two functions
    print(merged)
    print(sorted_merge)

if __name__ == "__main__":
    main()
