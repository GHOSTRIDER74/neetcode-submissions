class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0 
        n = len(nums)
        op = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i + 1, n -1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    op.append([nums[i],nums[j],nums[k]])
                    j, k = j + 1, k - 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif total < 0:
                    j += 1 
                else:
                    k -= 1        
        return op