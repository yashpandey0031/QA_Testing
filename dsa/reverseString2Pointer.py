def reverse_two_pointer(s):
  chars = list(s)
  left = 0
  right = len(chars) - 1

  while left < right:
    chars[left], chars[right] = chars[right], chars[left]
    left += 1
    right -= 1

    #the reason we use ''.join(chars) is because the join() method is used to concatenate the elements of a list into a single string. In this case, we are joining the characters in the chars list to form the reversed string.
  return ''.join(chars)


#python specific approach simple shortcut
#what it does -> it just flipts the whole string and returns it. It is a slicing technique that takes the whole string and reverses it by using the step parameter of -1.
def reverse_pythonic(s):
  return s[::-1]

if __name__ == "__main__":
  s = input("Enter a string: ")
  print(reverse_two_pointer(s))
  print(reverse_pythonic(s))