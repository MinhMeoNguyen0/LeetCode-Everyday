"""
Template: Linked List

Copy this file as a starting point for any singly-linked-list problem in
this folder.

When to use it:
  - The input is a singly linked list and you must inspect, rewire, or
    rebuild it: reversal, middle node, cycle detection, merging, removing
    the n-th node from the end.
    Examples in this folder: Reverse Linked List.

Why linked lists feel awkward:
  - No indices: you can't jump. Every step is through `.next`, so plan how
    to move pointers around a node you are about to detach.

Four skeleton moves every linked-list problem builds on:

1. TRAVERSAL - walk the list, look at each node:
   cur = head
   while cur:
       # use cur.val
       cur = cur.next

2. IN-PLACE REVERSAL (prev / cur / nxt):
   prev = None
   cur = head
   while cur:
       nxt = cur.next    # save the rest of the list BEFORE rewiring
       cur.next = prev   # flip this node's pointer backward
       prev = cur        # advance both
       cur = nxt
   return prev           # prev is the new head

3. DUMMY HEAD - when the head itself might change (delete/merge/insert):
   dummy = ListNode(0); dummy.next = head
   # do the work on dummy.next / tail ...
   return dummy.next

4. FAST / SLOW TWO POINTERS - cycle, middle node, nth-from-end:
   slow, fast = head, head
   while fast and fast.next:      # guard so fast.next.next never crashes
       slow = slow.next
       fast = fast.next.next
   # slow sits at the middle; fast at the end (or off the list)

Complexity: O(n) time for a single walk, O(1) extra space when rewiring
in place (no recursion), O(n) call-stack space for the recursive versions.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
