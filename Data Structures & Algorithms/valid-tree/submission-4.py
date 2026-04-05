class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return False
        graph=[ [] for _ in range(n)]
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)

        visiting =  set()
        def dfs(node , prev):

            if node in visiting:
                return False
            


            visiting .add(node)
            for nextNode in graph[node]:
                if nextNode == prev:
                    continue
                if not dfs(nextNode,node):
                    return False


            return True 
        return dfs(0,-1) and len(visiting) == n

        
            


        