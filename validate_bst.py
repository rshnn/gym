# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



from collections import deque
import math 



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


def preOrderTraverse(tree, array):
    # Write your code here.

    if tree is None: 
        return None 

    array.append(tree.value) 
    preOrderTraverse(tree.left, array) 
    preOrderTraverse(tree.right, array)   

    return array 


def postOrderTraverse(tree, array):
    # Write your code here.

    if tree is None: 
        return None 

    postOrderTraverse(tree.left, array) 
    postOrderTraverse(tree.right, array)   
    array.append(tree.value) 

    return array 



if __name__ == '__main__':

    root = BST(10)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.right = BST(5)
    root.right = BST(15)
    # root.right.left = BST(13)
    # root.right.left.right = BST(14)
    root.right.right = BST(22)


    print(inOrderTraverse(root, []))
    print(preOrderTraverse(root, list()))
    print(postOrderTraverse(root, []))        