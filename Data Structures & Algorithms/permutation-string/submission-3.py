class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        lens1=len(s1)
        perms1={}
        perms2={}
        for i  in range(len(s1)-1):
            perms1[s1[i]]=perms1.get(s1[i],0)+1
            perms2[s2[i]]=perms2.get(s2[i],0)+1
        perms1[s1[len(s1)-1]]=perms1.get(s1[len(s1)-1],0)+1
        i=0
        print(perms1)
        while i+lens1<=len(s2):
            perms2[s2[i+lens1-1]]=perms2.get(s2[i+lens1-1],0)+1
            print(perms2)
            if perms1 == perms2 :
                return True
            perms2[s2[i]]=perms2.get(s2[i],0)-1
            if perms2[s2[i]] == 0:
                del perms2[s2[i]]
            i+=1
            


        return False


        




   