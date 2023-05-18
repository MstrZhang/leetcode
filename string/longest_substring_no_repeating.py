"""
Given a string s, find the length of the longest substring without repeating characters.
"""


def longest_substring(s):
    seen = {}
    start = 0
    result = 0

    for end in range(len(s)):
        # grow window if we haven't seen this character yet
        if s[end] not in seen:
            result = max(result, end - start + 1)
        # if we've seen this character already
        else:
            # case 1: seen character is outside of the window
            if seen[s[end]] < start:
                # continue
                result = max(result, end - start + 1)
            # case 2: seen character is inside of the window
            else:
                # move start pointer to the character 1 after the seen character
                start = seen[s[end]] + 1

        seen[s[end]] = end

    return result


"""
idea:

- use a sliding window to keep track of the longest substring
- move the end pointer towards the end of the string
    - if we haven't seen this character before:
        - update the max length
        - continue
    - if we have seen this character before:
        - if we saw this character inside the window:
            - move the start pointer to the character after the seen character
        - if we saw this character outside the window:
            - it doesn't affect the current maximum substring
            - continue


case 1: character is inside the window
(in this case, we need to shrink the window)

a       b       c       d       c       a       d
^                       ^       ^
start                   |       end
                        new start


case 2: character is outside of window
(in this case, the seen character doesn't affect the window; continue)

a       b       c       d       c       a       d
^                       ^               ^
|                       start           end
end


---

time complexity:

- O(n) to traverse through the string
- O(1) hash map operations to keep track of "seen"
    - total: O(n)

space complexity:

- in the worst case, the entire string is unique and the hash map is size O(n)
"""
