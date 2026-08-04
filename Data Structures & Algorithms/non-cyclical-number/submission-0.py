class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sos(n)
            if n == 1:
                return True
        return False
    def sos(self, n):   
        s = 0
        while n:
            d = n % 10
            s += d ** 2
            n = n // 10
        return s