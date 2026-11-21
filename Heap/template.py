"""
Template: Heap

Copy this file as a starting point for any heap problem in this folder.

When to use it:
  - TOP-K (min-heap of size k): keep only the k largest (or k
    smallest, with a max-heap) elements of a stream. The root is
    always the kth element, so it is the answer or the threshold
    every new element is judged against.
    Examples in this folder: Kth Largest Element in an Array.
  - MERGE / SCHEDULING (min-heap as a priority queue): repeatedly
    take the smallest available item, process it, and push back its
    successor. The heap is the "what is next?" data structure.
    Examples: Merge K Sorted Lists, Task Scheduler.
  - K SMALLEST PAIRS / KTH SMALLEST (heap of candidates): start with
    the smallest candidate, pop it, and push its neighbours. Each
    pop is the next element in sorted order.
    Examples: Kth Smallest Element in a Sorted Matrix.

Python's heapq is a MIN-heap only. To get max-heap behaviour, push
negated values (-x) and negate again on the way out.

All heap operations on a heap of size m cost O(log m); peeking at
the root is O(1).
"""

import heapq


def top_k_largest(nums: list[int], k: int) -> list[int]:
    """Keep the k largest elements of nums in a min-heap of size k."""
    min_heap: list[int] = []
    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            heapq.heappushpop(min_heap, num)
    return min_heap


def top_k_smallest(nums: list[int], k: int) -> list[int]:
    """Keep the k smallest elements, using negated values as a max-heap."""
    max_heap: list[int] = []  # stores -x, so the root is the largest x
    for num in nums:
        if len(max_heap) < k:
            heapq.heappush(max_heap, -num)
        elif num < -max_heap[0]:
            heapq.heappushpop(max_heap, -num)
    return [-x for x in max_heap]
