class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}

        def solve(i: int) -> int:
            # If the current character is '0', it's an invalid decoding path
            if i < len(s) and s[i] == '0':
                return 0
            
            # Base case: reached the last character or successfully moved beyond it
            if i >= len(s) - 1:
                return 1

            # Check if the result is already memoized
            if i in dp:
                return dp[i]

            # Option 1: Decode a single digit
            ans = solve(i + 1)
            
            # Option 2: Decode a two-digit number (must be <= 26)
            if int(s[i : i + 2]) <= 26:
                ans += solve(i + 2)

            # Store in memoization table and return
            dp[i] = ans
            return ans

        return solve(0)