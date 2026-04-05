class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCount = Counter(tasks)
        maxHeap =[-count for count in taskCount.values() ]
        heapq.heapify(maxHeap)
        
        time=0
        q=deque() #[-cnt,idletime]
        
        while q or maxHeap :
            time+=1
            print(time)

            if maxHeap :
                cnt=1+heapq.heappop(maxHeap)
                if cnt :
                    q.append([cnt,time+n])
            
            if q and q[0][1]==time:
                heapq.heappush(maxHeap,q.popleft()[0])
        return time
           
