class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        temp_stack = []

        for i in range(len(temperatures)):

            while temp_stack and temperatures[temp_stack[-1]] < temperatures[i]:
                idx = temp_stack.pop()
                result[idx] = i-idx
            temp_stack.append(i)

        return result

        