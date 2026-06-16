class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if not nums:
            return []

        mapper = {}

        for i, nums in enumerate(nums):

            result = target - nums

            if result in mapper:
                return [mapper[result], i]

            mapper[nums] = i

        return 


        