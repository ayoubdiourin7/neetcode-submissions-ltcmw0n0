class Solution:
    def isNStraightHand(self, hands: List[int], groupSize: int) -> bool:
        

        count={}
        for hand in hands:
            count[hand]=1+count.get(hand,0)

        while count.keys():
            e=min(count.keys())
            i=0

            while i<=groupSize-1:
                if (e+i) in count:
                    count[e+i]-=1
                    if count[e+i] == 0:
                        del count[e+i]
                else:
                    return False
                i+=1
        return True

        