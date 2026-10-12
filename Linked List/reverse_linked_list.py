"""
LeetCode 206 - Reverse Linked List (Linked List)

Given the head of a singly linked list, reverse the list, and return the
reversed list's head.

Example:
    1 -> 2 -> 3 -> 4 -> 5
    becomes
    5 -> 4 -> 3 -> 2 -> 1

Constraints:
    * The number of nodes is in the range [0, 5000].
    * -5000 <= Node.val <= 5000

Approach - in-place pointer rewiring (prev / cur / nxt):
    1. Walk the list with `cur`. For each node, save `nxt = cur.next` FIRST,
       because the very next step destroys that link.
    2. Flip the pointer: `cur.next = prev`. The node now points at the part
       of the list we already reversed instead of the part ahead of us.
    3. Advance: `prev = cur`, `cur = nxt`.
    4. When `cur` falls off the end, `prev` is the new head.

    The recursive version does the same thing in reverse: it reverses the
    tail first, then makes the old head the new tail (`head.next.next = head`
    and `head.next = None`).

Time: O(n) - each node visited once.
Space: O(1) for the iterative version (three pointers); O(n) call stack for
the recursive version.
"""
from template import ListNode, build, to_list


def reverse_list_iterative(head):
    prev = None
    cur = head
    while cur:
        # Grab the rest of the list before we cut this link.
        nxt = cur.next
        # Flip this node to point backward at the already-reversed part.
        cur.next = prev
        # Step both pointers forward.
        prev = cur
        cur = nxt
    # `prev` is the last node we flipped -> new head.
    return prev


def reverse_list_recursive(head):
    # Base case: empty list or last node - this node IS the new head.
    if not head or not head.next:
        return head
    # Reverse everything after head; new_head is the tail turned head.
    new_head = reverse_list_recursive(head.next)
    # The old tail's tail must now point back at head...
    head.next.next = head
    # ...and head becomes the new tail: it must point at nothing, or we'd
    # leave a cycle (1 -> 2 would become 2 -> 1 -> 2).
    head.next = None
    return new_head


if __name__ == "__main__":
    # Sanity checks run against the shared template helpers.
    assert to_list(reverse_list_iterative(build([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert to_list(reverse_list_recursive(build([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    # Edge cases: empty list, single node, two nodes.
    assert to_list(reverse_list_iterative(build([]))) == []
    assert to_list(reverse_list_recursive(build([]))) == []
    assert to_list(reverse_list_iterative(build([1]))) == [1]
    assert to_list(reverse_list_recursive(build([1]))) == [1]
    assert to_list(reverse_list_iterative(build([1, 2]))) == [2, 1]
    assert to_list(reverse_list_recursive(build([1, 2]))) == [2, 1]
    print("All sanity checks passed.")
