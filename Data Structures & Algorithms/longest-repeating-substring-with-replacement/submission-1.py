class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0

        # Convert string to a set → all unique characters in s
        # We will try making the window all one character at a time
        charSet = set(s)

        # Try each character as the "target" we want the window to become
        for c in charSet:

            count = 0   # number of times 'c' appears in current window
            l = 0       # left pointer of sliding window

            # expand the window using right pointer
            for r in range(len(s)):

                # if current character matches our target 'c',
                # increase count of matching characters
                if s[r] == c:
                    count += 1

                # window size = (r - l + 1)
                # number of characters we need to replace =
                # window size - number of correct chars (count)
                # if replacements needed > k → window invalid → shrink it
                while (r - l + 1) - count > k:

                    # if we're removing a character that was 'c',
                    # decrease the count
                    if s[l] == c:
                        count -= 1

                    # move left pointer to shrink window
                    l += 1

                # update result with max valid window size found so far
                res = max(res, r - l + 1)

        # return the maximum length of valid window
        return res