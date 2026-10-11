"""
LeetCode 102 - Binary Tree Level Order Traversal (BFS)

Given the root of a binary tree, return the level order traversal of its
nodes' values — i.e., from left to right, level by level.

Example:

      3
     / \\
    9  20
      /  \\
     15   7

 -> [[3], [9, 20], [15, 7]]

Constraints:

  * The number of nodes in the tree is in the range [0, 2000].
  * -1000 <= Node.val <= 1000

Approach - iterative BFS with a queue (see this folder's template.py):

  BFS visits nodes level by level: the queue always holds the "frontier"
  of the next level. To group values per level, snapshot the queue size at
  the top of each loop — that many pops make up exactly one level. Then
  enqueue every child's children before moving on to the next level.

  Contrast with yesterday's DFS version (LeetCode 104): DFS drills down a
  single path and combines answers on the way back up (O(h) stack space).
  BFS instead fans out level by level, which costs O(w) queue space where
  w is the widest level. Pick BFS whenever the question itself is about
  levels, distances, or "nearest" anything.

  Time: O(n) — every node is enqueued and dequeued exactly once.
  Space: O(w) — the queue holds at most one full level (the widest one);
  the output itself is O(n) but doesn't count as extra space.

"""

from collections import deque


class TreeNode:
    """Minimal binary tree node, matching LeetCode's shape."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    # Template step 0: an empty tree gives an empty answer.
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        # Snapshot: everything currently in the queue is exactly one level.
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            # Template step 1: pop the oldest node — next in level order.
            node = queue.popleft()
            # Template step 2: record this node's value for its level.
            level.append(node.val)
            # Template step 3: enqueue the children for a later level.
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        result.append(level)

    return result


def build_tree(values):
    """Build a tree from a level-order list (LeetCode's input style)."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        parent = queue.popleft()
        if parent is None:
            continue  # a missing slot has no children; consume nothing
        # The next two entries are this parent's left and right children.
        for side in ("left", "right"):
            if i < len(values):
                if values[i] is not None:
                    child = TreeNode(values[i])
                    setattr(parent, side, child)
                    queue.append(child)
                i += 1
    return root


if __name__ == "__main__":
    # Classic example from the problem statement.
    assert level_order(build_tree([3, 9, 20, None, None, 15, 7])) == [
        [3],
        [9, 20],
        [15, 7],
    ]
    # Single node and empty tree.
    assert level_order(build_tree([1])) == [[1]]
    assert level_order(build_tree([])) == []
    # Left-skewed tree: every level has exactly one node.
    assert level_order(build_tree([1, 2, None, 3])) == [[1], [2], [3]]
    # Full tree: level sizes double.
    assert level_order(build_tree([1, 2, 3, 4, 5, 6, 7])) == [
        [1],
        [2, 3],
        [4, 5, 6, 7],
    ]
    print("All sanity checks passed")
