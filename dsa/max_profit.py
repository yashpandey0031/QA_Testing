def max_profit_memory(prices):
  min_price = float('inf')
  max_profit = 0

  for price in prices:
    min_price = min(min_price, price)
    max_profit = max(max_profit, price - min_price)
  return max_profit


if __name__ == "__main__":
  prices = list(map(int, input("Enter stock prices separated by spaces: ").split()))
  print(max_profit_memory(prices))