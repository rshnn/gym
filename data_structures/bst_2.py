""" Binary search tree implementation 
"""


class BSTNode():

    def __init__(self, val, left=None, right=None): 

        self.val = val 
        self.left = left 
        self.right = right


    def __str__(self): 
        return f"({self.val})"

    def __repr__(self): 
        return self.__str__() 



    def insert(self, val): 
        
        if val == self.val: 
            return  

        elif val < self.val: 
            if self.left is None: 
                n = BSTNode(val)
                self.left = n 
            else: 
                self.left.insert(val) 

        else: 
            if self.right is None: 
                n = BSTNode(val) 
                self.right = n 
            else: 
                self.right.insert(val) 


    def search(self, val):

        if val == self.val: 
            return True 

        elif val < self.val: 
            if self.left is None: 
                return False 
            else: 
                return self.left.search(val)

        else: 
            if self.right is None: 
                return False 
            else: 
                return self.right.search(val) 



    def delete(self, val): 
        """
        Three cases: 
        A:  leaf node.  Just pluck away 
        B:  one child.  Replace target with the child 
        C:  both children exist.  Replace target with next inorder 
        """ 

        if val == self.val: 
            # conduct the delete
            # case A 
            if self.left is None and self.right is None: 
                return None 

            # case B 
            if self.left is None: 
                return self.right 

            if self.right is None: 
                return self.left 


            # case C 
            min_node = self.right.get_min_node() 
            self.val = min_node.val 
            self.right = self.right.delete(min_node.val) 




        elif val < self.val: 
            if self.left is not None: 
                self.left = self.left.delete(val)

        else: 
            if self.right is not None: 
                self.right = self.right.delete(val) 


        return self 





    def get_min_node(self): 

        if self.left is None: 
            return self 
        else: 
            self.left.get_min_node()



    def get_max_node(self): 

        if self.right is None: 
            return self 
        else: 
            self.right.get_max_node()



def inorder(head): 
    tmp = head 

    if tmp is None: 
        return 

    inorder(tmp.left)
    print(tmp.val, end=' ')
    inorder(tmp.right)

    return 


def make_BST(arr): 

    head = BSTNode(arr[0])

    for item in arr[1:]: 
        head.insert(item) 

    return head 

counter = 0 

def get_nth(node, idx, counter): 

    if not node: 
        return 

    print(f'on node {node.val} and counter is {counter}')
    get_nth(node.left, idx, counter) 

    counter += 1 
    if counter == idx: 
        print(node.val) 

    get_nth(node.right, idx, counter) 


if __name__ == '__main__':

    head = BSTNode(3)
    head.insert(4) 
    head.insert(2)
    head.insert(1) 

    inorder(head)
    print()
    head = head.delete(3)
    inorder(head)

    print('\nhere')
    val = get_nth(head, 1, counter=0) 
