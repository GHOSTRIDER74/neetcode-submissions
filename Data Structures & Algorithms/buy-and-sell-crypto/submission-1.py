class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b_p = prices[0]
        max_p = 0 
        for p in prices[1:]:
            if b_p > p:
                b_p = p
            else:
                max_p = max(max_p, p - b_p)
        return(max_p)