class Solution:
    def isValid(self, s: str) -> bool:
        openPar = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        closePar = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for char in s:
            if char in openPar:
                stack.append(char)
            
            if char in closePar:
                if len(stack) == 0 or stack[-1] != closePar[char]:
                    return False
                stack.pop()
            
            
        
        return True if len(stack)==0 else False