class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        stack question! use List to represent stack

        input string - parse tokens
        - keep dictionary to track operations
        - will need a loop for each operation

        iterate through tokens?
        ["2","1","+","3","*"]
        """

        ops = {"+", "-", "*", "/"}

        def calculate (left, right, op):
            if op == "+":
                return left + right
            elif op == "-":
                return left - right
            elif op == "*":
                return left * right
            else: 
                return left / right
            

        stack = []
        result = 0

        # loop through tokens
        for tok in tokens:

            # push numbers onto stack
            if tok not in ops:
                stack.append(int(tok))
                print(tok)
            # if tok = operation, pop top 2 and calulate result
            else: 
                # type casting
                right = int(stack.pop())
                left = int(stack.pop())

                result = int(calculate(left, right, tok))
                print(result)
                stack.append(int(result)) # add result back onto top of stack

        # originally returning result
        # but stack already holds the final answer (since result is 
        # being pushed to the top after it's calculated)
        # also accounts for edge case where result isn't calculated at all

        return stack[-1]