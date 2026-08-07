class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        nums_set = set(nums)
        for num in nums:
            if num-1 not in nums_set:
                length = 1

                while num + 1 in nums_set:
                    num += 1
                    length += 1

                max_length = max(length, max_length)

        return max_length



        