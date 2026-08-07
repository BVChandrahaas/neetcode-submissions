class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        count_dict = {}

        res = []

        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1

        for key, val in count_dict.items():
            if val > len(nums)//3:
                res.append(key)
        
        return res



        
            

        

        