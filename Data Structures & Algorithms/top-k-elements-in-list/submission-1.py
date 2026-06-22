class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            map[num] = 1 + map.get(num, 0)
        map = sorted(map.items(), key=lambda x: x[1], reverse=True)

        op_list = []
        for i in range(k):
            op_list.append(map[i][0])
        return op_list