# File: dna.py 

# Description : 

# Student Name: Austine Do

# Student UT EID: ahd589

# Partner Name: Ahyeon Ko

# Partner UT EID:

# Course Name: CS 313E

# Unique Number : 52590

# Date Created : 8/27/23

# Date Last Modified :

# Input : s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest # common subsequence. The list is empty if there are no
# common subsequences .

"""
# test file
3

GAAGGTCGAA
CCTCGGGA

ATGATGGAC
GTGATAAGGACCC

AAATTT
GGGCCC
"""


def longest_subsequence(string_1, string_2):
    """ADD YOUR CODE HERE """
    substrings = []
    temp_str = ''

    string_1.upper()
    string_2.upper()

    for i in range(len(string_1)):
        for j in range(len(string_2)):
            if string_1[i] == string_2[j]:
                pass

    return substrings



def main():
    """
    This main function reads the data input files and
    prints to the standard output. 
    NO NEED TO CHANGE THE MAIN FUNCTION.
    """

    # read the data
    # number of lines
    n_lines = int(input())

    # for each pair
    for _ in range(0, n_lines):
        str_1 = input()
        str_2 = input()

        # call longest_subsequence
        subsequences = longest_subsequence(str_1, str_2)

        # write out result(s)
        if not subsequences:
            print("No Common Sequence Found")

        for subsequence in subsequences:
            print(f"{subsequence}")

        # insert blank line
        print()


if __name__ == "__main__":
    main()
