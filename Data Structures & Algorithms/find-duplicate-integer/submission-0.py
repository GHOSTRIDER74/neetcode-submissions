class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        from collections import defaultdict
        mp = defaultdict(int)
        for num in nums:
            mp[num] += 1
        for num in mp:
            if mp[num] > 1:
                return num   