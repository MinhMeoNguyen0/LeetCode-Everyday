"""
Template: Backtracking

Copy this file as a starting point for any backtracking problem in this folder.

When to use it:
- The problem asks for ALL combinations / permutations / subsets / paths
  that satisfy a condition, not just one answer or a count. If you catch
  yourself thinking "try every choice and see", that is backtracking.
  Examples: Subsets, Permutations, Combination Sum, N-Queens, Word Search.

The shape is always the same three steps, in this order:
  1. CHOOSE  - add a candidate to the current path.
  2. EXPLORE - recurse to extend the path further.
  3. UN-CHOOSE (backtrack) - remove the candidate, restoring the exact
     state you had before step 1, so the next candidate starts clean.

Two shapes to know:
- EVERY NODE COUNTS (subsets, combinations): record the current path at
  every recursive call, not just at the leaves.
  Examples in this folder: Subsets.
- ONLY LEAVES COUNT (permutations, N-Queens): record the path only when
  it is complete (or when a constraint is fully satisfied).

Complexity is usually O(branches ^ depth) in the worst case, times the
cost of copying each answer. Pruning (skipping a branch early when it
cannot lead to a valid answer) is what keeps it fast in practice.
"""


def backtrack_template(candidates, path, result):
    """Generic skeleton: choose, explore, un-choose."""
    # 1. Base case: if the path is complete (or every node counts),
    #    record a COPY of it: result.append(path.copy())
    # 2. Otherwise, for each candidate still available:
    #        path.append(candidate)   # CHOOSE
    #        backtrack_template(...)  # EXPLORE
    #        path.pop()               # UN-CHOOSE (backtrack)
    ...
