# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.


        if value < self.value: 
            if self.left: 
                self.left.insert(value)  
            else: 
                self.left = BST(value)  

        else: 
            if self.right: 
                self.right.insert(value) 
            else: 
                self.right = BST(value)  

        return self



    def contains(self, value):
        # Write your code here.
        

        if self is None: 
            return False 

        if self.value == value: 
            return True 

        elif value < self.value:
            # search left subtree 
            if self.left: 
                return self.left.contains(value) 
            else: 
                return False  

        else: 
            # search right subtree  
            if self.right: 
                return self.right.contains(value) 
            else:
                return False  



    def inorder_smallest(self): 

        if not self: 
            return None

        if self.left is None: 
            return self.value 

        return self.left.inorder_smallest() 




    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        # four cases: 
        #  case 1 - target is leaf.   just remove 
        #  case 2 - target has 1 child.  replace target with child 
        #  case 3 - target has 2 children.  replace with inorder successor 

        if self is None: 
            return None 

        if self.value == value: 
            # self is target to remove 
            
            # case 1 - leaf node 
            if self.left is None and self.right is None: 
                return None 

            # case 2 - one child.  return the child to replace target 
            if self.left is None and self.right: 
                return self.right 

            if self.right is None and self.left: 
                return self.left

            # case 3 - target has two children.  replace with inorder successor 
            inorder_val = self.right.inorder_smallest() 
            self.value = inorder_val
            self.right = self.right.remove(inorder_val) 


        else: 

            if value < self.value: 
                # hunt in left subtree 
                if self.left: 
                    self.left = self.left.remove(value) 

            else: 
                # hunt in right subtree 
                if self.right: 
                    self.right = self.right.remove(value) 

        return self



if __name__ == '__main__':


    root = BST(10)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.right = BST(5)
    root.right = BST(15)
    root.right.left = BST(13)
    root.right.left.right = BST(14)
    root.right.right = BST(22)

    root.insert(12)
    print((root.right.left.left.value == 12)) 

    print(root.contains(15))

    root.remove(10)
    print(not root.contains(10))
    print(root.value == 12)
