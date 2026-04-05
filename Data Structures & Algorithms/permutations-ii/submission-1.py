class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res=[]

        def dfs(ori ,perm):
            if len(ori)==0:
                res.append(perm[::])
                return
            for j in range(len(ori)):
                if 1<=j and ori[j-1]==ori[j]:
                    continue
                perm.append(ori[j])
                dfs(ori[:j]+ori[j+1:] ,perm)
                perm.pop()
        dfs(nums,[])
        return res


        

