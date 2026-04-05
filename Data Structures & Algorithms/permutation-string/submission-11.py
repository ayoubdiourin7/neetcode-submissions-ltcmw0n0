class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False

        lens1=len(s1)
        perms1=Counter(s1)
        perms2=Counter(s2[:len(s1)])

  
        for i in range(0,len(s2)-lens1):
            if perms1 == perms2 :
                return True

            perms2[s2[i+lens1]]=perms2.get(s2[i+lens1],0)+1
            perms2[s2[i]]=perms2.get(s2[i])-1
            if perms2[s2[i]] == 0:
                del perms2[s2[i]]
    
        return perms1 == perms2


        




   