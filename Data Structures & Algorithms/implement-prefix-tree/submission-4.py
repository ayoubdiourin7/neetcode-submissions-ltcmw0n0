class PrefixTree:

    def __init__(self):
        self.is_end = False
        self.nodes={}

        

    def insert(self, word: str) -> None:
        
        currNode=self
        for c in word:
            if c not in currNode.nodes:
                currNode.nodes[c] = PrefixTree()
                
            currNode = currNode.nodes[c]
        
        currNode.is_end=True


    def search(self, word: str) -> bool:
        currNode=self
        for c in word:
            if c in currNode.nodes:
                currNode=currNode.nodes[c]
            else:
                return False

        return currNode.is_end
        

    def startsWith(self, prefix: str) -> bool:
        currNodes = self.nodes
        for c in prefix:
            if c in currNodes:
                currNodes=currNodes[c].nodes
            else:
                return False

        return True

        
        