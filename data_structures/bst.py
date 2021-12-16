"""
Implementation of binary search tree 
"""


class BSTNode(): 

    def __init__(self, val, left=None, right=None): 
        self.val = val 
        self.left = None 
        self.right = None 
        self.count = 1 

    def __str__(self): 
        return f"({self.val}, l: {self.left}, r:{self.right})" 

    def __repr__(self): 
        return str(self.val)  


    def insert(self, data): 
        
        if data == self.val: 
            self.count += 1 
            return 

        if data < self.val: 

            if self.left is None: 
                self.left = BSTNode(data) 
                return 
            else: 
                self.left.insert(data) 

        else: 

            if self.right is None: 
                self.right = BSTNode(data)
                return 
            else: 
                self.right.insert(data)  

        return -1  


    def search(self, data): 
         
        if self.val == data: 
            return True

        if data < self.val: 
            # check left 
            if self.left is None: 
                return False
            else: 
                return self.left.search(data) 

        else: 
            # check right  
            if self.right is None: 
                return False 
            else: 
                return self.right.search(data) 

        raise ValueError()  


    def _get_first_inorder_traversal(self): 

        self.left._get_first_inorder_traversal()
        return self 
        self.right._get_first_inorder_traversal()


    def delete(self, data): 
        ... 





def inorder_traversal(root): 

    if root is not None: 
        inorder_traversal(root.left) 
        print(str(root.val), end=' ')
        inorder_traversal(root.right) 


if __name__ == '__main__':
    
    bst = BSTNode(10)
    bst.insert(12)
    bst.insert(323)
    bst.insert(2)

    inorder_traversal(bst)