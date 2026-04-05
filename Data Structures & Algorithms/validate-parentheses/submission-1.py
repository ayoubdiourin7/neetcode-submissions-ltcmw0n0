class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"]":"[","}":"{",")":"("}
        q=deque()
        for char in s:
            if char in dic :
                openbr = dic.get(char)
                if len(q) == 0 or not (openbr == q.pop()):
                    return False  
            else:
                q.append(char)

        return len(q)==0
        