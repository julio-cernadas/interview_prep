def max_profit(prices) -> int:
    unrealized_profit = 0
    realized_profit = 0

    buy_idx = 0
    sell_idx = 1
    while buy_idx < sell_idx < len(prices):
        profit = prices[sell_idx] - prices[buy_idx]
        if profit > unrealized_profit:
            unrealized_profit = profit

        if profit < unrealized_profit:
            buy_idx = sell_idx

            if unrealized_profit:
                realized_profit += unrealized_profit
                unrealized_profit = 0

        sell_idx += 1

    return realized_profit + unrealized_profit


data = [7, 1, 5, 3, 6, 4]
output = max_profit(data)
print(data)
