class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        length = len(nums)

        if length <=1:
            return nums[0]

        count_map = defaultdict(int)

        for i in range(length):
            if not count_map[nums[i]]:
                count_map[nums[i]] = 1
            count_map[nums[i]] += 1

        for num, count in count_map.items():
            if count > length/2:
                return num
        


        # return 1

        