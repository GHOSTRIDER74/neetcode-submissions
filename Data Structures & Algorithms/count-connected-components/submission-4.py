class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        c = 0
        if not n:
            return c
        
        adj = {i:[] for i in range(n)}

        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        
        v = set()

        def dfs(i):
            if i in v:
                return  
            v.add(i)
            for j in adj[i]:
                dfs(j)

        for i in range(n):
            if i not in v:
                dfs(i)
                c += 1
        return c 