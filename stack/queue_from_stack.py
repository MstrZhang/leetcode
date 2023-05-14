"""
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
"""


class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self.peek()
        return self.out_stack.pop()

    def peek(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.stack_out[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack


"""
idea:

use two stacks (an in-stack and an out-stack)
in-stack takes input elements
out-stack reverses the in-stack to pop for queue operation

- push:
    - add elements to the in-stack
- pop:
    - use peek to fill the out-stack
    - pop the top of the out-stack
- peek:
    - if the out-stack is empty
        - pop every element from the in-stack to the out-stack
    - return the last element from the out-stack
- empty:
    - if both stacks are empty, the queue must be empty

time complexity:

- push, and empty are O(1) operations
- in the worst case, peek() is an O(n) operation
    - if the out-stack needs to be filled, the operation is O(n)
    - if the out-stack is already filled, the operation is O(1)
- in the worst case, pop() is an O(n) operation
    - if the out-stack needs to be filled, the operation is O(n)
    - if the out-stack is filled, the operation is O(1)

space complexity:

- every element is only ever in any given stack once
- thus, the total space of both stacks adds up to O(n) in the worst case
"""
