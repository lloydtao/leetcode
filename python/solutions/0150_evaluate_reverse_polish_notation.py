#!/usr/bin/env python3
"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, * and /. Each operand may be an integer or another
expression.

Division between two integers should truncate toward zero.

It is guaranteed that the input expression is always valid. It will always evaluate to
a result, and there will not be any division by zero operation.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """Create an evaluation stack. If the next token is a number, add it to the
        stack. If the next token is an operator, take the top two elements from the
        stack as its operands, evaluate it, and add the result to the stack. At the
        end, there should be a single value left in the stack. Return this value.

        Args:
            tokens (List[str]): RPN expression as a list of operators and integers

        Returns:
            int: Result after evaluating RPN expression
        """
        # Store potential operators
        operators = {"+", "-", "*", "/"}
        # Initialise stack for evaluation
        stack = []
        for token in tokens:
            # Token is an operator
            if token in operators:
                # Get top two integers from stack
                s2 = stack.pop()
                s1 = stack.pop()
                # Evaluate expression
                new = eval(str(s1) + token + str(s2))
                new = int(new)
                # Add result to stack
                stack.append(new)
            # Token is an integer
            else:
                # Add integer to stack
                stack.append(token)
        # Expression will evaluate to a single value left in stack
        return stack[0]


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [["2", "1", "+", "3", "*"]]
        expected = 9

        assert Solution().evalRPN(*case) == expected

    def test_division(self):
        """Given test case from Leetcode, with a division."""
        case = [["4", "13", "5", "/", "+"]]
        expected = 6

        assert Solution().evalRPN(*case) == expected

    def test_tiny_negative_division(self):
        """Given test case from Leetcode, with a tiny, negative division (6 / -132)."""
        case = [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]]
        expected = 22

        assert Solution().evalRPN(*case) == expected
