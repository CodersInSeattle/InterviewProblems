def max_profit(prices):
    if len(prices) < 2:
        return 0
    profit = 0
    smallest_so_far = float('inf')
    for price in prices:
        smallest_so_far = min(smallest_so_far, price)
        profit = max(profit, price-smallest_so_far)
    return profit
