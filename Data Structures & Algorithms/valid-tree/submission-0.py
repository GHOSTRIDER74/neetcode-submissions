class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        adj = {i:[] for i in range(n)}

        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        
        v = set()
        def dfs(i,prev):
            if i in v:
                return False
            
            v.add(i)

            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j,i):
                    return False
            return True
        
        return dfs(0,-1) and n == len(v)