class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last={}
        res=[]

        for i,c in enumerate(s):
            last[c]=i
        
        lensubStr=0
        lastindex=0
        for i,c in enumerate(s):
            lensubStr+=1
            if lastindex<=last[c]:
                lastindex=last[c]

            if lastindex==i:
                res.append(lensubStr)
                lensubStr=0
        return res



        

        