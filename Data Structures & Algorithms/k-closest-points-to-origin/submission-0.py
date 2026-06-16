import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # use min heap

        # create a min heap and populate with points in a 3 tuple entry (evaluates starting at index 0)

        min_heap = []
        closest_points = []

        heapq.heapify(min_heap)
        for x, y in points:
            distance = x ** 2 + y ** 2
            heapq.heappush(min_heap, [distance, x, y])

        while len(closest_points) < k:
            _, xv, yv = heapq.heappop(min_heap)
            closest_points.append([xv, yv])

        
        return closest_points