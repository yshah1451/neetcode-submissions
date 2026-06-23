class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        for item in tokens:
                if item in operators:
                # Safety check to prevent the exact IndexError you encountered
                    if len(stack) < 2:
                        return 0 
                    
                    op1 = stack.pop()
                    op2 = stack.pop()
                    
                    # Perform the one-liner calculation
                    result = int(eval(f"{op2} {item} {op1}"))
                    stack.append(result)
                else:
                    # Crucial: Must convert string token to int before pushing
                    stack.append(int(item))
        return stack[0] if stack else 0