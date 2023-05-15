"""
Given two binary strings a and b, return their sum as a binary string.
"""


def add_binary(a, b):
    carry = 0
    result = []

    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or carry:
        if i >= 0:
            carry += int(a[i])
            i -= 1
        if j >= 0:
            carry += int(b[j])
            j -= 1

        result.append(str(carry % 2))
        # carry = carry // 2
        carry //= 2

    return ''.join(reversed(result))


"""
idea:

- start at the end of both strings
- while we haven't reached the end:
    - decrement both pointers
    - store the sum of a[i] and b[j] into carry (i.e. do the addition operation)
    - add the modded result (this converts the current digit to binary)
    - divide the carry by 2 (this converts the carry digit to binary)
- once we have reached the end:
    - return the reversed result (since we added sums in reverse order)

time complexity:

- O(n) to traverse through the entire array
    - where `n` is the length of the longer array
- O(n) to reverse the final result
    - where `n` is the length of the final result
- overall, O(n)

space complexity:

- in the worst case we will have one extra digit
- this is still O(n)
"""
