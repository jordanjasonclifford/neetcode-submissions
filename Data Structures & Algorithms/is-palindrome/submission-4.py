class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if len(s) == 0 or len(s) == 1:
            return True

        newStr = ""
        for i in s:
            if i.isalnum():
                newStr += i.lower()

        

        left = 0
        right = len(newStr) - 1
        
        while left < right:

            if newStr[left] != newStr[right]:
                return False

            left += 1
            right -= 1

        return True