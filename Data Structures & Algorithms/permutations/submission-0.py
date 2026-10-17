class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        if len(nums) == 1:
            return [nums[:]]

        for _ in range(len(nums)):
            n = nums.pop(0)
            prems = self.permute(nums)
            for perm in prems:
                perm.append(n)

            res.extend(prems)
            nums.append(n)
        return res