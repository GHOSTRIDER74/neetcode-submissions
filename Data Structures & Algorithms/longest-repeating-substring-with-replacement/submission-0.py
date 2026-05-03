class Solution:
    from collections import defaultdict
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        hash = defaultdict(int)
        n = len(s)
        m = 0
        result = 0
        for right in range(n):
            hash[s[right]] += 1
            m = max(m,hash[s[right]])
            if (right - left + 1) - m > k:
                hash[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result  