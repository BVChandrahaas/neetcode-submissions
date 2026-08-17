class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1
        res = len(nums)
        while i <=j:
            mid = i +(j-i)//2

            if nums[mid] < target:
                i = mid +1

            if nums[mid] > target:
                res = mid
                j = mid-1

            if nums[mid] == target:
                return mid

        return res

        