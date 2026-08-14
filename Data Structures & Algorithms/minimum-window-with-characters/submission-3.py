class Solution:
    def minWindow(self, s, t):
        needed_chars = {}
        for char in t:
            needed_chars[char] = needed_chars.get(char, 0) + 1
        
        min_window = ""
        window_counts = {}
        have, need = 0, len(needed_chars)
        l = 0
        
        for r in range(len(s)):
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            if char in needed_chars and window_counts[char] == needed_chars[char]:
                have += 1
            
            while have == need:
                substring_len = r - l + 1
                if not min_window or substring_len < len(min_window):
                    min_window = s[l:r+1]
                
                left_char = s[l]
                window_counts[left_char] -= 1
                if left_char in needed_chars and window_counts[left_char] < needed_chars[left_char]:
                    have -= 1
                l += 1
        
        return min_window