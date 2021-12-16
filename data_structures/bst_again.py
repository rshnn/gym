


class BSTNode(): 

    def __init__(self, value, left=None, right=None): 
        self.value = value 
        self.left = left 
        self.right = right  



    def insert(self, value): 


        if value < self.value: 
            # search left subtree 
            if not self.left: 
                self.left = BSTNode(value) 
            else: 
                self.left.insert(value) 

        else: 
            # search right subtree 
            if not self.right: 
                self.right = BSTNode(value) 
            else: 
                self.right.insert(value)  



    def find(self, value): 

        if value == self.value: 
            return True 

        elif value < self.value: 
            if not self.left: 
                return False 
            else: 
                self.left.search(value) 

        else: 
            if not self.right: 
                return False 
            else: 
                self.right.search(value)  


    def get_smallest(self): 

        if not self.left: 
            return self.value 

        get_smallest(self.left)


    def remove(self, value): 

        if value < self.value: 
            # search left subtree 
            if not self.left: 
                return -1 
            else: 
                self.left = self.left.remove(value) 


        elif value > self.value: 
            # search right subtree 
            if not self.right: 
                return -1 
            else: 
                self.right = self.right.remove(value) 


        else: 
            # found the target node to remove 
            # case 1 its a leaf node, return None 

            if not self.left and not self.right: 
                return None 

            # case 2 its got 1 child, replace with child  
            if not self.right and self.left: 
                return self.left  
            if not self.left and self.right: 
                return self.right 

            # case 3 its got two childrens, replace with inorder successor  
            inorder_successor = self.right.get_smallest()  
            self.value = inorder_successor  
            self.right.remove(inorder_successor)  

        return self 



import math 

def validate_bst(root): 

    # handle null root 

    left_max = -math.inf 
    right_min = math.inf 

    return inorder_validate(root, left_max, right_min) 


def inorder_validate(root, left_max, right_min): 

    # handle null root 
    if not root: 
        return True 

    if left_max > root.value: 
        return False 
    if right_min < root.value: 
        return False 

    left_subtree_valid = inorder_validate(root.left, left_max, root.value) 
    right_subtree_valid = inorder_validate(root.right, root.value, right_min)   

    return left_subtree_valid and right_subtree_valid 


def inorder(root): 
    if not root: 
        return 

    inorder(root.left) 
    print(root.value, end=' ') 
    inorder(root.right) 


def postorder(root): 
    if not root: 
        return 

    postorder(root.left) 
    postorder(root.right) 
    print(root.value, end=' ') 



head = BSTNode(3)
head.insert(4) 
head.insert(2)
head.insert(1) 
head.insert(12) 
head.right.right.left = BSTNode(13)


print(validate_bst(head))

inorder(head)
