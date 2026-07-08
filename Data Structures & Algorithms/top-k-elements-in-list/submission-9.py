class Solution:

    def topKFrequent(self, nums:List, k:int):

        bucket = [[] for i in range(len(nums)+1)]
        frequency = {}
        result = []

        for index, value in enumerate(nums):

            frequency[value] = frequency.get(value, 0) + 1

        for key, value in frequency.items():

            bucket[value].append(key)

        # print(frequency)
        # print(bucket)

        for i in range(len(bucket)-1, 0, -1):

            for num in bucket[i]:
                result.append(num)

                if len(result) == k:
                    return result






