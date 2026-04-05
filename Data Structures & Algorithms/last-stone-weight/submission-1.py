class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while 2<=len(stones):
            x=heapq.heappop_max(stones)
            y=heapq.heappop_max(stones)
            if not (x == y):
                heapq.heappush_max(stones,abs(x-y))

        return stones[-1] if len(stones)>=1 else 0


        