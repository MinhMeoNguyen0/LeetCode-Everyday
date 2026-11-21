"""
LeetCode 973 - K Closest Points to Origin (Heap)
https://leetcode.com/problems/k-closest-points-to-origin/

Problem: given a list of points [x, y] and an integer k, return the k
points closest to the origin (0, 0). Distance is Euclidean; the answer
may be returned in any order.

Pattern: Heap -- top-k with a max-heap of size k. Scan the points once,
keeping only the k closest seen so far. The heap root is always the
FARTHEST of the k kept, so each new point is judged against it: closer
than the root? Swap it in. Farther? Ignore it.

Why a heap and not a sort: sorting all n points costs O(n log n). The
heap never grows past k, so each step costs O(log k) and the whole scan
is O(n log k) -- a real win when k is much smaller than n. The trick is
Python's heapq is a MIN-heap, so we fake a max-heap by pushing NEGATED
distances: the root (-d) is then the largest distance among the kept k.

Why squared distance is enough: comparing sqrt(x^2 + y^2) gives the same
order as comparing x^2 + y^2 (sqrt is monotone), so skip the sqrt and
compare the squares directly -- cheaper and exact, no float error.

Complexity: O(n log k) time -- one heap push/pop per point, heap size k.
O(k) extra space -- the heap itself.

Edge cases to watch:
  - k == len(points): everything is kept, heap never evicts anyone.
  - Ties in distance: any k of the tied points is a valid answer, so
    don't overthink which one the heap keeps.
  - Points at the origin: distance 0, always kept.
  - The answer order does not matter -- but if a test compares lists
    directly, sort or compare as sets.
"""


import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # Max-heap of size k, stored as (-dist_squared, point).
        # The root is the farthest point among the k kept so far.
        max_heap: list[tuple[int, list[int]]] = []
        for x, y in points:
            dist = x * x + y * y  # squared distance -- same order, no sqrt
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-dist, [x, y]))
            elif dist < -max_heap[0][0]:
                # Closer than the farthest kept point: swap it in.
                heapq.heappushpop(max_heap, (-dist, [x, y]))
            # Else: farther than all k kept -- ignore it.
        return [point for _, point in max_heap]


if __name__ == "__main__":
    s = Solution()
    # Classic example: [-2, 2] (dist 8) beats [1, 3] (dist 10).
    assert s.kClosest([[1, 3], [-2, 2]], 1) == [[-2, 2]]
    # Two of three: [3, 3] (18) and [-2, 4] (20) beat [5, -1] (26).
    assert sorted(s.kClosest([[3, 3], [5, -1], [-2, 4]], 2)) == [[-2, 4], [3, 3]]
    # k == all points: everything comes back.
    assert sorted(s.kClosest([[1, 0], [0, 1]], 2)) == [[0, 1], [1, 0]]
    # Origin point is always kept.
    assert s.kClosest([[0, 0], [1, 1]], 1) == [[0, 0]]
    # Single point.
    assert s.kClosest([[2, -2]], 1) == [[2, -2]]
    print("LeetCode 973 - K Closest Points to Origin: all tests passed")
