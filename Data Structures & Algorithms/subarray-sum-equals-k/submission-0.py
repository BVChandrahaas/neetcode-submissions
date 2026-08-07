class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_dict = {0:1}
        prefix_sum =0
        subarray_count = 0
        
        for num in nums:
            prefix_sum += num

            prefix_window = prefix_sum - k

            subarray_count += prefix_dict.get(prefix_window, 0)

            prefix_dict[prefix_sum] = prefix_dict.get(prefix_sum, 0) + 1

        return subarray_count


        