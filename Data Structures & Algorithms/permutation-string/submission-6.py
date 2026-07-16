class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1 = sorted(s1)
        l, r = 0, len(s1)

        while r <= len(s2):
            sub = s2[l : r]
            print(sub)
            if sorted(sub) == s1:
                return True
            l += 1
            r += 1
        return False