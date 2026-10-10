"""
LeetCode 104 - Maximum Depth of Binary Tree (DFS)

Given the root of a binary tree, return its maximum depth: the number of
nodes along the longest path from the root down to the farthest leaf.

Example:

      3
     / \\
    9  20
      /  \\
     15   7

 -> 3 (the path 3 -> 20 -> 15, or 3 -> 20 -> 7)

Constraints:

  * 0 <= number of nodes <= 10^4
  * -100 <= Node.val <= 100

Approach - recursive DFS (post-order):

  The depth of a node is 1 (itself) plus the deeper of its two children,
  and an empty subtree has depth 0. So: solve both children first, then
  combine with max() on the way back up — exactly the template's
  post-order step.

  Every node is visited once, so O(n) time. The call stack follows the
  longest root-to-leaf path, so O(h) extra space where h is the height
  (O(n) worst case on a skewed tree, O(log n) on a balanced one).

"""


class TreeNode:
    """Minimal binary tree node, matching LeetCode's shape."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    # Base case (template step 1): an empty subtree contributes no depth.
    if root is None:
        return 0

    # Template step 3+4: recurse into the children, then combine the
    # children's answers on the way back up (post-order).
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    return 1 + max(left_depth, right_depth)


def build_tree(values):
    """Build a tree from a level-order list (LeetCode's input style)."""
    from collections import deque

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
            if i >= len(values):
                break
            child = None if values[i] is None else TreeNode(values[i])
            setattr(parent, side, child)
            queue.append(child)
            i += 1
    return root


if __name__ == "__main__":
    # LeetCode's example cases - quick sanity check.
    assert max_depth(build_tree([3, 9, 20, None, None, 15, 7])) == 3
    assert max_depth(build_tree([1, None, 2])) == 2

    # Edge cases: empty tree, single node, skewed chain.
    assert max_depth(build_tree([])) == 0
    assert max_depth(build_tree([1])) == 1
    assert max_depth(build_tree([1, None, 2, None, 3])) == 3

    print("All Maximum Depth checks passed.")
