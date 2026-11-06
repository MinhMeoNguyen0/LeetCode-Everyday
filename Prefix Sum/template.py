"""
Template: Prefix Sum

Copy this file as a starting point for any prefix-sum problem in this
folder.

When to use it:
  - RANGE QUERIES: you need the sum (or product, or count) of many
    subarrays, fast. Precompute prefix[i] = aggregate of nums[0..i-1]
    once, then any range [l, r) is prefix[r] - prefix[l] in O(1).
    Examples: Range Sum Query, Subarray Sum Equals K.
  - LEFT/RIGHT SPLIT: the answer at position i depends on everything
    to its left AND everything to its right. Run one pass left to
    right building the left aggregate, then one pass right to left
    folding the right aggregate in.
    Examples in this folder: Product of Array Except Self.

Both patterns run in O(n) time. The prefix array costs O(n) extra
space; the two-pass split version can reuse the output array and
costs O(1) extra space.
"""


def prefix_sums(nums: list[int]) -> list[int]:
    """prefix[i] = sum of nums[0..i-1]; prefix[0] = 0 (empty prefix)."""
    prefix = [0] * (len(nums) + 1)
    for i, x in enumerate(nums):
        # 1. prefix[i + 1] extends prefix[i] by one element.
        prefix[i + 1] = prefix[i] + x
    return prefix


def range_sum(prefix: list[int], left: int, right: int) -> int:
    """Sum of nums[left..right] inclusive, from a prefix array."""
    # 2. Range [left, right] = prefix[right + 1] - prefix[left].
    return prefix[right + 1] - prefix[left]


def left_right_split(nums: list[int]):
    """answer[i] = (aggregate of everything left of i) combined with
    (aggregate of everything right of i)."""
    n = len(nums)
    answer = [1] * n  # identity element: 1 for products, 0 for sums

    # 3. Left-to-right pass: store the running left aggregate.
    running = 1  # identity element
    for i in range(n):
        answer[i] = running
        running = running * nums[i]  # combine nums[i] into the aggregate

    # 4. Right-to-left pass: fold the running right aggregate in.
    running = 1  # identity element
    for i in range(n - 1, -1, -1):
        answer[i] = answer[i] * running  # combine left and right
        running = running * nums[i]

    return answer
