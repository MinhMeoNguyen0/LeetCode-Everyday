"""
LeetCode 167 - Two Sum II: Input Array Is Sorted (Two Pointers)

Given a 1-indexed array `numbers` sorted in non-decreasing order, find two
numbers that add up to `target`. Return their indices (1-based).

Example:
    numbers = [2, 7, 11, 15], target = 9 -> [1, 2]

Approach - two pointers:
    Left pointer at the start, right pointer at the end. If the sum is too
    big, move the right pointer in; if too small, move the left pointer out.
    Works because the array is sorted. O(n) time, O(1) extra space.
"""


def two_sum_ii(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]  # LeetCode wants 1-based indices.
        if total > target:
            right -= 1  # Sum too big -> shrink from the right.
        else:
            left += 1  # Sum too small -> grow from the left.

    raise ValueError("No solution exists (input violates constraints)")


if __name__ == "__main__":
    assert two_sum_ii([2, 7, 11, 15], 9) == [1, 2]
    assert two_sum_ii([2, 3, 4], 6) == [1, 3]
    assert two_sum_ii([-1, 0], -1) == [1, 2]
    print("All Two Sum II checks passed.")
