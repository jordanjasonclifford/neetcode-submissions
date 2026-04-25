class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # result = longest substring length found
        res = 0

        # set to track characters currently in the window
        charSet = set()

        # left pointer of the window
        l = 0

        # expand window with right pointer
        for r in range(len(s)):

            # if duplicate found, shrink window from left
            # until duplicate is removed
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            # add current character to window
            charSet.add(s[r])

            # update max length (window size = r - l + 1)
            res = max(res, r - l + 1)

        return res
        