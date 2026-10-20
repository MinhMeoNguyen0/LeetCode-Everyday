"""
LeetCode 49 - Group Anagrams (Hash Map)

Given an array of strings `strs`, group the anagrams together. You can
return the answer in any order. An anagram is a word formed by rearranging
the letters of another (same letters, same counts).

Example:
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    -> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    (order of groups/words may differ)

Approach - canonical key in one pass:
    The brute force compares every pair of strings with a 26-letter count
    check: O(n^2 * k), far too slow. The insight is that anagrams are
    IDENTICAL under a canonical form - sorted letters ("aet") or a fixed
    26-count tuple (1, 0, 0, ..., 1, ...). Compute that key once per string
    and let a dict collect strings by key: dict[key].append(s).

    This is the folder template's FREQUENCY COUNTING skeleton (see
    Hash Map/template.py): one pass to build the key, O(1) dict lookups
    to place each string into its group.

    Count-tuple keys cost O(k) per string, so O(n * k) time total, where
    n = number of strings and k = max string length. A tuple is hashable
    (a list is not), so it works as a dict key directly. Space is O(n * k)
    for the stored strings plus keys.

    Alternative key: ''.join(sorted(s)) - simpler, but O(k log k) per
    string. Mention it in an interview, ship the count tuple.
"""


def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups: dict[tuple[int, ...], list[str]] = {}

    for s in strs:
        # Canonical key: 26-slot count of each lowercase letter.
        # Anagrams produce the exact same tuple; different words don't.
        counts = [0] * 26
        for ch in s:
            counts[ord(ch) - ord("a")] += 1
        key = tuple(counts)  # Hashable -> usable as a dict key.

        # Group by key; setdefault creates the bucket on first sight.
        groups.setdefault(key, []).append(s)

    return list(groups.values())


if __name__ == "__main__":
    # The classic example: 3 anagram groups.
    out = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    normalized = sorted(sorted(g) for g in out)
    assert normalized == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]

    # Single string -> one group.
    assert group_anagrams(["a"]) == [["a"]]

    # Empty string is its own (zero-count) group; duplicates stay together.
    assert group_anagrams(["", ""]) == [["", ""]]

    # No anagrams at all -> each string alone.
    assert sorted(map(sorted, group_anagrams(["abc", "def"]))) == [["abc"], ["def"]]

    # Empty input -> empty output.
    assert group_anagrams([]) == []

    print("All Group Anagrams sanity checks passed.")
