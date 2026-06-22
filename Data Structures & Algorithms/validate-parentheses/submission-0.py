class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"}":"{","]":"[",")":"("}

        # Fixed: Changed s[1] to s to avoid IndexError on 1-char strings
        for char in s:
            if char in mapping:
                # Pop the top element if stack isn't empty; else assign a dummy value
                top_element = stack.pop() if stack else '#'

                # The mapping value must match the popped element
                if mapping[char] != top_element:
                    return False
            # Fixed: Changed stack[i] to stack[-1] to check the top item, and checked if stack exists
            else:
                # It is an opening bracket, push it onto the stack
                stack.append(char)
                
    # Return True if the stack is completely empty
        return len(stack) == 0
