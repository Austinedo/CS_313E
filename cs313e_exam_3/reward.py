#  File: reward.py

#  Description: The ABC staff decides to find the minimum number of gifts as each customer's reward.
#  Student Name: Austine Do
#  Student UT EID: ahd589
#  Course Name: CS 313E
#  Unique Number: 52590

import sys

max_val = 1000


def getmin(prices, T):
# Add your code here!
	N = int(0.1 * T)
	table = [[0 for i in range(N + 1)] for i in range(len(prices) + 1)]
	
	for i in range(1, N + 1):
		table[0][i] = max_val
	
	for i in range(1, len(prices) + 1):
		for j in range(1, N + 1):
			if prices[i - 1] > j:
				table[i][j] = table[i - 1][j]
			else:
				table[i][j] = min(table[i - 1][j], table[i][j - prices[i - 1]] + 1)
	
	if table[i][j] == max_val:
		return -1
	
	return table[len(prices)][N]



if __name__ == "__main__":

	# Read input list of prices for each gift
	prices_str = sys.stdin.readline().split()
	prices = [ int(x) for x in prices_str ]

	# Read total price that the customer spends
	T = int(sys.stdin.readline())

	print(getmin(prices, T))
