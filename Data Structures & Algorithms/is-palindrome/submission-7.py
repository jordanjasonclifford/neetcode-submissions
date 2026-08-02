class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if len(s) == 0 or len(s) == 1:
            return True

        newStr = ""

        for l in s:
            if l.isalnum():
                newStr += l.lower()

        #######
        # 2 ptrs
        left = 0
        right = len(newStr) - 1

        while left < len(newStr):

            if newStr[left] != newStr[right]:
                return False

            else:

                left += 1
                right -= 1

        return True