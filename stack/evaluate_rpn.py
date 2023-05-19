"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

- The valid operators are '+', '-', '*', and '/'.
- Each operand may be an integer or another expression.
- The division between two integers always truncates toward zero.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse polish notation.
- The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""


def eval_rpn(tokens):
    operations = ['+', '-', '*', '/']
    stack = []

    for token in tokens:
        if token not in operations:
            stack.append(int(token))
        else:
            right, left = stack.pop(), stack.pop()

            if token == '+':
                stack.append(left + right)
            elif token == '-':
                stack.append(left - right)
            elif token == '*':
                stack.append(left * right)
            elif token == '/':
                stack.append(int(left / right))

    return stack[0]


"""
idea:

reverse polish notation works as follows:

- if we encounter an operator
    - use the previous two values as the operands
    - evaluate the operation
    - replace the 2 operands and the operator with the value
    - continue until there are no operators

to accomplish this, we can use a stack:

- iterate through tokens
- if the element is not an operator, add it to the stack
- if the element is an operator:
    - pop the last two values from the stack
        - IMPORTANT: since stack is LIFO, the right operator is first and the left operator is last in the pop
            - this matters for non-commutative operations like subtraction and division
    - evaluate the operation
    - push the result back into the stack
- return the stack at the end

python rounding:

- in python, numbers are rounded down (i.e. not towards zero)
    - to fix this, we can use a trick where we do float division first and then convert back to an int

time complexity:

- technically, the check to see if the character is an operator or not takes O(n)
    - this can be improved by explicitly checking for the specific operators which is O(1)
    - this doesn't however affect the overall time complexity
- stack operations are O(1)
- each element is visited once so the total time complexity is O(n)

space complexity:

- we need O(n) space to keep track of the stack
    - `n` represents the number of numbers in the input
    - operators will never enter the stack
"""
