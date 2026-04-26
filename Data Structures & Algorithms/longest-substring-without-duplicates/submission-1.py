class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # set to store current window characters (no duplicates allowed)
        charSet = set()

        # left pointer of sliding window
        left = 0
        
        # result (max length found so far)
        res = 0

        # right pointer expands the window
        for right in range(len(s)):

            # if duplicate found, shrink window from the left
            # until duplicate is removed
            while s[right] in charSet:
                charSet.remove(s[left])  # remove left char
                left += 1                # move left pointer forward

            # add current character to the set
            charSet.add(s[right])

            # update max length of substring
            # (window size = right - left + 1)
            res = max(res, right - left + 1)

        return res