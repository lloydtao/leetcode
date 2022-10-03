#!/usr/bin/env python3
"""
Implement a first in first out (FIFO) queue using only two stacks. The implemented
queue should support all the functions of a normal queue (push, peek, pop, and empty).
"""
from typing import Dict, List, Optional, Set, Tuple


class MyQueue:
    def __init__(self):
        """Use two stacks: an input stack (s1) and an output stack (s2).
        Moving all items from the input to the output reverses their order.
        This effectively turns a stack into a queue, as FIFO turns to FILO.
        Therefore, when performing an operation:
        - If s2 is empty, move elements from s1 to s2.
        - If s2 has elements, treat these as the queue until s2 is empty."""
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        # Add items to input stack
        # (Don't worry about output stack until operation)
        self.s1.append(x)

    def pop(self) -> int:
        # Populate output stack if empty
        if not self.s2:
            for i in range(len(self.s1)):
                self.s2.append(self.s1.pop())
        # Pop top of output stack
        return self.s2.pop()

    def peek(self) -> int:
        # Populate output stack if empty
        if not self.s2:
            for i in range(len(self.s1)):
                self.s2.append(self.s1.pop())
        # Return top of output stack
        return self.s2[-1]

    def empty(self) -> bool:
        # Check if either list has elements
        return not (self.s1 or self.s2)


class Test:
    def test(self):
        """Test push, pop and peek"""
        # Initialise queue
        myQueue = MyQueue()

        # Test empty
        assert myQueue.empty() == True

        # Populate queue
        queue = range(0, 5)
        for n in queue:
            myQueue.push(n)

        # Test pop and peek
        assert myQueue.pop() == queue[0]
        assert myQueue.peek() == queue[1]
        assert myQueue.pop() == queue[1]
        assert myQueue.peek() == queue[2]

        # Test not empty
        assert myQueue.empty() == False
