"""
LeetCode 11 - Container With Most Water (Two Pointers)

You are given an integer array `height` of length n. There are n vertical
lines drawn such that the two endpoints of the i-th line are (i, 0) and
(i, height[i]). Find two lines that together with the x-axis form a
container that holds the most water. Return the maximum amount of water.

Example:
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7] -> 49
    (lines at index 1 and 8: width 7, height min(8, 7) = 7 -> 7 * 7 = 49)

Approach - two pointers, opposite ends:
    Start with the widest possible container (left = 0, right = n - 1).
    The area is width * min(height[left], height[right]). Every step
    shrinks the width by 1 no matter which pointer moves, so the only way
    to beat the current best is to find a taller bar — and a taller bar
    can only be hiding on the side of the shorter bar. Move the shorter
    side inward and keep the best area seen. O(n) time, O(1) extra space.
"""


def max_area(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    best = 0

    while left < right:
        # Current container: width times the shorter of the two bars.
        area = (right - left) * min(height[left], height[right])
        if area > best:
            best = area

        # Width shrinks either way, so a better area needs a taller bar.
        # Only the shorter side can possibly supply one.
        if height[left] < height[right]:
            left += 1   # Left bar is the bottleneck -> move it inward.
        else:
            right -= 1  # Right bar is the bottleneck (or tied) -> move it.

    return best


if __name__ == "__main__":
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    assert max_area([4, 3, 2, 1, 4]) == 16
    assert max_area([1, 2, 1]) == 2
    assert max_area([0, 0]) == 0
    print("All Container With Most Water checks passed.")
