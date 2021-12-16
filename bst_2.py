


class BSTNode(): 

    def __init__(self, val, left=None, right=None): 
        self.val = val 
        self.left = left  
        self.right = right  


    def __str__(self): 
        return f"{self.val}" 


    def __repr__(self): 
        return self.__str__()  


    def insert(self, val): 


        if val == self.val: 
            return 

        elif val < self.val: 

            if self.left: 
                self.left.insert(val)  
            else: 
                self.left = BSTNode(val) 

        else: 

            if self.right: 
                self.right.insert(val)  
            else: 
                self.right = BSTNode(val)  




    def search(self, val): 

        if val == self.val:  
            return True 

        elif val < self.val:  

            if self.left:
                return self.left.search(val)
            else: 
                return False 

        else: 
            if self.right: 
                return self.right.search(val) 
            else: 
                return False  




    def delete(self, val): 

        if val == self.val:  
            # self is the node to delete 
            
            # case 1:  target is leaf node 
            if self.left is None and self.right is None: 
                return None 
            
            # case 2:  target has 1 child  
            if self.left is None and self.right: 
                return self.right 

            if self.right is None and self.left: 
                return self.left    

            # case 3:  target has 2 childrens
            self.val = self.right.inorder_smallest() 
            self.right = self.right.delete(self.val)  

        elif val < self.val: 

            if self.left: 
                self.left = self.left.delete(val)  


        else: 
            if self.right: 
                self.right = self.right.delete(val)    

        return self 




    def inorder_smallest(self): 

        if not self.left: 
            return self.val 
        else: 
            return self.left.inorder_smallest() 


def inorder_print(head): 

    if not head:
        return 


    inorder_print(head.left) 
    print(head.val, end=' ')
    inorder_print(head.right) 
    





if __name__ == '__main__':
    head = BSTNode(3)
    head.insert(4) 
    head.insert(2)
    head.insert(1) 

    inorder_print(head)
    head = head.delete(3)
    print() 
    inorder_print(head)

    