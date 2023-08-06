def coin_change(coins, amount) -> int:
    if amount == 0:
        return 0

    hash_map = {}
    for target in range(min(coins), amount + 1):
        for coin in coins:
            if coin > target:
                continue

            if remaining := target - coin:
                if hash_map.get(remaining):
                    change = hash_map[remaining] + 1
                    curr = hash_map.get(target)
                    if not curr or (curr and change < curr):
                        hash_map[target] = change
            else:
                hash_map[target] = 1

    return hash_map.get(amount, -1)


data = [1, 2, 5]
output = coin_change(data, 11)
print(output)
