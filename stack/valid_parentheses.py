"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

OPENING_BRACKETS = "([{"
BRACKET_MAP = {
    ')': '(',
    '}': '{',
    ']': '['
}


def is_valid(s):
    stack = ""

    for bracket in s:
        if bracket in OPENING_BRACKETS:
            stack += bracket
        else:
            try:
                if stack[-1] != BRACKET_MAP[bracket]:
                    return False
                else:
                    stack = stack[:-1]
            except:
                return False

    return len(stack) == 0


if __name__ == "__main__":
    print(is_valid("()"))
    print(is_valid("()[]{}"))
    print(is_valid("(]"))


"""
idea:

- loop through array
- if you encounter an opening bracket:
  - accumulate the value in the stack
- if you encounter a closing bracket:
  - pop the stack
    - if the brackets match, continue
    - if the brackets do not match, return False
    - if you cannot pop the stack, return False
- return True only if the stack is empty

runtime complexity:

- looping through the array is O(n)
- adding and popping from stack is O(1)
- total runtime: O(n)

additional notes:

- the try/catch is very pythonic, can be replaced with a check to see if the stack is empty as an if/elif
- the check for OPENING_BRACKETS is a bit redundant
  - because we don't push closing brackets to stack, we can assume that we always push if it's not in the BRACKET_MAP
"""
