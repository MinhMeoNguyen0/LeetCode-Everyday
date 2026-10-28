"""LeetCode 53 - Maximum Subarray (Dynamic Programming / Kadane's Algorithm)

Problem: Given an integer array `nums`, find the subarray with the largest
sum, and return its sum. The subarray must be contiguous (at least one
element).

Pattern: Dynamic Programming, in its Kadane's Algorithm form. This is the
1D DP case from this folder's template, compressed to O(1) space: the only
earlier answer we ever need is the best sum of a subarray *ending at the
previous position*.

The DP idea, in one sentence: for each position, the best subarray ending
there either starts fresh at that element, or extends the best subarray
ending just before it -- whichever is larger.

    dp[i] = max(nums[i], dp[i - 1] + nums[i])

We never need the whole dp array, only the previous value, so two rolling
variables (`current` and `best`) replace it. One left-to-right pass.

Time:  O(n) -- one pass over the array.
Space: O(1) -- two variables, no extra array.

Edge cases this handles:
  - All-negative input (e.g. [-3, -2, -1] -> -1): `best` starts at
    nums[0], not 0, so we never "choose" an empty subarray with sum 0.
  - Single element: the loop body never runs, answer is that element.
  - A large negative in the middle: `current` resets to nums[i] when
    extending would drag the sum below starting fresh.
"""


def max_sub_array(nums: list[int]) -> int:
    """Return the largest sum of any contiguous subarray of `nums`."""
    # `current` = best sum of a subarray ENDING at the previous position.
    # `best`    = best sum of a subarray ending ANYWHERE so far.
    # Starting both at nums[0] (not 0) is what makes all-negative
    # arrays work: the answer must be a real, non-empty subarray.
    current = best = nums[0]

    for x in nums[1:]:
        # Either start fresh at x, or extend the subarray ending before x.
        # Extending only wins when the previous subarray's sum is positive:
        # a negative `current` would only pull x down.
        current = max(x, current + x)
        # The best subarray overall may end here, or may have ended earlier.
        best = max(best, current)

    return best


if __name__ == "__main__":
    # Classic example: subarray [4, -1, 2, 1] sums to 6.
    assert max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    # Single element.
    assert max_sub_array([1]) == 1
    # All positive except one dip: the whole array is best.
    assert max_sub_array([5, 4, -1, 7, 8]) == 23
    # All negative: answer is the least-bad single element, NOT 0.
    assert max_sub_array([-3, -2, -1]) == -1
    assert max_sub_array([-2, -1]) == -1
    # A big negative resets the running subarray.
    assert max_sub_array([2, -100, 3, 4]) == 7
    print("All Maximum Subarray checks passed.")
