class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curmax, curmin = 1, 1

        for n in nums:
            if n == 0:
                res = max(n, res)
                curmax, curmin = 1, 1
                continue
            temp = curmax * n
            curmax = max(temp, curmin * n, n)
            curmin = min(temp, curmin * n, n)
            res = max(res, curmax)
        
        return res