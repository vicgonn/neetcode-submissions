import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        max_heap = [x for x in count.values()]

        heapq.heapify_max(max_heap)
        queue = deque()
        time = 0
        while max_heap or queue:
            time += 1

            if max_heap:
                cnt = heapq.heappop_max(max_heap) - 1
                if cnt:
                    queue.append([cnt, time + n])
            if queue and queue[0][1] == time:
                heapq.heappush_max(max_heap, queue.popleft()[0])

        

        print(max_heap)

        return time