#!/usr/bin/env python3
"""
You are given the `root` of a binary tree with unique valies, and an integer `start`. At
minute `0`, an infection starts from the node with value `start`.

Each minute, a node becomes infected if:

- The node is currently uninfected.
- The node is adjacent to an infected node.

Return the number of minutes needed for the entire tree to be infected.
"""
from typing import Dict, List, Optional, Set, Tuple

from .utils.binary_tree import TreeNode


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        """Convert the tree to a graph, which is required as infection can propogate
        back to parents. Then, traverse the graph to find the furthest away point (i.e.,
        largest depth of an unvisited node)."""
        # Initialise graph
        graph = {}
        # Add tree nodes to graph via breadth-first search
        queue = [root]
        for node in queue:
            # Add nodes to graph
            if node not in graph:
                graph[node] = {}
            if node.left:
                graph[node][node.left] = True
                if node.left not in graph:
                    graph[node.left] = {node: True}
                else:
                    graph[node.left][node] = True
                queue.append(node.left)
            if node.right:
                graph[node][node.right] = True
                if node.right not in graph:
                    graph[node.right] = {node: True}
                else:
                    graph[node.right][node] = True
                queue.append(node.right)
            # Check if infection start
            if node.val == start:
                # Replace value with actual node
                start = node

        # Initialise depth tracker
        max_depth = 0
        # Traverse graph via breadth-first search
        queue = [start]
        depth = {start: 0}
        visited = {}
        for node in queue:
            neighbours = graph[node]
            for neighbour in neighbours:
                if neighbour not in visited:
                    queue.append(neighbour)
                    depth[neighbour] = depth[node] + 1
                    max_depth = max(max_depth, depth[neighbour])
            visited[node] = True
        return max_depth


class Test:
    def test(self):
        """Given test case from Leetcode."""
        case = [TreeNode.list_to_node([1, 5, 3, None, 4, 10, 6, 9, 2]), 3]
        expected = 4

        assert Solution().amountOfTime(*case) == expected
