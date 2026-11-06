"""
LeetCode 238 - Product of Array Except Self (Prefix Sum)

Given an integer array nums, return an array answer such that
answer[i] is equal to the product of all the elements of nums
except nums[i]. The product of any prefix or suffix of nums is
guaranteed to fit in a 32-bit integer. You must write an algorithm
that runs in O(n) time and without using the division operation.

Example:
    nums = [1, 2, 3, 4]  ->  [24, 12, 8, 6]
    nums = [-1, 1, 0, -3, 3]  ->  [0, 0, 9, 0, 0]

Constraints:
    * 2 <= nums.length <= 10^5
    * -30 <= nums[i] <= 30

Pattern: Prefix Sum -- more precisely, prefix and suffix PRODUCTS.
The answer for position i is just two pieces multiplied together:

    answer[i] = (product of everything LEFT of i)
              * (product of everything RIGHT of i)

So one left-to-right pass fills in the "product of everything left"
for each position, and one right-to-left pass multiplies in the
"product of everything right". No division needed, which matters
because a zero in nums would break a divide-by-total approach
(and dividing by zero is undefined anyway).

This is the same skeleton as this folder's template.py: build the
running product in one direction, then fold the other direction in.

Time: O(n) -- two linear passes over the array.
Space: O(1) extra -- the output array doesn't count, and besides it
we keep only two running-product variables.
"""


class Solution:
    def productExceptSelf(self, nums):
        """Return the product of all elements except self, for each i."""
        n = len(nums)
        answer = [1] * n

        # Pass 1 (template step 1): left-to-right. After this loop,
        # answer[i] holds the product of everything to the LEFT of i.
        # `prefix` is the running product of nums[0..i-1]; we store it
        # BEFORE multiplying in nums[i], so nums[i] itself is excluded.
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Pass 2 (template step 2): right-to-left. `suffix` is the running
        # product of everything to the RIGHT of i. Multiply it into the
        # answer we already stored, then fold nums[i] in for the next
        # position to the left.
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer


if __name__ == "__main__":
    sol = Solution()

    # Example from the problem statement.
    assert sol.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]

    # Example with a zero: only the position OF the zero gets a
    # non-zero answer (the product of everything else).
    assert sol.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]

    # Two elements: each answer is just the other element.
    assert sol.productExceptSelf([2, 3]) == [3, 2]

    # Two zeroes: every position's product includes a zero.
    assert sol.productExceptSelf([0, 0]) == [0, 0]

    # One zero: only the zero's own position escapes it.
    assert sol.productExceptSelf([0, 4, 5]) == [20, 0, 0]

    # Single element: product of "everything except it" is empty = 1.
    assert sol.productExceptSelf([5]) == [1]

    # Negatives: sign flips come along for free.
    assert sol.productExceptSelf([-2, -3, -4]) == [12, 8, 6]

    print("All checks passed.")
