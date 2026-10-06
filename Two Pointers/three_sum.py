"""
LeetCode 15 - 3Sum (Two Pointers)

Given an integer array `nums`, return all unique triplets [a, b, c] such that
a + b + c == 0. The solution set must not contain duplicate triplets.

Example:
    nums = [-1, 0, 1, 2, -1, -4] -> [[-1, -1, 2], [-1, 0, 1]]

Approach - sort + two pointers:
    Sort the array first. Fix the first element of the triplet, then run a
    Two Sum II style two-pointer scan on the remainder looking for pairs
    that sum to the negation of the fixed element. Skip duplicates both for
    the fixed element and inside the scan. O(n^2) time, O(1) extra space
    (not counting the output list).
"""


def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result: list[list[int]] = []

    for i in range(len(nums) - 2):
        # Skip duplicate fixed elements -> no duplicate triplets.
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # Smallest possible sum already > 0 -> nothing left to find.
        if nums[i] > 0:
            break

        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                # Skip duplicates on both sides before moving on.
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1  # Need a bigger sum.
            else:
                right -= 1  # Need a smaller sum.

    return result


if __name__ == "__main__":
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum([0, 1, 1]) == []
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]
    print("All 3Sum checks passed.")
