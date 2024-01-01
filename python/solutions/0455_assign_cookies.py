#!/usr/bin/env python3
"""
Assume you are an awesome parents and want to give your children some cookies. But, you
should give each child at most one cookie.

Each child `i` has a greed factor `g[i]`, which is the minimum size of a cookie that the
child will be content with; and each cookie 'j' has a size `s[j]`. If `s[j] >= g[i]`, we
can assign the cookie `j` to the child `i`, and the child `i` will be content.

Your goal is to maximise the number of your content children and output the maximum
number.

For example:
- Input: g = [1,2,3], s = [1,1]
- Output: 1
- Explanation: The two cookies each have size 1, and only one child will be content with
a cookie of size 1. Therefore, the maximum number of content children is 1.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """The ideal matching strategy is to give a cookie to a child only if it cannot
        be given to a more greedy child. For example, with children of greed [1,2] and
        cookies of size [1,2], giving the cookie of size `2` to child of greed `1` would
        not be optimal as child of greed `2` will go without a cookie. We should start
        by attempting to give the smallest cookie `1` to the least greedy child `1`.

        In order to achieve this, we can start with two sorted lists. We attempt to give
        the first (smallest) cookie to the first (least greedy) child. If it's feasible,
        we move on to the next cookie and child (or terminate if we are at the final
        cookie or child), and increment our content children counter. If it's not
        feasible, we  move on to the next cookie, or terminate if we are at the final
        cookie or child.
        """
        # Sort lists
        children = sorted(g)
        cookies = sorted(s)
        # Initialise pointers
        p_children = 0
        p_cookies = 0
        # Initialise counter
        content_children = 0
        # Iterate over lists
        for _ in range(len(cookies)):
            # Terminate if out of cookies or children
            if p_children >= len(children) or p_cookies >= len(cookies):
                break
            # Check if child and cookie match
            if cookies[p_cookies] >= children[p_children]:
                # If match, increment counter and both pointers
                content_children += 1
                p_children += 1
                p_cookies += 1
            else:
                # If not match, increment cookie pointer
                p_cookies += 1
        # Return content children
        return content_children


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [[1, 2, 3], [1, 1]]
        expected = 1

        assert Solution().findContentChildren(*case) == expected

    def test_more_cookies_than_children(self):
        """Given test case from Leetcode, with more cookies than children."""
        case = [[1, 2], [1, 2, 3]]
        expected = 2

        assert Solution().findContentChildren(*case) == expected

    def test_larger_cookies_satisfy_kids(self):
        """Test case where only the larger cookies in the batch will satisfy the
        children. Catches failure due to early termination when the number of children
        is used as an iteration limit."""
        case = [[4, 5, 6], [1, 2, 3, 4, 5, 6]]
        expected = 3

        assert Solution().findContentChildren(*case) == expected
