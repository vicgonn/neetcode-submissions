import heapq
import copy

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        self.k = k
        self.min_heap = copy.deepcopy(nums)
        heapq.heapify(self.min_heap)
        self.init_len = len(self.min_heap)

        while self.init_len > k:
            heapq.heappop(self.min_heap)
            self.init_len -= 1

        # print(self.init_len)

    def add(self, val: int) -> int:
        
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        

        return self.min_heap[0]
