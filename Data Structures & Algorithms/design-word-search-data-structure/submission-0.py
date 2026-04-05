class TriNode:

    def __init__(self):
        self.is_end=False
        self.noods={}

class WordDictionary:

    def __init__(self):
        self.root=TriNode()

    def addWord(self, word: str) -> None:
        curNode =self.root
        for c in word:
            if c not in curNode.noods :
                curNode.noods[c]=TriNode()
            
            curNode=curNode.noods[c]

        curNode.is_end=True


    def search(self, word: str) -> bool:
        curNode =self.root
        for i , c in enumerate(word):
            if c == "."   :
                for nood in curNode.noods.values():
                    wordDic =WordDictionary()
                    wordDic.root=nood
                    if wordDic.search(word[i+1:]):
                        return True
                    
                return False 

            elif c not   in curNode.noods :
                return False
            
            curNode=curNode.noods[c]

        return curNode.is_end


        
