"""
LeetCode 143 - Reorder List (Linked List)

https://leetcode.com/problems/reorder-list/

Problem: Given the head of a singly linked list, reorder it to
L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...
You may not modify the values in the list's nodes, only the nodes
themselves -- relink the pointers, don't swap values.

Example: [1, 2, 3, 4] -> [1, 4, 2, 3]
         [1, 2, 3, 4, 5] -> [1, 5, 2, 4, 3]

Constraints: 1 <= n <= 5 * 10^4; -1000 <= Node.val <= 1000.

Pattern: Linked List -- three moves chained together, all from this
folder's template.py:

    1. Find the MIDDLE with FAST / SLOW TWO POINTERS (template
       move 4): fast moves two steps per slow step, so when fast
       runs off the end, slow sits at the middle node. Everything
       before slow is the first half, everything after it is the
       second half.

    2. REVERSE the second half IN PLACE (template reverse move):
       walk it with prev / cur / nxt and flip each pointer as you
       go. Reversing turns the second half from L(n/2+1) -> ... ->
       Ln into Ln -> ... -> L(n/2+1), which is exactly the order
       the answer needs those nodes in.

    3. MERGE the two halves by ALTERNATING one node from each:
       first, second, first, second... until the second half runs
       out. The first half is never longer than the second by more
       than one node, so the merge always ends cleanly.

Why three steps instead of something cleverer? The target order is
"first half forwards, second half backwards, interleaved". There is
no way to produce that with one pass -- you cannot know what Ln is
until you have walked to the end. Splitting at the middle and
reversing the second half converts the problem into a plain
alternating merge, and each step is a standard linked-list move
you already know from this folder.

Why reverse in place instead of collecting nodes in a list? A list
of nodes would make the merge trivial, but it costs O(n) extra
space. The in-place reversal keeps the whole solution at O(1)
extra space -- the only new pointers are prev / cur / nxt and the
merge temporaries.

Time: O(n) -- one pass to find the middle, one pass to reverse the
second half, one pass to merge. Three passes, still linear.
Space: O(1) -- a handful of pointers, no new nodes or arrays.

Edge cases to watch:
  - 0 or 1 node: nothing to reorder, return the head as-is. (The
    problem guarantees n >= 1, but the guard costs one line.)
  - 2 nodes: [1, 2] -> [1, 2], unchanged. The second half has one
    node, the merge does one splice and stops.
  - Even length: the first half keeps one extra node (the middle),
    e.g. [1, 2, 3, 4] splits into [1, 2, 3] and [4]. The merge
    still ends exactly when the second half runs out, and the
    leftover first-half tail (3) already points to None (the cut).
  - Odd length: the middle node stays at the end of the first half,
    e.g. [1, 2, 3, 4, 5] splits into [1, 2, 3] and [4, 5] ->
    reversed [5, 4] -> merged [1, 5, 2, 4, 3]. The middle node (3)
    is the last node of the answer, and its next is already None.
  - THE CUT: after finding the middle, set slow.next = None. If
    you forget this, the tail of the first half still points into
    the second half and the merge walks in a cycle forever.
  - During the merge, save first.next and second.next BEFORE
    rewiring either pointer -- each splice overwrites a pointer
    you still need for the next step.
"""


class ListNode:
    """Minimal singly-linked-list node, matching LeetCode's shape."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head):
        """Reorder the list in place; returns nothing (LeetCode style)."""
        if not head or not head.next:
            return

        # Step 1 -- find the middle (template move 4, fast/slow).
        # When fast runs off the end, slow is at the middle node.
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split into two halves. THE CUT: slow.next = None, or the
        # merge below cycles forever.
        second = slow.next
        slow.next = None

        # Step 2 -- reverse the second half in place.
        prev = None
        cur = second
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        second = prev  # head of the reversed second half

        # Step 3 -- merge by alternating one node from each half.
        # The first half is never longer than the second by more than
        # one node, so the loop ends exactly when second runs out and
        # the last first-half node's next is already None (the cut).
        first = head
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2


def build(values):
    """Helper for tests: list -> linked list head."""
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head):
    """Helper for tests: linked list head -> list."""
    out = []
    cur = head
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out


if __name__ == "__main__":
    sol = Solution()

    # Example 1 from the problem statement.
    head = build([1, 2, 3, 4])
    sol.reorderList(head)
    assert to_list(head) == [1, 4, 2, 3]

    # Example 2 from the problem statement (odd length).
    head = build([1, 2, 3, 4, 5])
    sol.reorderList(head)
    assert to_list(head) == [1, 5, 2, 4, 3]

    # Edge case: single node, unchanged.
    head = build([1])
    sol.reorderList(head)
    assert to_list(head) == [1]

    # Edge case: two nodes, unchanged.
    head = build([1, 2])
    sol.reorderList(head)
    assert to_list(head) == [1, 2]

    # Three nodes: middle node lands last.
    head = build([1, 2, 3])
    sol.reorderList(head)
    assert to_list(head) == [1, 3, 2]

    # Six nodes, even length.
    head = build([1, 2, 3, 4, 5, 6])
    sol.reorderList(head)
    assert to_list(head) == [1, 6, 2, 5, 3, 4]

    # Seven nodes with distinct values (catches off-by-one in split).
    head = build([10, 20, 30, 40, 50, 60, 70])
    sol.reorderList(head)
    assert to_list(head) == [10, 70, 20, 60, 30, 50, 40]

    print("All checks passed.")
