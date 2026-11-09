"""
Template: Greedy

Copy this file as a starting point for any greedy problem in this folder.

When to use it:
  - A LOCAL choice that looks best right now never hurts the future:
    taking the biggest jump, the earliest finishing interval, the
    cheapest next step. If a choice can be swapped for the greedy one
    without making the answer worse, greedy is safe.
    Examples in this folder: Jump Game (furthest reach).
  - You only need ONE piece of running state (a max, a count, a
    deadline) — not a table of subproblems. If you need to remember
    many past decisions, that is Dynamic Programming instead.

The greedy proof habit: before coding, argue the EXCHANGE — "if the
optimal solution does something else at this step, I can swap in the
greedy choice and the solution stays valid." If you cannot make that
argument, do not trust greedy.

Runs in O(n) time and O(1) extra space for the scan below.
"""


def furthest_reach(nums):
    """Greedy scan: track the furthest index reachable so far.

    The pattern for Jump Game: walk left to right, keep `furthest`.
    If the current index is beyond `furthest`, you are stuck.
    Otherwise extend `furthest` and stop early once the goal is in reach.
    """
    furthest = 0
    for i, jump in enumerate(nums):
        if i > furthest:
            return -1  # stuck: position i is unreachable
        furthest = max(furthest, i + jump)
        # if furthest >= len(nums) - 1: goal reached, stop early
    return furthest


def greedy_scan(items):
    """Generic greedy shape: sort (if order matters), then take the
    best available choice at each step, updating one piece of state.
    """
    # 1. Sort by the greedy criterion (e.g. end time, size, value).
    #    items.sort(key=...)
    # 2. state = <initial value>
    # 3. for item in items:
    #        if <item is compatible with state>:
    #            take it; update state
    ...
