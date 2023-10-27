#  File: toomany.py

#  Description: Each flower has to be inserted into one of the vases.
#				She wants to arrange the flower so that no more than two flowers of the same type
#				will be inserted in the same vase.
#				She wants to find out which type of flower will be left after her arrangement.

#  Student Name: Austine Do

#  Student UT EID: ahd589

#  Course Name: CS 313E

#  Unique Number: 52590

import sys


# Input: flower_list is a list of integers that represent the flower type.
#		 N is the number of vases
# Output: is a list of flower types that Jennifer bought too many (sorted)
def findTooMany(flower_list, N):
	flower_counts = {}
	for flower in flower_list:
		if flower in flower_counts:
			flower_counts[flower] += 1
		else:
			flower_counts[flower] = 1
	
	too_many_flowers = []
	for flower, count in flower_counts.items():
		if count > N * 2:
			too_many_flowers.append(flower)

	return sorted(too_many_flowers)


if __name__ == '__main__':

	# Read flower_list
	flower_list_str = sys.stdin.readline().split()
	flower_list = [ int(x) for x in flower_list_str ]

	# N: number of vases
	N = int(sys.stdin.readline())

	# output list of flower types. sorted.
	item_too_many_ls = findTooMany(flower_list, N)

	print(item_too_many_ls)
