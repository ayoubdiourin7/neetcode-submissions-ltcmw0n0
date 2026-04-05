class Solution:
    def isNStraightHand(self, hands: List[int], groupSize: int) -> bool:
        

        count={}
        for hand in hands:
            count[hand]=1+count.get(hand,0)
        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            e=minH[0]
            i=0

            while i<=groupSize-1:
                if (e+i) in count:
                    count[e+i]-=1
                    if count[e+i] == 0:
                        heapq.heappop(minH)
                else:
                    return False
                i+=1
        return True

        