class Solution:
    def isValid(self, s: str) -> bool:

        map = {')': '(', ']': '[', '}': '{'}
        stack = []

        for char in s:
            if char not in map:
                stack.append(char)
            else:
                if not stack or map[char] != stack.pop():
                    return False

        return not stack
        