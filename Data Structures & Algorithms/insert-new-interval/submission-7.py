class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        def overlap(a , b):
            if a[1]<b[0]:
                return 0,None
            elif b[1]<a[0]:
                return -1,None
            return 1,[min(a[0],b[0]),max(a[1],b[1])]
        precedent = False
        i=0
        if len(newInterval)==0:
            return intervals
        if len(intervals)==0:
            return [newInterval]

        while  i < len(intervals):
            
            interval=intervals[i]
            comp,merged=overlap(interval ,newInterval)
            if comp==1:
                newInterval=merged
                intervals[i]=newInterval
                if precedent:
                    del intervals[i-1]
                else:
                    precedent=True
                    i+=1

            elif comp==-1:
                if precedent :
                    return intervals
                return intervals[:i]+[newInterval]+intervals[i:]
            elif comp==0:
                i+=1
        if not precedent :
            return intervals + [newInterval]
        else :
            return intervals




            

