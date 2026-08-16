class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        heapq.heapify(minHeap)
        for i in range(len(points)):
            x, y = points[i]
            dist = (x**2 + y**2)**(1/2)
            heapq.heappush(minHeap, (dist, [x, y]))
        res = []
        for _ in range(k):
            dist, point = heapq.heappop(minHeap)
            res.append(point)
            
        return res