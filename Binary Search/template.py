"""
Template: Binary Search

Copy this file as a starting point for any binary search problem in this folder.

When to use it:
  - CLASSIC SEARCH (sorted array): the input is sorted and you need an exact
    target, an insertion position, or a boundary (first/last occurrence).
    Examples: Binary Search (LC 704), Find First and Last Position (LC 34).
  - ROTATED / UNBOUNDED: the array is sorted but rotated, or the boundary
    condition comes from a predicate, not a plain value comparison.
    Examples in this folder: Search in Rotated Sorted Array (LC 33).

The loop shape stays the same in all cases:
  1. Compute mid (avoid overflow habits from other languages: mid = lo + (hi - lo) // 2).
  2. Shrink ONE side with certainty: left = mid + 1 or right = mid - 1.
  3. Loop while left <= right (when mid itself can be the answer).

All variants run in O(log n) time and O(1) extra space.
"""


def classic_search(arr: list[int], target: int) -> int:
    """Plain binary search on a sorted array; returns the index or -1."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def lower_bound(arr: list[int], target: int) -> int:
    """First index whose value is >= target (insertion position)."""
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def predicate_search(lo: int, hi: int, is_bad) -> int:
    """Binary search over an integer RANGE for the first `bad` value,
    where `is_bad` is a monotonic predicate (False...False, True...True).
    Example: First Bad Version (LC 278)."""
    left, right = lo, hi
    while left < right:
        mid = (left + right) // 2
        if is_bad(mid):
            right = mid
        else:
            left = mid + 1
    return left
