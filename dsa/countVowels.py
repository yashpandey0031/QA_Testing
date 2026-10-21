def count_vowels(s):
  vowels = "aeiouAEIOU"
  count = 0
  for ch in s:
    if ch in vowels:
      count += 1
  return count


def vowel_frequency(s):
  
  freq = {}
  for ch in s.lower():
    if ch in 'aeiou':
      freq[ch] = freq.get(ch, 0) + 1
  return freq

if __name__ == "__main__":
  s = input("Enter a string: ")
  print(count_vowels(s))
  print(vowel_frequency(s))