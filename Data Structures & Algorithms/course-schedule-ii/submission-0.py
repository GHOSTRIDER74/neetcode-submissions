class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        prereq = {c : [] for c in range(numCourses)}
        for c , pre in prerequisites:
            prereq[c].append(pre)
        output = []
        visit, cycle = set(), set()

        def dfs(c):
            if c in cycle:
                return False
            if c in visit:
                return True
            
            cycle.add(c)

            for pre in prereq[c]:
                if dfs(pre) == False:
                    return False
            cycle.remove(c)
            visit.add(c)
            output.append(c)
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output