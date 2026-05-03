class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        from collections import deque 
        rows, columns = len(heights), len(heights[0])
        p_que = deque()
        p_set = set()

        a_que = deque()
        a_set = set()

        for i in range(columns):
            p_que.append((0, i))
            p_set.add((0, i))

        for j in range(1,rows):
            p_que.append((j, 0))
            p_set.add((j, 0))
        
        for j in range(rows):
            a_que.append((j, columns-1))
            a_set.add((j, columns-1))
        
        for i in range(columns):
            a_que.append((rows-1, i))
            a_set.add((rows-1, i))
        
        def get_coords(que, seen):
            while que:
                i, j = que.popleft()
                for i_off, j_off in [(0,1),(1,0),(-1, 0),(0, -1)]:
                    r, c = i + i_off, j + j_off
                    if 0 <= r <= rows-1 and 0 <= c <= columns-1 and heights[r][c] >= heights[i][j] and (r, c) not in seen:
                        seen.add((r, c))
                        que.append((r, c))
        get_coords(p_que, p_set)
        get_coords(a_que, a_set)

        return list(p_set.intersection(a_set))