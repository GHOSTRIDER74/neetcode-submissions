class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r= 0, len(height) - 1
        area = 0
        while l < r:
            area_curr = min(height[l],  height[r]) * (r - l)
            area = max(area, area_curr)
            if height[l] > height[r] and l < r:
                r -= 1
            else:
                l += 1
        return area
        