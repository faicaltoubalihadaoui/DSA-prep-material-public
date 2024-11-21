def min_coins(coins, amount):
    n = len(coins)
    coins.sort()

    res = 0
    for i in range(n - 1, -1, -1):
        if amount >= coins[i]:
            cnt = amount // coins[i]

            res += cnt

            amount -= cnt * coins[i]

        if amount == 0:
            break
    return res
