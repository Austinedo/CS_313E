#  File: giftcard.py

#  Description: The gift card is worth the amount of N dollars.
#				Mark has to use it all at once without any exchange possible.
#				He wants to maximize the value of the gift card by ordering many different types of dessert
#				in the cafe without duplicates. Most importantly, he wants to spend exactly the amount on the
#				gift card. Is this possible? What are the maximum different deserts he can order?

#  Student Name:

#  Student UT EID:

#  Course Name: CS 313E

#  Unique Number:

import sys


# Input: desert_list is a list which contents price of each desert (non-zero integers)
#		 N is the amount of the gift card
# Output: 6
#		  Return -1 if he can't find a way to order deserts in this way.
def max_giftcard_value(desert_list, total):
	sumsList = (summationList(desert_list,total))


def summationList(desert_list,total,p=[],sumsList=[]):
	s = sum(p)
	if s == total:
		sumsList.append(len(p))
	for x in range(len(desert_list)):
		n = 

	return sumsList


if __name__ == '__main__':

	desert_list_str = sys.stdin.readline().split()
	desert_list = [ int(x) for x in desert_list_str ]
	N = int(sys.stdin.readline())
	result = max_giftcard_value(desert_list, N)

	print(result)
