"""
Template: Two Pointers

Copy this file as a starting point for any two-pointer problem in this folder.

When to use it:
  - OPPOSITE ENDS (left/right): the array is sorted (or can be sorted) and
    you need pairs with a target property.
    Examples in this folder: Two Sum II, 3Sum.
  - FAST/SLOW (same direction): partition or scan in one pass, where `slow`
    marks the boundary of the "kept" prefix.
    Examples: Remove Duplicates from Sorted Array, Move Zeroes.

Both run in O(n) time and O(1) extra space.
"""


def opposite_ends(arr: list[int]):
    """Left at the start, right at the end, move inward on a condition."""
    left, right = 0, len(arr) - 1
    while left < right:
        # 1. Evaluate the pair (arr[left], arr[right]).
        # 2. Condition met -> record the answer, move a pointer.
        # 3. Too big  -> right -= 1   (shrink from the right)
        #    Too small -> left += 1   (grow from the left)
        ...


def fast_slow(arr: list[int]):
    """`slow` = end of the kept prefix, `fast` = scanner."""
    slow = 0
    for fast in range(len(arr)):
        # if arr[fast] should be kept:
        #     arr[slow] = arr[fast]
        #     slow += 1
        ...
    return slow
