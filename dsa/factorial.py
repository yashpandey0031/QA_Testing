def fact_loop(n):
  if n < 0:
    return "factorial does not exist for negative numbers"
  result = 1
  for i in range(1, n + 1): #we use n + 1 because range is exclusive of the last number
    result *= i
  return result

if __name__ == "__main__":
  n = int(input("Enter a number: "))
  print(fact_loop(n))
#time complexity: O(n)
#space complexity: O(1)
