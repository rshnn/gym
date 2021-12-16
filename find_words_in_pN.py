


alphabet = ["abc", "def", "ghi", "jkl", "mno", "pqr", "stuv", "wxyz"]

idx_lookup = {} 
for idx, char_set in enumerate(alphabet): 
    for char in char_set: 
        idx_lookup[char] = idx + 2 




class TrieNode(): 

    def __init__(self, letter, idx, next=dict(), is_word=False, word=None): 
        self.letter = letter
        self.next = next 
        self.idx = idx 
        self.is_word = is_word 
        self.word = word 


    def __str__(self): 
        return f"{self.letter}"

    def __repr__(self): 
        return self.__str__() 


    def insert(self, word): 
        """ inserts word into trie.  self should be the root.""" 

        tmp = self 
        is_full_word = False 
        word_ = None 

        for idx, char in enumerate(word): 

            # last character of the word.  
            # this next node should contain full word metadata 
            if idx == len(word) - 1: 
                is_full_word = True 
                word_ = word  

            if char in tmp.next.keys(): 
                if is_full_word: 
                    tmp[char].is_word = True 
                    tmp[char].word = word  
            else: 
                tn = TrieNode(char, idx_lookup[char], {}, is_full_word, word_) 
                tmp.next[char] = tn  
            
            tmp = tmp.next[char] 


    def find_child_nodes(self, idx):  
        """ returns list of children nodes of node.idx if present under self 
        """
        out = list() 
        for child in self.next.values(): 
            if child.idx == idx: 
                out.append(child) 

        return out 


    def search_word(self, word): 
        """ returns true if word exists in trie.  run this on root only""" 

        tmp = self 

        for char in word: 

            if char in tmp.next.keys(): 
                tmp = tmp.next[char]
            else: 
                return False 

        return tmp.is_word 


from collections import deque

def find_words_in_pN(pN, root): 


    result = list() 
    left, right = 0, 0 

    while left < len(pN): 
        stack = deque() 

        idx = pN[left]
        nodes = root.find_child_nodes(int(idx))

        for n in nodes: 
            stack.append((n, left, right + 1))

        while stack: 
            n, l, r = stack.pop() 


            if n.is_word: 
                result.append(n.word)  

            # append next possible states 
            if r == len(pN)-1 :
                continue  

            idx = pN[r]
            next_nodes = n.find_child_nodes(int(idx))

            for n_ in next_nodes: 
                stack.append((n_, l, r + 1))



        left += 1 
        right = left 

    return result 




if __name__ == '__main__':
    

    words = "foo bar baz foobar emo cap car cat".split()  
    phoneNumber = "3662277"

    root = TrieNode(None, None) 
    # O(n) where n is number of words | O(n) for space 
    for word in words: 
        root.insert(word) 


    print(find_words_in_pN(phoneNumber, root))

