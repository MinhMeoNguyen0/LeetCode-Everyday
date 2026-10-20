"""
LeetCode 153 - Find Minimum in Rotated Sorted Array (Binary Search)

Given a rotated sorted array `nums` with DISTINCT integers (originally sorted
in ascending order, then rotated some number of times), return the minimum
element. Must run in O(log n) time.

Example:
    nums = [4, 5, 6, 7, 0, 1, 2]
    -> 0

Constraints:
    * 1 <= len(nums) <= 5000
    * All values are distinct, in range [-5000, 5000].

Approach - binary search on "which half holds the minimum":
    The pivot (minimum) sits where the ascending run breaks. Comparing
    nums[mid] against nums[right] always tells us which half is unsorted:
      1. If nums[mid] > nums[right], the right half contains the break, so
         the minimum must be at mid+1 or later -> left = mid + 1.
      2. Otherwise the right half is still ascending, so the minimum is at
         mid or somewhere left of it -> right = mid.
    The loop invariant "the minimum is always in [left..right]" holds every
    step, and each step discards half the window. When left == right, that
    index IS the minimum. This is O(log n) time, O(1) extra space.

Relation to this folder's LC 33: same rotated-array idea, but instead of
comparing a target against a sorted half, we use the mid-vs-right
comparison to always move toward the pivot.
"""


def find_min(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1

    # Invariant: the minimum is always inside [left..right].
    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            # Right half holds the break -> minimum is right of mid.
            left = mid + 1
        else:
            # Right half is still ascending -> minimum is mid or left of it.
            right = mid

    return nums[left]


if __name__ == "__main__":
    # LeetCode's example cases - quick sanity check.
    assert find_min([3, 4, 5, 1, 2]) == 1
    assert find_min([4, 5, 6, 7, 0, 1, 2]) == 0
    assert find_min([11, 13, 15, 17]) == 11
    # Edge cases: single element, already sorted, rotation by n-1.
    assert find_min([1]) == 1
    assert find_min([1, 2]) == 1
    assert find_min([2, 1]) == 1
    assert find_min([5, 1, 2, 3, 4]) == 1
    assert find_min([2, 3, 4, 5, 1]) == 1
    print("All sanity checks passed.")
