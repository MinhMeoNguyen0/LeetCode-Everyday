"""
LeetCode 70 - Climbing Stairs (Dynamic Programming)

Problem: You are climbing a staircase. It takes n steps to reach the top.
Each time you can climb either 1 or 2 steps. In how many DISTINCT ways can
you climb to the top?

Example: n = 2 -> 2  (1+1, 2)
         n = 3 -> 3  (1+1+1, 1+2, 2+1)
         n = 5 -> 8

Constraints: 1 <= n <= 45

Pattern: DYNAMIC PROGRAMMING (1D, counting, optimal substructure).
Define ways[i] = the number of distinct ways to reach step i.
Consider how you ARRIVE at step i: your last move was either a 1-step from
i-1 or a 2-step from i-2. Every way to reach i ends with one of those two
moves, and the two groups don't overlap, so:
    ways[i] = ways[i-1] + ways[i-2]
That IS the whole problem — the staircase is Fibonacci in disguise.

Base cases: ways[0] = 1 (exactly one way to "be at the ground": take no
steps), ways[1] = 1 (only 1). Then fill upward; the answer is ways[n].

Space trick from template.py: ways[i] only needs the last two values, so
keep two rolling variables. O(n) time, O(1) space.

The trap: brute-force recursion enumerates every path and re-solves the
same sub-steps exponentially (2^n-ish). The DP insight is that ways[i-1]
and ways[i-2] never change once computed, so remember them and each i is
done once.
"""


def climb_stairs(n):
    """
    Bottom-up fill with two rolling variables.
    prev2 = ways[i-2], prev1 = ways[i-1]; answer for n is the last cur.
    Time: O(n). Space: O(1).
    """
    if n <= 1:
        return 1  # ways[0] and ways[1] are both 1

    prev2 = 1  # ways[0]: one way to stand on the ground
    prev1 = 1  # ways[1]: only "1"
    for _ in range(2, n + 1):
        cur = prev1 + prev2          # ways[i] = ways[i-1] + ways[i-2]
        prev2, prev1 = prev1, cur    # roll forward
    return prev1


if __name__ == "__main__":
    assert climb_stairs(1) == 1, "n=1"
    assert climb_stairs(2) == 2, "n=2"
    assert climb_stairs(3) == 3, "n=3"
    assert climb_stairs(4) == 5, "n=4"
    assert climb_stairs(5) == 8, "n=5"
    assert climb_stairs(10) == 89, "n=10"
    assert climb_stairs(45) == 1836311903, "n=45 (max constraint)"
    print("All Climbing Stairs sanity checks passed.")
