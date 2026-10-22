"""
LeetCode 155 - Min Stack (Stack)

Design a stack that supports push, pop, top, and retrieving the minimum
element in constant time.

Implement the MinStack class:
    MinStack()   initializes the stack object.
    push(val)    pushes the element val onto the stack.
    pop()        removes the element on the top of the stack.
    top()        gets the top element of the stack.
    getMin()     retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

Example:
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    obj.getMin()   -> -3
    obj.pop()
    obj.top()      -> 0
    obj.getMin()   -> -2

Constraints:
    * -2**31 <= val <= 2**31 - 1
    * pop, top and getMin are always called on a non-empty stack.
    * At most 3 * 10**4 calls will be made in total.

Approach - remember the running minimum at every stack level:
    1. push/pop/top are trivially O(1) on a list. The hard one is getMin():
       once the current minimum is popped, a plain stack has forgotten it
       and would need an O(n) re-scan to find the next one.
    2. Trick: store (value, min_so_far) pairs. On push, the new minimum is
       min(val, previous top's min_so_far); on pop the pair comes off for
       free, automatically restoring the earlier minimum - exactly how a
       stack undoes history.
    3. Every operation touches only the top of the stack: O(1) time each.
       Space is O(n) for the pairs, which is unavoidable - you must remember
       one minimum per stack level to restore them on pop.
"""


class MinStack:
    def __init__(self):
        # Each entry is (value, min_so_far): the minimum of everything
        # in the stack up to and including this entry.
        self._stack: list[tuple[int, int]] = []

    def push(self, val: int) -> None:
        # New running minimum: either val itself, or the minimum that was
        # already on top. Empty stack -> val is the minimum by definition.
        current_min = val if not self._stack else min(val, self._stack[-1][1])
        self._stack.append((val, current_min))

    def pop(self) -> None:
        # LeetCode guarantees pop is only called on a non-empty stack.
        # The stored min_so_far of the entry below is restored automatically.
        self._stack.pop()

    def top(self) -> int:
        # LeetCode guarantees top is only called on a non-empty stack.
        return self._stack[-1][0]

    def getMin(self) -> int:
        # LeetCode guarantees getMin is only called on a non-empty stack.
        # The top entry's min_so_far IS the minimum of the whole stack.
        return self._stack[-1][1]


if __name__ == "__main__":
    # LeetCode's example case - quick sanity check.
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    assert ms.getMin() == -3
    ms.pop()
    assert ms.top() == 0
    assert ms.getMin() == -2

    # Edge cases: single element, duplicates of the minimum, negatives.
    ms2 = MinStack()
    ms2.push(5)
    assert ms2.getMin() == 5
    assert ms2.top() == 5
    ms2.pop()

    ms3 = MinStack()
    ms3.push(2)
    ms3.push(2)   # duplicate minimum pushed twice
    ms3.push(1)
    ms3.push(1)   # new minimum pushed twice
    assert ms3.getMin() == 1
    ms3.pop()     # pop one 1 -> minimum must STILL be 1
    assert ms3.getMin() == 1
    ms3.pop()     # pop the last 1 -> minimum restores to 2
    assert ms3.getMin() == 2
    assert ms3.top() == 2

    # Decreasing pushes: every push sets a new minimum.
    ms4 = MinStack()
    for v in (3, 2, 1, 0, -1):
        ms4.push(v)
        assert ms4.getMin() == v
    for v in (-1, 0, 1, 2, 3):
        assert ms4.top() == v
        ms4.pop()
    print("All sanity checks passed.")
