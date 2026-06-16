import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        


        min_heap = nums.copy()
        heapq.heapify(min_heap)

        if not nums:
            return 0

        while len(min_heap) > k:

            heapq.heappop(min_heap)

        return min_heap[0]