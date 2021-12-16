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

        tmp = self 

        while True: 
            if value < tmp.value: 
                if not tmp.left: 
                    tmp.left = BST(value)  
                    break  
                else: 
                    tmp = tmp.left
                    continue 
            else: 
                if not tmp.right: 
                    tmp.right= BST(value) 
                    break 
                else: 
                    tmp = tmp.right 
                    continue 

        return self 



    def contains(self, value):
        # Write your code here.
        
        tmp = self

        while tmp is not None: 

            if value < tmp.value: 
                # search in left subtree 
                if not tmp.left: 
                    return False 
                else: 
                    tmp = tmp.left 
                    continue  

            elif value > tmp.value: 
                # search in right subtree 
                if not tmp.right: 
                    return False 
                else: 
                    tmp = tmp.right 
                    continue 

            else: 
                # target found 
                return True 
         



    def inorder_smallest(self): 
        
        tmp = self 
    
        while True: 
            if tmp.left is None: 
                return tmp.value 

            tmp = tmp.left  


    def remove(self, value, parent=None):
        # Write your code here.
        # Do not edit the return statement of this method.
        # four cases: 
        #  case 1 - target is leaf.   just remove 
        #  case 2 - target has 1 child.  replace target with child 
        #  case 3 - target has 2 children.  replace with inorder successor 
        
        tmp = self  

        while tmp is not None: 

            if value < tmp.value: 
                # hunt in left subtree 
                parent = tmp 
                tmp = tmp.left 
                continue 

            elif value > tmp.value: 
                # hunt in right subtree 
                parent = tmp 
                tmp = tmp.right 
                continue  

            else: 
                # tmp is target to remove... 

                # case 3 target has two children.  replace with inorder successor 
                if tmp.left and tmp.right: 
                    inorder_successor = tmp.right.inorder_smallest() 
                    tmp.value = inorder_successor 
                    tmp.right.remove(inorder_successor, tmp) 
                    break 

                # if target is root 
                if parent is None: 
                    if tmp.left is None and tmp.right is None: 
                        pass   
                        
                    if tmp.right is None and tmp.left: 
                        tmp.value = tmp.left.value 
                        tmp.right = tmp.left.right 
                        tmp.left = tmp.left.left 

                    if tmp.left is None and tmp.right: 
                        tmp.value = tmp.right.value 
                        tmp.left = tmp.right.left 
                        tmp.right = tmp.right.right   


                # otherwise 
                else: 
                    # case 1 target is leaf node 
                    if tmp.left is None and tmp.right is None: 
                        if parent.left == tmp:  parent.left = None 
                        else: parent.right = None

                    # case 2 target has 1 child.  replace target with child 
                    if tmp.right is None and tmp.left: 
                        if parent.left == tmp:  parent.left = tmp.left 
                        else: parent.right = tmp.left  

                    if tmp.left is None and tmp.right: 
                        if parent.left == tmp: parent.left = tmp.right 
                        else: parent.right = tmp.right  


                break 

        return self 


def print_inorder(root): 

    if not root: 
        return 


    print_inorder(root.left) 
    print(root.value, end=' ') 
    print_inorder(root.right) 


if __name__ == '__main__':


    root = BST(10)
    root.insert(15).insert(5) 


    print_inorder(root) 
    print() 

    print(root.remove(10))

    print_inorder(root) 
    print() 


    print(not root.contains(10))
    print(root.value == 12)
