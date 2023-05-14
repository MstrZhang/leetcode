"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""


def ransom_note(ransomNote, magazine):
    frequency_map = {}

    for letter in magazine:
        if letter in frequency_map:
            frequency_map[letter] += 1
        else:
            frequency_map[letter] = 1

    for letter in ransomNote:
        if letter not in frequency_map:
            return False
        else:
            frequency_map[letter] -= 1
            if frequency_map[letter] < 0:
                return False

    return True


"""
idea:

- add every letter in magazine to a frequency map
- iterate through ransomNote and check the frequency map
    - if the letter is not in the frequency map, return False
    - if the letter underflows, return False
- return True if the iteration is successful

time complexity:

- hash map operations are all O(1)
- in the worst case, both magazine and ransomNote are iterated through:
    - O(a + b) where `a` and `b` are the lengths of magazine and ransomNote respectively
    - thus, results in O(n) time complexity

space complexity:

- hash map is at most the size of magazine
- thus, O(n) space complexity where `n` is the number of letters in magazine
"""
