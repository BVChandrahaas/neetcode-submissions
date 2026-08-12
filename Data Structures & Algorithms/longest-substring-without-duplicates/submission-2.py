class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        visited_chars = set()
        left = 0
        max_length = 0

        for right in range(len(s)):

            while s[right] in visited_chars:
                visited_chars.remove(s[left])
                left += 1

            visited_chars.add(s[right])
            max_length = max(right-left+1, max_length)
        return max_length


        
            


        