class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        result = []
        i = 0
        j = len(arr) - 1

        while j - i + 1 > k:
            if abs(arr[i] - x) > abs(arr[j] - x):
                i += 1
            else:
                j -= 1

        for y in range(i, j+1):
            result.append(arr[y])

        return result

        
        

        