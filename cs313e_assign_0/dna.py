"""
File: dna.py

Description : This program takes in strings that represent DNA strings and compares,
              finds, and returns the longest common subsequence(s) between the two
              given strands.

Student Name: Austine Do

Student UT EID: ahd589

Partner Name: Ahyeon Ko

Partner UT EID: ak42464

Course Name: CS 313E

Unique Number : 52590

Date Created : 8/27/23

Date Last Modified : 9/1/23

Input : s1 and s2 are two strings that represent strands of DNA
Output: returns a sorted list of substrings that are the longest #
        common subsequence. The list is empty if there are no
        common subsequences.

test file:
3

GAAGGTCGAA
CCTCGGGA

ATGATGGAC
GTGATAAGGACCC

AAATTT
GGGCCC
"""


def longest_subsequence(string_1, string_2):
    """
    Input: string_1 and string_2 are DNA strings to
           to be compared for the longest common
           subsequence(s)
    Output: returns a list of the longest common
            subseqence(s) found between string_1
            and string_2
    """
    substrings = []

    string_1.upper()
    string_2.upper()

    for i in range(len(string_1)):
        for j in range(len(string_2)):
            common_subsequence = ''
            k = 0
            while (i + k < len(string_1)
                        and j + k < len(string_2)
                        and string_1[i+k] == string_2[j+k]):
                common_subsequence += string_1[i+k]
                k += 1
            if len(common_subsequence) >= 3:
                substrings.append(common_subsequence)

    if len(substrings) == 0:
        return []

    longest_length_str = max(len(item) for item in substrings)
    substrings = [item for item in substrings if len(item) == longest_length_str]

    substrings.sort()

    return substrings

def remove_duplicates(substrings):
    """
    Input: a list of the longest common subsequence(s)
    Output: a list of the longest common subsequence(s)
            with duplicates removed from the list
    """
    if not substrings:
        return []

    duplicates_removed = set(substrings)
    duplicates_removed = list(duplicates_removed)
    duplicates_removed.sort()

    return duplicates_removed


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
        subsequences = remove_duplicates(subsequences)

        # write out result(s)
        if not subsequences:
            print("No Common Sequence Found")

        for subsequence in subsequences:
            print(f"{subsequence}")

        # insert blank line
        print()


if __name__ == "__main__":
    main()
