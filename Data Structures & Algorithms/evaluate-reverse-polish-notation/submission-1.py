class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation_stack = []

        for token in tokens:
            if token == "+":
                operation_stack.append(operation_stack.pop()+operation_stack.pop())
            elif token == "*":
                operation_stack.append(operation_stack.pop()*operation_stack.pop())
            elif token == "-":
                a,b = operation_stack.pop(), operation_stack.pop()
                operation_stack.append(b-a)
            elif token == "/":
                a,b = operation_stack.pop(),operation_stack.pop()
                operation_stack.append(int(float(b)/a))
            
            else:
                operation_stack.append(int(token))
        return operation_stack[0]
        