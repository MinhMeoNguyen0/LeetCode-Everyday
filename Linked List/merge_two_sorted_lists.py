"""
LeetCode 21 - Merge Two Sorted Lists (Linked List)

You are given the heads of two sorted linked lists `list1` and `list2`.
Merge the two lists into one sorted list by splicing together their nodes
(reuse the existing nodes, don't build new ones), and return the head of
the merged list.

Example:
    list1 = [1, 2, 4], list2 = [1, 3, 4]
    -> [1, 1, 2, 3, 4, 4]

Approach - dummy head + tail pointer (template skeleton #3: DUMMY HEAD):
    The awkward part of building a list by hand is the head: the first
    node has no "previous" to link from, so a naive loop needs a special
    case for it. The dummy-head trick kills the special case: create a
    throwaway node `dummy` before the real head, grow the result through
    `tail = dummy`, and return `dummy.next` at the end - the throwaway
    node's own value is never read.

    Walk both lists together. At each step the smaller head value wins:
    point `tail.next` at it, advance that list's pointer AND tail by one
    node. This is the same "zip merge" idea as merge step of merge sort -
    because both inputs are already sorted, the smaller of the two front
    nodes is guaranteed to be the next smallest remaining node.

    When one list runs out, just attach whatever is left of the other:
    it is already sorted, and every value in it is >= everything merged
    so far (otherwise its nodes would have been taken already). No need
    to walk it node by node.

    Each node is visited exactly once: O(n + m) time. Only the dummy node
    is new: O(1) extra space (we splice, we never copy nodes).

    Compare with this folder's Reverse Linked List (LC 206), which used
    skeleton #2 (prev / cur / nxt in-place reversal). Same folder, same
    no-indices awkwardness - different skeleton move.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1, list2):
    # Dummy head: a fixed anchor so appending never needs a "first node?"
    # special case. Its value is never read; the answer is dummy.next.
    dummy = ListNode(0)
    tail = dummy

    # Zip merge: the smaller front node always wins the next position.
    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1   # Take list1's head, keep the rest of list1
            list1 = list1.next  # attached via list1.next.
        else:
            tail.next = list2   # Take list2's head, keep the rest of list2
            list2 = list2.next  # attached via list2.next.
        tail = tail.next  # Tail always points at the last merged node.

    # One list is empty now. The remainder of the other is already sorted
    # and everything in it is >= what we merged, so attach it whole.
    tail.next = list1 if list1 else list2

    return dummy.next  # Skip the throwaway dummy node.


def _build(values):
    """Test helper: list -> linked list head (mirrors template.py's build)."""
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def _to_list(head):
    """Test helper: linked list head -> list (mirrors template.py's to_list)."""
    out = []
    cur = head
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out


if __name__ == "__main__":
    # LeetCode's example cases.
    assert _to_list(merge_two_lists(_build([1, 2, 4]), _build([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert _to_list(merge_two_lists(_build([]), _build([]))) == []
    assert _to_list(merge_two_lists(_build([]), _build([0]))) == [0]

    # Edge cases: one list empty, equal values everywhere, single nodes,
    # and interleaving (not just one list fully before the other).
    assert _to_list(merge_two_lists(_build([5]), _build([1, 2, 3]))) == [1, 2, 3, 5]
    assert _to_list(merge_two_lists(_build([1, 1, 1]), _build([1, 1]))) == [1, 1, 1, 1, 1]
    assert _to_list(merge_two_lists(_build([2]), _build([1]))) == [1, 2]
    assert _to_list(merge_two_lists(_build([-3, 0, 4]), _build([-5, -1, 2, 9]))) == [-5, -3, -1, 0, 2, 4, 9]

    # Nodes are spliced, not copied: result shares nodes with the inputs.
    a = _build([1, 2, 4])
    b = _build([1, 3, 4])
    merged = merge_two_lists(a, b)
    assert merged is a or merged.next is a  # head of merged comes from an input

    print("All Merge Two Sorted Lists sanity checks passed.")
