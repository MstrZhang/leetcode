"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""


def is_anagram(s, t):
    frequency_map = {}

    for letter in s:
        if letter in frequency_map:
            frequency_map[letter] += 1
        else:
            frequency_map[letter] = 1

    try:
        for letter in t:
            frequency_map[letter] -= 1
            if frequency_map[letter] < 0:
                return False
    except:
        return False

    return all(value == 0 for value in frequency_map.values())


"""
idea:

hash map:

- go through every character in the first string and add to the hash map
- go through every character in the second string:
  - if the character doesn't exist, return False
  - if the character does exist, decrement the counter
    - if the counter goes below 0, return False
- return True only if every value in the hash map is 0

time complexity:
  - O(n + m) to traverse through every element in s and t
    - `n` and `m` are the lengths of s and t
  - O(n) to traverse through the hash map
  - O(1) for hash map operations
  - total: O(n)

space complexity:
  - in the very worst case, the frequency map will be 26 characters long so space is O(26) => O(1)

alternative:
  - create two buckets of all 26 letters
  - traverse through s
    - increment per character seen
  - traverse through t
    - increment per character seen
  - both buckets should have the same frequency values
    - because buckets have a fixed length of 26 characters they are O(1) space complexity

---

intuition:

- sort both words
- compare both words
  - if they are the same they are anagrams
  - if they are different they are not anagrams

time complexity:
  - lower bound of comparison based sort is O(n * log(n))
  - O(n) to do a comparison between the two strings
    - `n` is the length of the shorter string (should be the same size if real anagrams)

space complexity:
  - depends on the sorting algorithm
    - if using an in-place algorithm, space is O(1)

---

meme answer:

- generate all permutations of s
- check if any of the permutations match t
  - if one matches, return True
  - if no matches, return False

time complexity:
  - permutation algorithm has run time of O(n * n!)
  - O(m) to compare with t to find a match
    - `m` is the number of permutation elements generated

space complexity:
  - you need to allocate O(n!) amount of space for all the permutations

"""
