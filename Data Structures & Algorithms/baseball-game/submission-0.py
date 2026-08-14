class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_stack = []
        result = 0
        for op in operations:
            if op =='+':
                score_stack.append(score_stack[-1]+score_stack[-2])
            elif op == 'D':
                score_stack.append(score_stack[-1]*2)
            elif op == 'C':
                score_stack.pop()
            else:
                score_stack.append(int(op))

        for score in score_stack:
            result += score
        
        return result
        