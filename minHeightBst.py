import math 
from collections import deque  

def validateBst(root): 
    return inorder_traversal(root) 


def inorder_traversal(root, minimum=-math.inf, maximum=math.inf): 

    if not root: 
        return True 

    if root.value < minimum or root.value >= maximum: 
        return False 

    # validate left subtree
    left_valid = inorder_traversal(root.left, minimum, root.value) 

    return left_valid and inorder_traversal(root.right, root.value, maximum) 



def inOrderTraverse(tree, array):
    # Write your code here.

    if tree is None: 
        return None 

    inOrderTraverse(tree.left, array) 
    array.append(tree.value) 
    inOrderTraverse(tree.right, array)   

    return array 

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)



def getTreeHeight(tree, height=0):
    if tree is None:
        return height
    leftTreeHeight = getTreeHeight(tree.left, height + 1)
    rightTreeHeight = getTreeHeight(tree.right, height + 1)
    return max(leftTreeHeight, rightTreeHeight)



def divide_conq_insert(head, array): 

    if len(array) == 0:
        return head 

    mid = len(array) // 2
    head.insert(array[mid])
    print(array[mid])

    divide_conq_insert(head, array[:mid])
    divide_conq_insert(head, array[mid+1:])

    return head 



def minHeightBst(array):

    if len(array) == 0: 
        return None 

    if len(array) == 1: 
        return BST(array[0])

    # if len(array) == 2: 
    #     head = BST(array[0]) 
    #     head.insert(array[1])
    #     return head 

    mid = len(array) // 2 
    head = BST(array[mid]) 
    
    head = divide_conq_insert(head, array[:mid])
    head = divide_conq_insert(head, array[mid+1:])
    return head 

if __name__ == '__main__':

    array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
    array = [1] 
    array = [1, 2]


    tree = minHeightBst(array)

    print(validateBst(tree))

    print(getTreeHeight(tree), 4)

    print(inOrderTraverse(tree, []))

    # print(inOrder, [1, 2, 5, 7, 10, 13, 14, 15, 22])
