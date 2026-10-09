"""
LeetCode 20 - Valid Parentheses (Stack)

Given a string `s` containing just the characters '(', ')', '{', '}',
'[' and ']', determine if the input string is valid.

An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket.

Example:
    s = "()[]{}"
    -> True

    s = "(]"
    -> False

Constraints:
    * 1 <= len(s) <= 10^4
    * s consists of parentheses only: ()[]{}

Approach - stack of openers, match on every closer:
    1. Scan left to right. Push every OPENING bracket onto the stack; the
       stack's top is always the most recently opened, still-unclosed bracket.
    2. On a CLOSING bracket, pop the stack and check the popped opener is its
       pair. Two ways to fail: the stack is empty (closer with no opener), or
       the popped opener is the wrong type ("(]" or "[)").
    3. After the scan, the stack must be empty: any leftover opener was never
       closed (e.g. "(((").
    Each character is pushed and popped at most once, so this is O(n) time
    and O(n) space (the stack in the worst case, e.g. all openers).
"""
from typing import Optional


PAIRS = {")": "(", "]": "[", "}": "{"}


def is_valid(s: str) -> bool:
    stack: list[str] = []

    for ch in s:
        # Closer: must match the most recent unclosed opener.
        if ch in PAIRS:
            # No opener at all -> fail (e.g. ")(").
            if not stack or stack.pop() != PAIRS[ch]:
                return False
        # Opener: remember it; its match must come later.
        else:
            stack.append(ch)

    # Leftovers mean unclosed openers -> invalid (e.g. "(((").
    return not stack


def is_valid_typed(s: str) -> Optional[bool]:
    """Typed variant returning None for non-bracket input; True/False otherwise."""
    if any(ch not in "()[]{}" for ch in s):
        return None
    return is_valid(s)


if __name__ == "__main__":
    # LeetCode's example cases - quick sanity check.
    assert is_valid("()") is True
    assert is_valid("()[]{}") is True
    assert is_valid("(]") is False
    assert is_valid("([)]") is False
    assert is_valid("{[]}") is True
    # Edge cases: closer with no opener, unclosed opener, single bracket.
    assert is_valid(")()") is False
    assert is_valid("((") is False
    assert is_valid("]") is False
    assert is_valid("(){}}{") is False
    assert is_valid("(" * 10 + ")" * 10) is True
    assert is_valid_typed("()a") is None
    print("All sanity checks passed.")
