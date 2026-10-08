"""
LeetCode 33 - Search in Rotated Sorted Array (Binary Search)

Given a rotated sorted array `nums` with DISTINCT integers (originally sorted
in ascending order, then rotated some number of times) and an integer
`target`, return the index of `target` in `nums`, or -1 if it isn't there.

Example:
    nums   = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    -> 4

Constraints:
    * 1 <= len(nums) <= 5000
    * All values are distinct, in range [-10^4, 10^4].

Approach - binary search with one extra decision:
    In a rotated sorted array, at least ONE half of every mid-split is always
    sorted. That sorted half lets us decide with certainty:
      1. Find mid; if nums[mid] == target, done.
      2. If nums[left] <= nums[mid], the LEFT half is sorted: check whether
         target falls inside [nums[left], nums[mid]); if yes, search left,
         otherwise search right.
      3. Else the RIGHT half is sorted: check whether target falls inside
         (nums[mid], nums[right]]; if yes, search right, otherwise search left.
    One side is discarded each step, so this is O(log n) time, O(1) space.
"""


def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # The left half [left..mid] is sorted.
        if nums[left] <= nums[mid]:
            # Target inside the sorted half -> keep left, else go right.
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Otherwise the right half [mid..right] is sorted.
        else:
            # Target inside the sorted half -> keep right, else go left.
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


if __name__ == "__main__":
    # LeetCode's example cases - quick sanity check.
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search([1], 0) == -1
    # Edge cases: no rotation, rotation by 1, target at the pivot.
    assert search([1, 2, 3, 4, 5], 3) == 2
    assert search([2, 1], 1) == 1
    assert search([5, 1, 3], 5) == 0
    assert search([5, 1, 3], 3) == 2
    print("All sanity checks passed.")
