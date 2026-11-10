class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]

        def dfs (r, c):
            if dp[r][c] != 0:
                return dp[r][c]

            max_len = 1 
            
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    max_len = max(max_len, 1 + dfs(nr, nc))
            
            dp[r][c] = max_len
            return dp[r][c]
        
        longest = 0
        for r in range(rows):
            for c in range(cols):
                longest = max(longest, dfs(r, c))
                
        return longest