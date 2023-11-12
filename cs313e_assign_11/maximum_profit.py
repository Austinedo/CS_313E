"""
  File: maximum_profit.py
  Description: This program uses a bottom-up dynamic programming
               technique to produce the maximum profit for a given
               investment amount, properties, property values, and
               annual percent return on properties.

  Student Name: Austine Do
  Student UT EID: ahd589

  Partner Name: Ahyeon Ko
  Partner UT EID: ak42464

  Course Name: CS 313E
  Unique Number: 52590
  Date Created: 11/11/23
  Date Last Modified: 11/12/23

"""
import sys

def max_investment_profit(total_money, num_houses, prices, percent_return):
    """
    Input: total_money (int) : Is the total money available to invest
           num_houses (int) : The total numver of houses available to invest in
           prices (list) : A list of house prices (in millions of $)
           percent_return (list) : A list of investment return percentages for
                                   each of the houses in `prices`
    Output: Returns the maximum profit possible for investing `total_money`
    """
    # Initialize DP table to store maximum profit for each budget and property
    dp_table = [[0] * (total_money + 1) for _ in range(num_houses + 1)]

    for i in range(1, num_houses + 1):
        for j in range(total_money + 1):
            if prices[i-1] <= j:
                dp_table[i][j] = max(dp_table[i-1][j],
                                     dp_table[i - 1][j - prices[i - 1]] + prices[i - 1] * (percent_return[i - 1] / 100))
            else:
                dp_table[i][j] = dp_table[i-1][j]

    return round(dp_table[num_houses][total_money], 2)


def main():
    """
    Main function
    """
# The first line is the amount of investment in million USD which is an integer number.
    line = sys.stdin.readline()
    line = line.strip()
    money = int(line)


# The second line includes an integer number which is the number of houses listed for sale.
    line = sys.stdin.readline()
    line = line.strip()
    num_houses = int(line)


# The third line is a list of house prices in million dollar
    line = sys.stdin.readline()
    line = line.strip()
    prices = line.split(",")
    prices = [int(value) for value in prices]

# read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    increase = line.split(",")
    increase = [int(value) for value in increase]


    result = max_investment_profit(money, num_houses, prices, increase)
    print(result)


if __name__ == '__main__':
    main()
