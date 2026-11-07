"""
LeetCode 322 - Coin Change (Dynamic Programming)

Problem: You are given coins of different denominations and a total amount
of money. Compute the FEWEST number of coins needed to make up that amount.
If the amount cannot be made up by any combination of the coins, return -1.
You may assume you have an infinite number of each kind of coin.

Example: coins = [1, 2, 5], amount = 11 -> 3  (5 + 5 + 1)
         coins = [2], amount = 3 -> -1  (no combination makes 3)
         coins = [1], amount = 0 -> 0   (zero coins make amount 0)

Constraints: 1 <= len(coins) <= 12, 1 <= coins[i] <= 2^31 - 1,
             0 <= amount <= 10^4

Pattern: DYNAMIC PROGRAMMING (1D, minimum, optimal substructure).
Define dp[a] = the fewest coins needed to make amount a.
Consider the LAST coin you place to reach amount a: it is some coin c
(with c <= a), and everything before it is an optimal way to make a - c.
Every way to make a ends with one last coin, so:
    dp[a] = 1 + min(dp[a - c] for c in coins if c <= a)
That IS the whole problem — the best way to make a is built from the best
ways to make smaller amounts.

Base case: dp[0] = 0 (zero coins make amount 0). Every other dp[a] starts
at "infinity" (unreachable) and only improves if some coin leads to a
reachable smaller amount. The answer is dp[amount], or -1 if it is still
infinity.

Why not greedy? Taking the biggest coin first feels right (it works for
US coins), but it fails in general: coins = [1, 3, 4], amount = 6 ->
greedy takes 4 + 1 + 1 = 3 coins, but 3 + 3 = 2 coins is better. DP
checks every last-coin choice, so it never gets fooled.

The trap: brute-force recursion tries every combination of coins and
re-solves the same amounts exponentially. The DP insight is that dp[a - c]
never changes once computed, so remember it and each amount is done once.
"""


def coin_change(coins, amount):
    """
    Bottom-up fill of dp[0..amount].
    dp[a] = fewest coins to make amount a (inf = unreachable).
    Time: O(amount * len(coins)). Space: O(amount).
    """
    if amount == 0:
        return 0

    INF = float("inf")
    dp = [INF] * (amount + 1)
    dp[0] = 0  # base case: zero coins make amount 0

    for a in range(1, amount + 1):
        # Try every coin as the LAST coin placed to reach a.
        for c in coins:
            if c <= a and dp[a - c] != INF:
                dp[a] = min(dp[a], dp[a - c] + 1)

    return dp[amount] if dp[amount] != INF else -1


if __name__ == "__main__":
    assert coin_change([1, 2, 5], 11) == 3, "5 + 5 + 1"
    assert coin_change([2], 3) == -1, "impossible"
    assert coin_change([1], 0) == 0, "amount 0"
    assert coin_change([1], 1) == 1, "single coin"
    assert coin_change([1], 2) == 2, "only 1s"
    assert coin_change([1, 3, 4], 6) == 2, "greedy fails: 3 + 3 beats 4 + 1 + 1"
    assert coin_change([186, 419, 83, 408], 6249) == 20, "classic large case"
    assert coin_change([2, 5, 10, 1], 27) == 4, "10 + 10 + 5 + 2"
    print("All Coin Change sanity checks passed.")
