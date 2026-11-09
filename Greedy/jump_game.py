"""
LeetCode 55 - Jump Game (Greedy)

Problem: You are given an integer array nums. You are initially positioned
at the first index, and each element nums[i] is the maximum jump length
from that position. Return True if you can reach the last index, and
False otherwise.

Example: nums = [2, 3, 1, 1, 4] -> True  (jump 1 step to index 1, then
         3 steps to the last index)
         nums = [3, 2, 1, 0, 4] -> False (every path strands you at
         index 3, where the jump length is 0)

Constraints: 1 <= len(nums) <= 10^4, 0 <= nums[i] <= 10^5

Pattern: GREEDY (furthest reachable index).
Instead of trying every jump from every position (which is exponential),
keep ONE number: the furthest index you can reach so far. Walk i from
left to right:

  - If i is beyond the furthest index you can reach, you are stuck:
    you cannot even stand on i, so return False.
  - Otherwise, standing on i extends your reach to i + nums[i], so
    update furthest = max(furthest, i + nums[i]).
  - The moment furthest reaches (or passes) the last index, you win:
    return True.

Why is greedy safe here? You never need to remember WHICH jump got you
to a position — only HOW FAR you can get. Any jump that lands anywhere
up to `furthest` is available to you, so the exact path does not matter.
A position is reachable exactly when some earlier reachable position can
jump to it, and `furthest` is the running max of all those jumps. If the
furthest you can ever reach is short of the last index, no path exists;
if it reaches the end, a path exists (just follow the jumps that kept
extending `furthest`).

The trap: recursion / DFS from each index re-explores the same positions
over and over — O(2^n) without memoization. The greedy scan visits each
index once, because `furthest` is the only state that matters.

Time: O(n) — one pass. Space: O(1) — just the `furthest` counter.
"""


def can_jump(nums):
    """
    Greedy scan: track the furthest index reachable so far.
    Time: O(n). Space: O(1).
    """
    furthest = 0  # furthest index reachable from any position seen so far
    last = len(nums) - 1

    for i, jump in enumerate(nums):
        # i is beyond everything we can reach -> stranded, no path exists.
        if i > furthest:
            return False
        # Standing on i, we can now reach as far as i + jump.
        furthest = max(furthest, i + jump)
        # Early exit: the last index is within reach.
        if furthest >= last:
            return True

    # Loop ended without reaching the last index (only possible when
    # len(nums) == 1, where the loop returns True on i == 0 already).
    return True


if __name__ == "__main__":
    assert can_jump([2, 3, 1, 1, 4]) is True, "2 -> 1 -> end"
    assert can_jump([3, 2, 1, 0, 4]) is False, "stranded at index 3"
    assert can_jump([0]) is True, "already at the last index"
    assert can_jump([0, 1]) is False, "cannot leave index 0"
    assert can_jump([1, 0]) is True, "one jump to the end"
    assert can_jump([1, 1, 1, 1]) is True, "step by step"
    assert can_jump([2, 0, 0]) is True, "first jump clears the zeros"
    assert can_jump([1, 2, 0, 1]) is True, "jump over the zero"
    assert can_jump([5, 0, 0, 0, 0, 0]) is True, "one big jump"
    assert can_jump([1, 0, 2]) is False, "zero blocks the only path"
    print("All Jump Game sanity checks passed.")
