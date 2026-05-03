class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = 0 
        char = '' 
        for ca in s:
            if ca in char:
                dup_index = char.index(ca)
                char = char[dup_index + 1:]
            char += ca
            c = max(c, len(char))
        return c