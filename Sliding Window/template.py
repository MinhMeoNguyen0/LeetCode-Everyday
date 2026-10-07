"""
Template: Sliding Window

Copy this file as a starting point for any sliding-window problem in this folder.

When to use it:
- The problem asks about a CONTIGUOUS subarray/substring that optimizes or
  is constrained by something: longest, shortest, count, or max/min sum.

- FIXED window (size k is given): the window never changes size, it just
  slides. Add the incoming element, drop the outgoing one.

  Examples: Maximum Sum of k Consecutive Elements, find all anagrams of p in s.

- VARIABLE window: the window grows and shrinks on a condition. Expand `right`
  by default; shrink `left` while the window is invalid.

  Examples in this folder: Longest Substring Without Repeating Characters,
  Minimum Size Subarray Sum, Longest Repeating Character Replacement.

Both run in O(n) time: each element enters and leaves the window once.
Space is O(k) for the window's bookkeeping (dict/set/counter).
"""


def fixed_window(arr: list[int], k: int):
    """Window of fixed size k: add arr[right], subtract arr[left]."""
    # window_sum = sum(arr[:k])
    # best = window_sum
    # for right in range(k, len(arr)):
    #     window_sum += arr[right] - arr[right - k]
    #     best = max(best, window_sum)
    # return best
    ...


def variable_window(arr: list[int]):
    """Window grows/shrinks on a condition; each index moves at most n times."""
    left = 0
    # bookkeeping = {}  # e.g. char counts in the current window
    # for right in range(len(arr)):
    #     1. Expand: include arr[right] in the bookkeeping.
    #     2. While window is INVALID:
    #            remove arr[left] from the bookkeeping; left += 1
    #     3. Window is valid here -> update the answer.
    ...
