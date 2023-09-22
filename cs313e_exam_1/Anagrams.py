# File: Anagrams.py

# Description: A program to group strings into anagram families

# Student Name: Austine Do

# Student UT EID: ahd589

# Course Name: CS 313E

# Unique Number: 52590

# Output: True or False
def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    char_count_str1 = {}
    char_count_str2 = {}

    for char in str1:
        char_count_str1[char] = char_count_str1.get(char, 0) + 1
    for char in str2:
        char_count_str2[char] = char_count_str2.get(char, 0) + 1

    return char_count_str1 == char_count_str2

# Input: lst is a list of strings comprised of lowercase letters only
# Output: the number of anagram families formed by lst
def anagram_families(lst):
    anagram_families_dict = {}

    for word in lst:

        word_key = ''.join(sorted(word))

        if word_key in anagram_families_dict:
            anagram_families_dict[word_key].append(word)
        else:
            anagram_families_dict[word_key] = [word]

    return len(anagram_families_dict)

def main():
    # read the number of strings in the list
    num_strs = int(input())

    # add the input strings into a list
    lst = []
    for i in range(num_strs):
        lst += [input()]

    # compute the number of anagram families
    num_families = anagram_families(lst)

    # print the number of anagram families
    print(num_families)

if __name__ == "__main__":
    main()
