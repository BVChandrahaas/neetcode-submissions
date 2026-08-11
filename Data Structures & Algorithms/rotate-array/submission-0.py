class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        k = k%n
        res = []

        for i in range(n-k, n):
            res.append(nums[i])

        for i in range(0, n-k):
            res.append(nums[i])
        
        for i in range(n):
            nums[i] = res[i]

        

        