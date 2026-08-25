class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time, fresh = 0, 0 
        q = collections.deque()
        row, col = len(grid), len(grid[0])

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    rw = r + dr
                    co = c + dc
                    if (rw not in range(row) or co not in range(col)
                        or grid[rw][co] != 1):
                        continue
                    grid[rw][co] = 2
                    fresh -= 1
                    q.append((rw, co))
            time += 1
        return time if fresh == 0 else -1