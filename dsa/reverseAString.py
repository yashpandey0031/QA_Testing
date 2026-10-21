def reverse_loop(s):
  result = ""
  for ch in s:
    result = ch + result
  return result

if __name__ == "__main__":
  s = input("Enter a string: ")
  print(reverse_loop(s))