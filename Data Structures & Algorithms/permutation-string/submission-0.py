class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        freq1 = {}
        freq2 = {}

        for char in s1:
            freq1[char] = freq1.get(char, 0) +1

        left = 0
        k = len(s1)

        for right in range(len(s2)):
            char_right = s2[right]

            freq2[char_right] = freq2.get(char_right,0)+1

            if right - left + 1 > k:
                char_left = s2[left]
                freq2[char_left] -= 1
                if freq2[char_left] == 0:
                    del freq2[char_left]
                left += 1

            # 3. Check if the current window matches s1's frequency
            if freq1 == freq2:
                return True
                
        return False

            

        