
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = [[] for _ in range(numCourses)]

        for (a,b) in prerequisites:
            graph[a].append(b)

        
        def dfs(a , visiting):
            if a in visiting :
                return False 

            if graph[a] == []:
                return True
            
            visiting.add(a)
            for pre in graph[a]:
                if not dfs(pre,visiting):
                    return False
            visiting.remove(a)
            graph[a]=[]
            return True
        for a in range(numCourses):
            
            if not dfs(a, set()):

                return False

        return True

        


        

    