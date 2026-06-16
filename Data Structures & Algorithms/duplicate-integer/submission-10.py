class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False

        mapper = {}

        for num in nums:
            mapper[num] = mapper.get(num, 0) + 1

        for k,v in mapper.items():

            if v > 1:
                return True
                
        return False

