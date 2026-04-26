class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  # stack to store numbers

        for c in tokens:
            # if operator, perform operation using top elements of stack
            if c == "+":
                # pop two values and add
                stack.append(stack.pop() + stack.pop())
                
            elif c == "-":
                # order matters → second popped is first operand
                a = stack.pop()  # second number
                b = stack.pop()  # first number
                stack.append(b - a)
                
            elif c == "*":
                # multiply top two values
                stack.append(stack.pop() * stack.pop())

            elif c == "/":
                # order matters for division
                a = stack.pop()
                b = stack.pop()

                # use int(float(...)) to truncate toward zero
                stack.append(int(float(b) / a))

            else:
                # if it's a number, push onto stack
                stack.append(int(c))

        # final result is the only value left in stack
        return stack[0]