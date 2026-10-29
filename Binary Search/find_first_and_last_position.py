"""
LeetCode 34 - Find First and Last Position of Element in Sorted Array (Binary Search)

Given a sorted array of integers `nums` (non-decreasing order) and a
`target` value, return the starting and ending position of `target`
in the array. If `target` is not found, return [-1, -1].

Example:
    nums = [5, 7, 7, 8, 8, 10], target = 8  -> [3, 4]
    nums = [5, 7, 7, 8, 8, 10], target = 6  -> [-1, -1]
    nums = [], target = 0                   -> [-1, -1]

Constraints:
    * 0 <= len(nums) <= 10^5
    * -10^9 <= nums[i], target <= 10^9
    * nums is sorted in non-decreasing order

Pattern: BINARY SEARCH (boundary search, twice).
The array is sorted, so a target's occurrences form one contiguous
block. Finding that block is the same as finding its two boundaries:
  - the first index whose value is >= target  (lower bound)
  - the first index whose value is > target   (upper bound)
The answer is [lower_bound, upper_bound - 1] -- but only if the value
at lower_bound actually equals the target; otherwise the target is
absent and the answer is [-1, -1].

This reuses the lower_bound shape from this folder's template.py,
run twice with a different comparison. Each search halves the range,
so the whole thing stays O(log n). Note the two loop invariants:
  - lower_bound keeps `left` as "first index that could still be >=
    target" and runs while left < right, shrinking with right = mid
    (never mid - 1) so the candidate itself is never discarded.
  - The empty-array and not-found cases fall out naturally: the
    bounds check `left == len(nums) or nums[left] != target` catches
    both, with no special-casing needed beyond it.

Time: O(log n) -- two binary searches.
Space: O(1) extra.
"""


def _lower_bound(nums: list[int], target: int) -> int:
    """First index i with nums[i] >= target (or len(nums) if none)."""
    left, right = 0, len(nums)  # right is exclusive here
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1  # mid is too small, discard it and everything left
        else:
            right = mid  # mid could be the answer, keep it in range
    return left


def _upper_bound(nums: list[int], target: int) -> int:
    """First index i with nums[i] > target (or len(nums) if none)."""
    left, right = 0, len(nums)  # right is exclusive here
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] <= target:
            left = mid + 1  # mid is still <= target, move past it
        else:
            right = mid  # mid could be the answer, keep it in range
    return left


def search_range(nums: list[int], target: int) -> list[int]:
    """Return [first, last] positions of target in sorted nums, else [-1, -1]."""
    first = _lower_bound(nums, target)
    # If first ran off the end, or the value there isn't the target,
    # the target is absent -- the upper bound would be meaningless.
    if first == len(nums) or nums[first] != target:
        return [-1, -1]
    # The last occurrence is one before the first value greater than target.
    last = _upper_bound(nums, target) - 1
    return [first, last]


if __name__ == "__main__":
    assert search_range([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert search_range([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert search_range([], 0) == [-1, -1]
    assert search_range([1], 1) == [0, 0]
    assert search_range([1], 0) == [-1, -1]
    assert search_range([2, 2, 2], 2) == [0, 2]
    assert search_range([1, 2, 3, 4, 5], 5) == [4, 4]
    assert search_range([1, 2, 3, 4, 5], 1) == [0, 0]
    assert search_range([1, 3, 3, 3, 5], 3) == [1, 3]
    assert search_range([1, 2, 3], 0) == [-1, -1]
    assert search_range([1, 2, 3], 4) == [-1, -1]
    print("All tests passed.")
