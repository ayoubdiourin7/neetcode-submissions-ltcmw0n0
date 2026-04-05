class Node:
    def __init__(self , value , next_node):
        self.val= value
        self.nxt = next_node

class LinkedList:
    
    def __init__(self):
        self.head= Node(None,None)
        self.ln = 0
        

    
    def get(self, index: int) -> int:
        index = index +1
        if index <= self.ln  :
            currNode = self.head
            for i in range(0,index):
                currNode = currNode.nxt
            return currNode.val
        return -1


        
    def insertTail(self, val: int) -> None:
        curNode =self.head 
        while curNode.nxt is not None:
            curNode = curNode.nxt
        curNode.nxt = Node(val,None)
        self.ln +=1
        

    def insertHead(self, val: int) -> None:
        node=Node(val ,self.head.nxt) 
        self.head.nxt=node
        self.ln +=1
        

    def remove(self, index: int) -> bool:
        if index +1<= self.ln  :
            currNode = self.head
            for i in range(0,index):
                currNode = currNode.nxt
            self.ln -=1
            currNode.nxt = currNode.nxt.nxt
            
            return True
        return False 
        

    def getValues(self) -> List[int]:
        res = []
        curNode = self.head.nxt  
        while curNode is not None:
            res.append(curNode.val)
            curNode = curNode.nxt
        return res

        
