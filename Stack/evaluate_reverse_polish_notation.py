"""
LeetCode 150 - Evaluate Reverse Polish Notation (Stack)

Given an array of strings `tokens` representing an arithmetic
expression in Reverse Polish Notation, evaluate it and return the
result as an integer.

In Reverse Polish Notation (postfix), operators come *after* their
operands, so there are no parentheses and no precedence rules to
worry about -- the order you read the tokens is the order you
evaluate them.

Example:
    tokens = ["2", "1", "+", "3", "*"]  -> 9
        ((2 + 1) * 3 = 9)
    tokens = ["4", "13", "5", "/", "+"]  -> 6
        (4 + (13 / 5) = 4 + 2 = 6)
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/",
              "*", "17", "+", "5", "+"]  -> 22

Constraints:
    * 1 <= len(tokens) <= 10^4
    * tokens[i] is an operator ("+", "-", "*", "/") or an integer
      in the range [-200, 200]
    * The expression is always valid, and division by zero never
      occurs. Division truncates toward zero.

Pattern: STACK.
A stack is the natural home for postfix evaluation because an
operator always applies to the two most recent values that have
not been consumed yet -- exactly what the top of a stack holds.
  - Number token: push it onto the stack (it is waiting for an
    operator to use it).
  - Operator token: pop the two most recent values, apply the
    operator, and push the result back -- it may itself be an
    operand for a later operator.
This reuses the stack shape from this folder's template.py: push
values as you go, pop when an operator (or a closing bracket, in
the template's case) forces a decision, and the answer is what is
left on the stack at the end -- here, the single remaining value.

One Python pitfall to watch: `//` floors toward negative infinity,
but the problem wants truncation toward zero. So -3 / 2 must be -1,
not -2. Computing with absolute values and re-applying the sign
gives truncation toward zero without floating-point rounding.

Time: O(n) -- each token is pushed and popped at most once.
Space: O(n) -- the stack holds at most the number of operands.
"""


def eval_rpn(tokens: list[str]) -> int:
    """Evaluate a Reverse Polish Notation expression."""
    stack: list[int] = []

    for token in tokens:
        if token in ("+", "-", "*", "/"):
            # Pop in reverse order: the second pop is the left operand.
            # E.g. for "10 6 -", b = 6, a = 10, so a - b = 4, not -4.
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            else:  # "/": truncate toward zero, not floor.
                quotient = abs(a) // abs(b)
                if (a < 0) != (b < 0):
                    quotient = -quotient
                stack.append(quotient)
        else:
            # A number token: it waits on the stack for its operator.
            stack.append(int(token))

    # A valid expression leaves exactly one value behind.
    return stack.pop()


if __name__ == "__main__":
    assert eval_rpn(["2", "1", "+", "3", "*"]) == 9
    assert eval_rpn(["4", "13", "5", "/", "+"]) == 6
    assert eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/",
                     "*", "17", "+", "5", "+"]) == 22
    # Division truncates toward zero, it does not floor.
    assert eval_rpn(["-3", "2", "/"]) == -1
    assert eval_rpn(["3", "-2", "/"]) == -1
    # Operand order matters for - and /.
    assert eval_rpn(["10", "6", "-"]) == 4
    assert eval_rpn(["42"]) == 42
    print("All tests passed.")
