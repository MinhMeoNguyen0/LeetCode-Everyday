"""
LeetCode 1 - Two Sum (Hash Map)

Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to `target`.

Example:
    nums   = [2, 7, 11, 15]
    target = 9
    -> [0, 1] because nums[0] + nums[1] == 2 + 7 == 9

Constraints:
    * 2 <= len(nums) <= 10^4
    * Exactly one valid answer exists.

Approach - one pass with a hash map:
    For each number, check whether its complement (target - number) has been
    seen before. Dict lookups are O(1), so the whole scan is O(n) time
    and O(n) extra space.
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}  # number -> its index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            # Found the pair: complement's index + current index.
            return [seen[complement], i]
        seen[num] = i

    raise ValueError("No solution exists (input violates constraints)")


if __name__ == "__main__":
    # LeetCode's example cases - quick sanity check.
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    print("All Two Sum checks passed.")
