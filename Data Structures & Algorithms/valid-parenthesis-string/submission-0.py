class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin = 0  # Minimum possible unmatched '('
        cmax = 0  # Maximum possible unmatched '('

        for char in s:
            if char == '(':
                cmin += 1
                cmax += 1
            elif char == ')':
                cmin -= 1
                cmax -= 1
            else:  
                cmin -= 1  
                cmax += 1  

            if cmax < 0:
                return False

            cmin = max(cmin, 0)

        return cmin == 0 