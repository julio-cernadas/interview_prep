# EXPLANATION:
# This solution employs a "One Pass Dynamic Programming" strategy to solve LeetCode problem 121. By iterating through
# the array of stock prices, it keeps track of the minimum price encountered so far and calculates the potential profit
# by subtracting this minimum price from the current price. The maximum profit is continuously updated using the
# maximum of the current maximum profit and the potential profit.


def max_profit(prices):
    min_price = prices[0]  # Initialize the minimum price to the first day's price
    profit = 0  # Initialize the maximum profit to 0

    for price in prices:
        min_price = min(min_price, price)  # Update the minimum price if the current price is lower
        profit = max(profit, price - min_price)  # Update the maximum profit if the potential profit is higher

    return profit


data = [7, 1, 5, 3, 6, 4]
output = max_profit(data)
print(data)
