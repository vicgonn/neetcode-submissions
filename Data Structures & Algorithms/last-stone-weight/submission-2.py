import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # initialize heap and populate

        max_heap = stones.copy()
        
        heapq.heapify_max(max_heap)

        # do this while heap size > 1

        while len(max_heap) > 1:
            
            # max heap, pop first 2 if heap size >= 2

            rock_x = heapq.heappop_max(max_heap)
            rock_y = heapq.heappop_max(max_heap)

            print(rock_x)
            print(rock_y)
            # smash them
            if rock_x == rock_y:
                continue
            elif rock_x < rock_y:
                rock_y = rock_y - rock_x
                heapq.heappush_max(max_heap, rock_y)
            elif rock_x > rock_y:
                rock_x = rock_x - rock_y
                heapq.heappush_max(max_heap, rock_x)

        return heapq.heappop_max(max_heap) if max_heap else 0