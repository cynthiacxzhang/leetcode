class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        # dict????
        part = {")":"(", "]":"[", "}":"{"}

        for ch in s:
            # if opening bracket, add to top of stack
            if ch in part.values():
                stack.append(ch)
            # if closing bracket, check top of stack to see if corresponding opening is correct
            elif ch in part: 
                # stack empty or bracket mismatch
                if not stack or stack[-1] != part[ch]:
                    return False
                # remove topmost if closing corresponds to opening
                stack.pop()
            else:
                return False
        
        # if stack is empty, return true (means all openings have been closed properly)
        return len(stack) == 0

        

