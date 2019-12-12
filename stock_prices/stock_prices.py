#!/usr/bin/python

import argparse

# UNDERSTAND: What is the problem asking me to do?

# prices is an array of daily fluxating stock prices.
# the task is to buy at the lowest price, sell at the highest price
# which results the maximum profit.
# we essentially want to find the maximum difference
# between the smallest and largest prices in the list of prices, but we also have to make
# sure that the max profit is computed by subtracting some price by another price that comes before it;
# it can't come after it in the list of prices.

# PLAN: What steps will I take to solve the problem?
                                              #  (compare?)
#  current_min_price_so_far will hold min price and subtract it from 
# every value to the right index of [prices]. This highest value added to max_profit_so_far.
# find_max_profit recusively calls itself until
# find_max_profit_so_far with maximum profit is the correct answer 
def find_max_profit(prices):
    profit = 0
    print(prices)

    for i in range(0, len(prices) - 2):
        for x in range(i + 1, len(prices) - 1):
            if profit is 0 or prices[x] - prices[i] > profit:
                profit = prices[x] - prices[i]

        print(profit)


#   if len(prices) - 1:
#     current_min_price_so_far = []
#     max_profit_so_far = []

#     c = 0
#     p = 0

#     # find_max_profit(prices)

#     while p < len(prices) - 1:
#         print(prices[c])
#         if prices[p] < current_min_price_so_far[c]:
#             # Left half used
#             prices[p] = current_min_price_so_far[c]
#             p += 1
#             c += 1
#         # else:
#         #     arr[a] = right[r]
#         #     r += 1
#         # Move to next slot
#         p += 1

#     return prices

find_max_profit([10, 7, 5, 8, 11, 9])

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))