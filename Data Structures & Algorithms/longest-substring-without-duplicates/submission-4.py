class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Stores the characters currently inside the sliding window.
        # A set is used because checking whether a character exists is O(1).
        charSet = set()

        # Left pointer of the sliding window.
        left = 0

        # Stores the maximum substring length found so far.
        res = 0

        # The right pointer expands the window one character at a time.
        for right in range(len(s)):

            # If the current character is already in the window,
            # shrink the window from the left until the duplicate is removed.
            while s[right] in charSet:
                
                # Remove the leftmost character from the current window.
                charSet.remove(s[left])

                # Move the left pointer forward.
                left += 1

            # Add the current character to the window.
            # At this point, it is guaranteed not to be a duplicate.
            charSet.add(s[right])

            # Calculate the current window length.
            # We add 1 because both left and right positions are included.
            current_length = right - left + 1

            # Update the longest valid substring length found so far.
            res = max(res, current_length)

        # Return the length of the longest substring
        # that contains no repeating characters.
        return res