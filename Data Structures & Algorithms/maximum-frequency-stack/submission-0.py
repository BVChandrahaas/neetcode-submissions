class FreqStack:

    def __init__(self):
        self.stack = []
        self.frequency_map = {}
        self.max_frequency = 0
        

    def push(self, val: int) -> None: # O(n)
        
        self.stack.append(val)
        self.frequency_map[val] = self.frequency_map.get(val, 0) + 1
        self.max_frequency = max(self.frequency_map.values()) # O(n)
        
    def pop(self) -> int:

        for i in range(len(self.stack)-1 ,-1, -1):

            if self.frequency_map[self.stack[i]] == self.max_frequency:

                self.frequency_map[self.stack[i]] = self.frequency_map.get(self.stack[i],0)-1
                self.max_frequency = max(self.frequency_map.values())
                val = self.stack.pop(i)

                return val
            


