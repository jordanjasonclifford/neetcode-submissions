class Solution:
    def isValid(self, s: str) -> bool:

       

         # Map each closing bracket to its corresponding opening bracket
        map = {')': '(', ']': '[', '}': '{'}

        # Stack to keep track of opening brackets
        stack = []

        for c in s:
            if c in map:
                if stack and stack[-1] == map[c]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)

        if not stack:
            return True

        else:
            return False