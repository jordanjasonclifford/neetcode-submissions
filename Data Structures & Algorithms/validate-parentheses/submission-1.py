class Solution:
    def isValid(self, s: str) -> bool:

        # Map each closing bracket to its corresponding opening bracket
        map = {')': '(', ']': '[', '}': '{'}

        # Stack to keep track of opening brackets
        stack = []

        # Iterate through each character in the string
        for char in s:

            # If it's an opening bracket, push it onto the stack
            if char not in map:
                stack.append(char)

            else:
                # If it's a closing bracket:
                # 1. Check if stack is empty (no matching opening bracket)
                # 2. Check if top of stack matches the expected opening bracket
                if not stack or map[char] != stack.pop():
                    return False

        # If stack is empty, all brackets were matched correctly
        # If not, there are unmatched opening brackets left
        return not stack