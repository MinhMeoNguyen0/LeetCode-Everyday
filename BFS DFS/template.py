"""
Template: BFS / DFS

Copy this file as a starting point for any tree (or graph) traversal problem
in this folder.

When to use it:

- DFS (recursive): drill down one path at a time. Natural for questions
  about root-to-leaf paths, depths, or anything where "the answer is built
  from the children's answers" (post-order).

  Examples in this folder: Maximum Depth of Binary Tree.

- BFS (iterative, with a queue): sweep level by level. Natural for
  shortest-path-on-unweighted-graphs, level-order output, or "nearest X"
  style questions.

  Examples: Binary Tree Level Order Traversal, Number of Islands.

DFS costs O(n) time and O(h) extra space (the call stack follows the
height h). BFS costs O(n) time and O(w) extra space (the queue holds the
widest level w).

"""

from collections import deque


class TreeNode:
    """Minimal binary tree node, matching LeetCode's shape."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(root):
    """Recursive depth-first traversal skeleton."""

    # 1. Base case: nothing to do on an empty subtree.
    if root is None:
        ...
        return

    # 2. Do the work for THIS node (pre-order), or...
    ...

    # 3. Recurse into the children.
    dfs(root.left)
    dfs(root.right)

    # 4. ...combine the children's answers on the way back up (post-order).
    ...


def bfs(root):
    """Iterative breadth-first traversal skeleton using a queue."""

    if root is None:
        return

    queue = deque([root])

    while queue:
        # 1. Pop the oldest node; it is the next one in level order.
        node = queue.popleft()

        # 2. Do the work for THIS node.
        ...

        # 3. Enqueue its children for a later level.
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
