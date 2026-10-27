"""
LeetCode 125 - Valid Palindrome (Two Pointers)

Problem: Given a string s, return True if it is a palindrome after
converting all uppercase letters to lowercase and removing all
non-alphanumeric characters. A string that becomes empty after this
cleaning counts as a palindrome.

Example: "A man, a plan, a canal: Panama" -> True
         "race a car" -> False

Constraints: 1 <= s.length <= 2 * 10^5, s consists of printable ASCII.

Pattern: TWO POINTERS (inward from both ends)
- This is the inward two-pointers shape: one pointer starts at the
  left end, one at the right end, and they walk toward each other.
  Compare the Two Pointers solutions already in this folder
  (Container With Most Water, Three Sum, Two Sum II), where the
  pointers also move based on what they see -- here, though, the
  pointers only ever move inward, one step at a time, and they never
  cross: the loop stops as soon as left >= right, because everything
  in between has already been checked.
- The twist versus a plain "is s == s[::-1]" check is the SKIPPING:
  the pointers must skip any character that is not alphanumeric
  before comparing. Skipping happens inside the loop, before the
  comparison, so a punctuation mark or space never gets compared
  to a letter or digit -- it is simply stepped over.
- Case is normalised with lower() at comparison time, not by
  building a cleaned copy of the string first. Building a cleaned
  copy (filter + reverse, or s == s[::-1] on the cleaned string)
  is also correct, but it costs O(n) extra space; the two-pointer
  version needs only the two indices, so it is O(1) extra space.
- The first mismatch decides the answer: as soon as one pair
  differs, we can return False immediately, without scanning the
  rest of the string.

Time:  O(n) -- each character is visited at most once by one pointer.
Space: O(1) extra -- only the two pointer indices, no cleaned copy.

Pitfall to watch: comparing characters before skipping, or
forgetting to re-check that left < right after skipping (a string
of only punctuation, like ".,", must return True, not crash or
compare a character against itself out of order).
"""


def is_palindrome(s: str) -> bool:
    """
    Return True if s is a palindrome after lowercasing and
    removing all non-alphanumeric characters.

    Time:  O(n).
    Space: O(1) extra.
    """
    left = 0
    right = len(s) - 1

    while left < right:
        # Skip anything that is not a letter or digit.
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        # After skipping, the pointers may have met (e.g. the
        # whole string was punctuation) -- then it is a palindrome.
        if left >= right:
            break

        # Compare case-insensitively; one mismatch ends it.
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    # The classic example: punctuation and capitals are ignored.
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    # "raceacar" is not a palindrome.
    assert is_palindrome("race a car") is False
    # Only spaces / punctuation left after cleaning -> palindrome.
    assert is_palindrome(" ") is True
    assert is_palindrome(".,") is True
    # Empty string is a palindrome.
    assert is_palindrome("") is True
    # Digits count as alphanumeric, and '0' != 'p'.
    assert is_palindrome("0P") is False
    # Mixed case, single differing pair in the middle.
    assert is_palindrome("ab@a") is True
    assert is_palindrome("ab@b") is False
    print("All sanity checks passed.")
