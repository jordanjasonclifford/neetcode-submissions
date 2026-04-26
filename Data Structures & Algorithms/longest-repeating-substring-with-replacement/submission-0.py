class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}   # stores frequency of characters in current window
        res = 0      # max length found

        l = 0        # left pointer
        maxf = 0     # count of most frequent character in window

        for r in range(len(s)):
            # add current character to window
            count[s[r]] = 1 + count.get(s[r], 0)

            # update most frequent character count
            maxf = max(maxf, count[s[r]])

            # if window is invalid (need more than k replacements)
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1  # shrink from left
                l += 1

            # update result with current valid window size
            res = max(res, r - l + 1)

        return res