#!/usr/bin/env python3
"""
Design a stack that supports push, pop, top and retrieving the minimum element in
constant time.

Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.
"""
from typing import Dict, List, Optional, Set, Tuple


class MinStack:
    """Keep track of the current minimum at any given point. We can either:
    1. Store the current minimum alongside each value as it's added (stack of tuples)
    2. Create a second stack with the minimums (e.g. [4, 2, 3, 1, 5] -> [4, 2, 1]), and
    pop from it if we remove the minimum from the main stack.

    The second approach should theoretically use equal or less memory, as it will store
    up to n minimums for n inputs (≤ 2n), as opposed to exactly n minimums (2n).
    However, memory overheads for lists and tuples make this benefit unclear. I'm going
    to use tuples as we won't need a conditional to remove from second stack (cleaner).
    """

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        curr_minimum = self.getMin()
        next_minimum = min(val, curr_minimum if curr_minimum is not None else val)
        self.stack.append((val, next_minimum))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1][1]


class MinStackBrute:
    """Iterate over the stack to get the minimum. O(n) time complexity for getMin()."""

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)


class Test:
    def test(self):
        """Given test case from Leetcode."""
        ms = MinStack()
        ms.push(-2)
        ms.push(0)
        ms.push(-3)
        assert ms.getMin() == -3
        ms.pop()
        assert ms.top() == 0
        assert ms.getMin() == -2

    def test_zeroes(self):
        """Given test case from Leetcode with zeroes."""
        ms = MinStack()
        ms.push(0)
        ms.push(1)
        ms.push(0)
        assert ms.getMin() == 0
        ms.pop()
        assert ms.getMin() == 0
