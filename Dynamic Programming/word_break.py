"""
LeetCode 139 - Word Break (Dynamic Programming)

Problem: Given a string s and a dictionary of strings wordDict, return
True if s can be segmented into a space-separated sequence of one or
more dictionary words. The same word may be reused multiple times.

Example: s = "leetcode", wordDict = ["leet", "code"] -> True
         ("leetcode" splits as "leet" + "code")
         s = "applepenapple", wordDict = ["apple", "pen"] -> True
         s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
         -> False ("cats" + "and" + "og" fails, "cat" + "sand" + "og" fails)

Constraints: 1 <= len(s) <= 300, 1 <= len(wordDict) <= 1000,
             1 <= len(word) <= 20, all lowercase English letters.

Pattern: DYNAMIC PROGRAMMING (1D boolean table over prefixes).
Ask a smaller question first: instead of "can the WHOLE string be
segmented?", ask "can the PREFIX ending at each position be segmented?"
Let dp[i] = True if the first i characters, s[:i], can be segmented.
dp[0] = True — the empty prefix is trivially segmentable, and it is
the base every longer answer builds on.

To compute dp[i], look backwards for a split point j < i such that:
  - the prefix s[:j] is segmentable (dp[j] is True), AND
  - the slice s[j:i] is a word in the dictionary.
If any such j exists, dp[i] = True. The answer is dp[len(s)].

Why this works: any valid segmentation of s[:i] ends with some
dictionary word s[j:i], and everything before it, s[:j], must itself
be a valid segmentation. So the problem at length i reduces to the
same problem at a shorter length j — the classic DP shape: the answer
for a prefix depends only on answers for shorter prefixes.

Two small speedups worth knowing:
  - Only check j where dp[j] is True. A False prefix can never be
    extended into a True one, so most split points are skipped.
  - Only check slices up to the longest dictionary word. A slice
    longer than every word in wordDict can never be a word, so there
    is no point testing it. This caps the inner loop at max_len (<= 20)
    instead of i.

The tempting wrong approach is the greedy one: scan left to right and
take the longest (or shortest) dictionary word that matches at each
step. It fails: s = "catsandog" with ["cats", "dog", "sand", "and",
"cat"] — greedy takes "cats", then "and", then gets stuck on "og".
DP survives because it remembers EVERY reachable split point, not
just the one greedy picked. A related trap: "applepenapple" needs
"apple" twice — reuse is allowed, so the dictionary is a set you can
draw from again and again, not a bag of words you use up.

The alternative shape is recursion + memoization (DFS from position i:
try every word that matches at i, recurse on the rest). Same idea,
same complexity — DP bottom-up just writes the table explicitly,
which is usually cleaner to explain in an interview.

Complexity: O(n * m) time, where n = len(s) and m = the longest word
in wordDict (<= 20): for each of the n positions we test at most m
split points, each a set lookup. Without the max-length cap it is
O(n^2) in the worst case. O(n) extra space for the dp table, plus
O(total dictionary characters) for the word set.
"""


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # A set makes "is this slice a word?" an O(1) lookup.
        word_set = set(wordDict)
        # max_len caps how far back we need to look for a split point:
        # no dictionary word is longer than this.
        max_len = max(len(word) for word in wordDict)

        n = len(s)
        # dp[i] = can the first i characters, s[:i], be segmented?
        # dp[0] = True: the empty prefix is trivially segmentable,
        # and every longer answer builds on it.
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            # Only look back as far as the longest dictionary word.
            start = max(0, i - max_len)
            for j in range(start, i):
                # Skip split points that are not reachable: a False
                # prefix can never be extended into a True one.
                if not dp[j]:
                    continue
                # If the prefix up to j works AND s[j:i] is a word,
                # the prefix up to i works too.
                if s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]


if __name__ == "__main__":
    s = Solution()

    # Examples from the problem statement.
    assert s.wordBreak("leetcode", ["leet", "code"]) is True
    assert s.wordBreak("applepenapple", ["apple", "pen"]) is True
    assert s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False

    # Same words as the False example above, but with a "d" added the
    # string segments: "cats" + "and" + "dog" (or "cat" + "sand" + "dog").
    assert s.wordBreak("catsanddog", ["cats", "dog", "sand", "and", "cat"]) is True

    # Single word that is the whole string; reuse of the same word.
    assert s.wordBreak("apple", ["apple"]) is True
    assert s.wordBreak("aaaaaaa", ["aaaa", "aaa"]) is True

    # A word that is a prefix of another must not fool the check:
    # "aaaa" cannot be made from "aaa" alone.
    assert s.wordBreak("aaaa", ["aaa"]) is False

    # Empty dictionary and single-character cases.
    assert s.wordBreak("a", ["b"]) is False
    assert s.wordBreak("a", ["a"]) is True

    # Overlapping words: "aaaaaaa" from "aa" + "aaa" in many ways.
    assert s.wordBreak("aaaaaaa", ["aa", "aaa"]) is True

    print("All tests passed!")
