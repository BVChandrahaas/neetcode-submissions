class Solution:
    def isValid(self, s: str) -> bool:
        valid_stack = []

        parentheses_map = {'}':'{', ']':'[', ')':'('}

        for char in s:
            if char in parentheses_map:          
                if not valid_stack or valid_stack[-1] != parentheses_map[char]:
                    return False                  
                valid_stack.pop()
            else:                                 
                valid_stack.append(char)
        return len(valid_stack) <=0
        