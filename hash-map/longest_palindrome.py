"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
"""


def longest_palindrome(s):
    frequency_map = {}
    odd_counter = 0

    for letter in s:
        if letter in frequency_map:
            frequency_map[letter] += 1
        else:
            frequency_map[letter] = 1

        if frequency_map[letter] % 2 == 1:
            odd_counter += 1
        else:
            odd_counter -= 1

    if odd_counter > 1:
        return len(s) - odd_counter + 1

    return len(s)


"""
idea:

- iterate through the string and keep a frequency map
- keep track of a variable odd_count
    - whenever the frequency of a given character is odd, increment the counter
    - whenever the frequency of the given character is even, decrement the counter
- if odd_count is greater than 1, we cannot use the entire string
    - remove all the odd frequency characters from the string (i.e. odd counter)
    - add 1 (because palindrome can be of odd length with pivot character in the middle)
- if odd_counter is 0, we can use the entire string
    - return len(s)

odd_count saves a pass for len(frequency_map) because we keep a static running total of characters to remove

time complexity:

- O(n) where `n` is the number of characters in the string
- hash map operations are amortized O(1)

space complexity:

- the dictionary is at most O(52) (uppercase and lowercase english letters)
    - using ascii characters this is O(128) at most
    - thus, the space complexity is O(1)
"""
