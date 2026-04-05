class Solution:

    def encode(self, strs: List[str]) -> str:
        lenlist=[]
        res=""
        for s in strs:
            lenlist.append(str(len(s)))
            res+=s
        res+="°"
        res+=",".join(lenlist)
        return res
        



    def decode(self, s: str) -> List[str]:
        split = s.split("°")
        print(split)
        strs= split[0]
        lenlist = split[1].split(",")



        
        
        res=[]
        i=0
        if  len(lenlist)==0:
            return res

        print(lenlist)
        for lens in lenlist:
            if lens!="" :
                lens=int(lens)
                res.append(strs[i:i+lens]) 
                i+=lens
            

            
            
        return res



