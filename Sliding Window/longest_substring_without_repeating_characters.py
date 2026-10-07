"""
LeetCode 3 - Longest Substring Without Repeating Characters (Sliding Window)

Given a string `s`, find the length of the longest substring without
repeating characters.

Example:
    s = "abcabcbb" -> 3 ("abc")
    s = "bbbbb"    -> 1 ("b")
    s = "pwwkew"   -> 3 ("wke")

Constraints:
    * 0 <= len(s) <= 5 * 10^4
    * s consists of English letters, digits, symbols and spaces.

Approach - variable-size sliding window + hash map:
    Grow `right` one char at a time. Remember each char's LAST index seen.
    If the incoming char already appears INSIDE the current window,
    jump `left` to just past its previous occurrence (never backwards).
    The window [left, right] is then always duplicate-free, and the best
    length seen so far is the answer.

    Each index enters/leaves the window once -> O(n) time.
    The dict holds at most one entry per distinct char -> O(min(n, alphabet)) space.
"""


def length_of_longest_substring(s: str) -> int:
    last_seen: dict[str, int] = {}  # char -> its most recent index
    left = 0
    best = 0

    for right, ch in enumerate(s):
        # Duplicate inside the current window? Shrink from the left past it.
        # The `>= left` guard keeps `left` from ever moving backwards
        # (e.g. "abba": the second 'a' is stale once left passed index 0).
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1

        last_seen[ch] = right
        best = max(best, right - left + 1)

    return best


if __name__ == "__main__":
    # LeetCode's example cases - quick sanity check.
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    # Edge cases.
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring(" ") == 1
    assert length_of_longest_substring("abba") == 2      # stale-index trap
    assert length_of_longest_substring("dvdf") == 3
    assert length_of_longest_substring("tmmzuxt") == 5

    print("All Longest Substring Without Repeating Characters checks passed.")
