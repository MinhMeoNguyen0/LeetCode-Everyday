"""
LeetCode 78 - Subsets (Backtracking)

Problem: Given an integer array nums of unique elements, return all
possible subsets (the power set). The solution set must not contain
duplicate subsets, and subsets may be returned in any order.

Example: nums = [1, 2, 3] ->
    [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

Constraints: 1 <= nums.length <= 10, all elements unique, -10 <= nums[i] <= 10.

Pattern: BACKTRACKING (build candidates one choice at a time)
- At each step we face a binary choice for nums[i]: TAKE it or SKIP it.
- We walk a decision tree: depth = index i, and every node on the path
  is itself a valid subset, so we record the current path at EVERY node,
  not just at the leaves (this is the key difference from problems like
  permutations, where only full-length leaves count).
- "Backtrack" means: after exploring the branch that takes nums[i], we
  undo that choice (pop it off the path) so the skip-branch starts from
  the same clean state. Forgetting the pop is the classic bug here:
  the path would keep growing and later subsets would wrongly contain
  elements from earlier branches.
- Because the input elements are unique, no duplicate subsets can arise
  and no extra de-duplication step is needed.

Time:  O(n * 2^n) — there are 2^n subsets, and copying each one into the
       answer costs up to O(n).
Space: O(n) for the recursion stack and the current path, plus O(n * 2^n)
       for the output itself (which any correct solution must produce).
"""


def subsets(nums: list[int]) -> list[list[int]]:
    """
    Return all subsets of nums.

    Time:  O(n * 2^n) — 2^n subsets, each copied in O(n).
    Space: O(n) extra (recursion + current path), excluding the output.
    """
    result: list[list[int]] = []
    current: list[int] = []  # the subset built along the current path

    def backtrack(i: int) -> None:
        # Every node is a valid subset, so record the path as it stands.
        # Copy it: appending `current` itself would let later pops mutate
        # subsets already stored in result.
        result.append(current.copy())

        # Try extending the subset with each remaining element.
        for j in range(i, len(nums)):
            current.append(nums[j])   # CHOOSE nums[j]
            backtrack(j + 1)           # EXPLORE with it included
            current.pop()              # UN-CHOOSE (backtrack): restore state

    backtrack(0)
    return result


if __name__ == "__main__":
    # Example from the problem statement: 2^3 = 8 subsets.
    assert sorted(map(sorted, subsets([1, 2, 3]))) == sorted(
        [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    )
    # Single element: the empty set plus the element itself.
    assert sorted(subsets([0])) == [[], [0]]
    # Empty input: only the empty subset.
    assert subsets([]) == [[]]
    # Count check: n = 4 must give exactly 2^4 = 16 subsets, all unique.
    four = subsets([1, 2, 3, 4])
    assert len(four) == 16 and len({tuple(s) for s in four}) == 16
    print("All sanity checks passed.")
