"""
Implementation of Trie datastructure 
"""

class TrieNode(): 

    def __init__(self, val, full_word=False, children=None): 
        self.val = val 
        self.full_word = False 
        self.children = dict()    

    def __str__(self): 
        return str(self.val)  

    def __repr__(self): 
        return self.__str__() 


class Trie(): 

    def __init__(self): 
        self.root = TrieNode(-1)
         

    def insert(self, s): 
        
        curr = self.root 

        for char in s: 

            if char in curr.children.keys():  
                curr = curr.children[char] 
                continue 

            tmp = TrieNode(char) 
            curr.children[char] = tmp 

            curr = tmp 

        curr.full_word = True 
        return 

    def search(self, s): 
        
        curr = self.root 

        for char in s: 

            if char in curr.children.keys():  
                 curr = curr.children[char] 
                 continue 

            else: 
                return False 

        if curr.full_word: 
                return True 
        else: 
                return False  


    def startsWith(self, s): 

        curr = self.root 

        for char in s: 

            if char in curr.children.keys():  
                 curr = curr.children[char] 
                 continue 

            else: 
                return False 

        return True 
          


if __name__ == '__main__':
    
    trie = Trie()
    trie.insert("apple")
    trie.insert("banana")
    trie.insert("applesauce")
    trie.insert("aggony")

    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    

    print(trie.search("applesauc"))
    print(trie.search("applesauce"))
    print(trie.startsWith("agggg"))