class LinkedList:
    
    def __init__(self):
        self.lst=[]
        

    
    def get(self, index: int) -> int:
        if index<=len(self.lst) -1 and len(self.lst)>0:
            return self.lst[index]
        return -1
        

    def insertTail(self, val: int) -> None:
        self.lst.append(val)
        

    def insertHead(self, val: int) -> None: 
        self.lst = [val] + self.lst
        

    def remove(self, index: int) -> bool:
        if index<=len(self.lst) -1 and len(self.lst)>0:
            print(index)
            print(len(self.lst))
            del self.lst[index]
            return True
        return False
        

    def getValues(self) -> List[int]:
        return self.lst
        
