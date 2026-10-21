def fib_series_loop(n):
  series = []
  a,b = 0,1
  for _ in range(n):
    series.append(a)
    a,b=b,a+b #move the window forward
  return series

if __name__ == "__main__":
  n = int(input("Enter the number of terms: "))
  print(fib_series_loop(n))

#time complexity: O(n)
#space complexity: O(n)