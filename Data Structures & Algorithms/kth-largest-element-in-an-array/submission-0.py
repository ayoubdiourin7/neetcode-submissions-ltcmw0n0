class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap,num)
            if k<len(heap):
                heapq.heappop(heap)
            
        return heapq.heappop(heap)