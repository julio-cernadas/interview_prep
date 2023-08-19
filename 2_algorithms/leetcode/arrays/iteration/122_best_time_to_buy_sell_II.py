# EXPLANATION:
# It iterates through the prices array, and whenever a price increase is detected from the previous day, it adds the
# difference to the total profit. By allowing transactions on consecutive days, the code accumulates gains to maximize
# overall profit. The solution returns the total achievable profit from multiple buy-sell pairs.


def max_profit(prices) -> int:
    profit = 0
    for i in range(1, len(prices)):
        curr_profit = prices[i] - prices[i - 1]
        profit = max(profit, profit + curr_profit)

    return profit


data = [7, 1, 5, 3, 6, 4]
output = max_profit(data)
print(data)
