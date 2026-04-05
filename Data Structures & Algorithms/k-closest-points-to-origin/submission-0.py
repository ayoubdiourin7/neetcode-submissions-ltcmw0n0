import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        maxcloset=[]
        res=[]


        for x,y in points:
            dist=math.sqrt(x**2+y**2)
            heapq.heappush_max(maxcloset,[dist,[x,y]])
            if k < len(maxcloset) :
                heapq.heappop_max(maxcloset)

        for dist , point in maxcloset:
            res.append(point)


        return res



        