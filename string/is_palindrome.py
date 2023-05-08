"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""


def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        # case 1: left is non-alphanumeric
        if not s[left].isalnum():
            left += 1
        # case 2: right is non-alphanumeric
        elif not s[right].isalnum():
            right -= 1
        # case 3: both are characters
        else:
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1

    return True


"""
idea:

there are several classical ways to solve this problem

recursion:

- if string is empty, return True
- if string has only one character, return True
- if string has more than one character
  - check if first and last characters are the same
  - if so, return True, otherwise return False

this isn't super clean since this variant of the question adds a lot of junk to the input so you need to skip non-alpha characters and also sanitize cases
time complexity: O(n) every character is only traversed once
space complexity: O(n) stack needs to keep track of every character

two pointers:

- use left and right pointers
- move pointers together from the opposite ends of the string until they cross
  - increment the pointer if it is invalid
  - for each pair, check if the character match
    - if they do not match, return False
    - if they do match, return True
- if the loop ends, return True

time complexity: O(n) every character is only traversed once
space complexity: O(1) no additional space needed as everything is done in place

intuition:

a palindrome is just a string that is read the same forwards and backwards
if we clone the string and reverse it and then compare, it should be exactly the same
(this is less straightforward since there is a lot of garbage in the string we need to sanitize)

- .lower() string
- sanitize string of non-alpha characters (can use regex or just simple pass)
- call .reverse()
- compare reverse and original

time complexity:
  - O(n) traverses all characters to do .lower()
  - O(n) to sanitize non-alpha characters or regex
  - O(n) for reverse
  - O(n) for comparison (worst-case traverses entire string and does not break)
    - in total = 4 * O(n) = O(n)

space complexity:
  - 2 * O(n) to store two instances of the string and compare
"""
