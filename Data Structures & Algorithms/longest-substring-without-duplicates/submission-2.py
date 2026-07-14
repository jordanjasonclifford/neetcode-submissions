class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # set to store current window characters (no duplicates allowed)
        charSet = set()

        left = 0

        res = 0

        for right in range(len(s)):

            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1

            # add
            charSet.add(s[right])


            # update lengthh
            res = max(res, right - left + 1)


        return res