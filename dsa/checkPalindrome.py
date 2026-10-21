def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    return s == s[::-1]

def is_palindrome_two_pointer(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()

#     #shorthand for 
#     left = 0
#     right = len(s) - 1
    left, right = 0, len(s) - 1

    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    s= input("Enter a string: ")
    if is_palindrome(s):
        print(f'"{s}" is a palindrome.')
    else:
        print(f'"{s}" is not a palindrome.')

    if is_palindrome_two_pointer(s):
        print(f'"{s}" is a palindrome (two-pointer method).')
    else:
        print(f'"{s}" is not a palindrome (two-pointer method).')