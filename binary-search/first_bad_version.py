"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
"""


def is_bad_version(version):
    print('i was called')
    # number is arbitrary
    return True if version == 4 else False


def first_bad_version(n):
    left = 1
    right = n
    result = 1

    while left <= right:
        # try the middle number
        mid = (left + right) // 2

        # if middle is not a bad version, first bad version must be in the latter half of the list
        # set pointers to [mid + 1, n]
        if not is_bad_version(mid):
            left = mid + 1
        # otherwise, it is in the first half of the list
        # set pointers to [1, mid - 1]
        else:
            right = mid - 1
            # set result to the "latest" bad version we saw
            result = mid

    return result


"""
idea:

see explanation for binary search. this is the exact same problem
"""
