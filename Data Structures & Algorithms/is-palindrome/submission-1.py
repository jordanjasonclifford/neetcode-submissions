class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""


        if len(s) == 0 or len(s) == 1: # base check
            return True   

        for n in s:         # build new string
            if n.isalnum():
                newStr += n.lower()

        left = 0
        right = len(newStr) - 1

        while left < right:

            if newStr[left] != newStr[right]:   # check if indices are same
                return False

            left += 1
            right -= 1


        return True






        
        