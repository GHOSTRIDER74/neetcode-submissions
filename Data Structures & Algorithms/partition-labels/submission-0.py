class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastidx = {}
        for i in range(len(s)):
            lastidx[s[i]] = i
        res = []
        size = end = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastidx[c])

            if i == end:
                res.append(size)
                size = 0
        return res