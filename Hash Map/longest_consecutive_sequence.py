"""
LeetCode 128 - Longest Consecutive Sequence (Hash Map)

Given an unsorted array of integers `nums`, return the length of the
longest consecutive elements sequence. The algorithm must run in
O(n) time.

Example:
    nums = [100, 4, 200, 1, 3, 2]  -> 4   (the sequence 1, 2, 3, 4)
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]  -> 9
    nums = []  -> 0

Constraints:
    * 0 <= len(nums) <= 10^5
    * -10^9 <= nums[i] <= 10^9

Pattern: HASH MAP -- specifically the SEEN-SET shape from this
folder's template.py, used in a slightly different way than Two Sum
or Valid Anagram.
Instead of counting frequencies or mapping a value to an index, the
set here answers one question in O(1): "is this number present?"
That membership test is the whole trick:

  1. Put every number in a set (duplicates collapse for free).
  2. A number can only be the *start* of a consecutive run if the
     number just below it is missing -- if num - 1 is in the set,
     then num is in the middle of some other run, and counting
     from here would just re-count work already done.
  3. So only count forward from true starts: while num + length
     is in the set, extend the run. Keep the best length seen.

Why this stays O(n) even though there is a nested loop: each number
is the start of a run at most once, and each number is visited as
part of a run at most once -- the inner while loop only runs for
starts, and a run's numbers are never re-scanned as starts (their
predecessor is present, so step 2 skips them). So every number is
touched a constant number of times overall, not once per element.

Compare with the tempting alternative: sorting first gives the
same answer, but sorting costs O(n log n), which breaks the
problem's O(n) requirement. The set buys the ordering back
without paying for a sort.

Time: O(n) -- one pass to build the set, and each number is
visited a constant number of times while counting runs.
Space: O(n) -- the set holds every distinct number.
"""


def longest_consecutive(nums: list[int]) -> int:
    """Return the length of the longest consecutive sequence in nums."""
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Only start counting at a run's first element. If num - 1
        # exists, this run was already counted from its real start.
        if num - 1 in num_set:
            continue

        # Count forward from this start.
        length = 1
        while num + length in num_set:
            length += 1

        longest = max(longest, length)

    return longest


if __name__ == "__main__":
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert longest_consecutive([]) == 0
    # Duplicates must not inflate the run length.
    assert longest_consecutive([1, 2, 2, 3, 3, 4]) == 4
    # A single element is a run of length 1; negatives work the same.
    assert longest_consecutive([42]) == 1
    assert longest_consecutive([-2, -1, 0, 5]) == 3
    # No consecutive pair at all.
    assert longest_consecutive([10, 30, 20]) == 1
    print("All tests passed.")
