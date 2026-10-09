"""
Template: Stack

Copy this file as a starting point for any stack problem in this folder.

When to use it:
  - You need LAST-IN, FIRST-OUT order: the most recently seen item is the
    next one to handle. Classic signals: matching delimiters (parentheses,
    braces), "nearest smaller/greater" problems, undo histories.
    Examples in this folder: Valid Parentheses.
  - MONOTONIC STACK (keep a sorted stack by pushing/popping): "next greater
    element", "daily temperatures", "largest rectangle in histogram".
  - EVALUATION: postfix/RPN expressions ("2 1 + 3 *") - push operands, pop
    two on every operator.

Both run in O(n) time; the stack holds at most O(n) items.
"""


def lifo_skeleton(items):
    """Push to remember, pop to match/undo: most recent item handled first."""
    stack = []
    for item in items:
        # if item should be remembered (opener, operand, not-yet-resolved):
        #     stack.append(item)
        # else:  # item resolves something already on the stack
        #     if not stack or <stack[-1] doesn't match item>:
        #         return failure
        #     stack.pop()
        ...
    return not stack  # leftovers mean something was never resolved


def monotonic_skeleton(arr, increasing=True):
    """Keep stack monotonic; pop while the new element breaks the order."""
    stack = []  # usually stores indices so you can look back at arr
    for i, x in enumerate(arr):
        # while stack and (arr[stack[-1]] < x if increasing else arr[stack[-1]] > x):
        #     j = stack.pop()
        #     # arr[j]'s "next greater/smaller" is x at index i
        ...
        stack.append(i)
    return stack
