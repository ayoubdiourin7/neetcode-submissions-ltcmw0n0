class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        print(intervals)
        res=[]
        newInterval = intervals[0]
        for i in range(1,len(intervals)):
            interval=intervals[i]
            if newInterval[1]<interval[0]:
                res.append(newInterval)
                newInterval=intervals[i]
            elif newInterval[0]>interval[1]:
                res.append(interval)
            else :
                newInterval = [min(newInterval[0],interval[0]), max(newInterval[1],interval[1])]
                              
                            

        return res +[newInterval]


        