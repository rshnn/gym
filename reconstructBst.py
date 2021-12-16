# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def getDfsOrder(node, values):
    if node is None:
        return
    values.append(node.value)
    getDfsOrder(node.left, values)
    getDfsOrder(node.right, values)
    return values

from collections import deque 
import math 


def reconstructBst(array):
    # Write your code here.
    
    if len(array) == 0: 
        return None 

    global root_idx 
    root_idx = 0   
    head = recursive_add(array, -math.inf, math.inf) 

    return head



def recursive_add(array, minval, maxval): 
    global root_idx 

    if root_idx >= len(array): 
        return None 

    val_to_add = array[root_idx]

    if minval > val_to_add  or val_to_add > array[root_idx]: 
        return None 

    root_idx += 1 
    left_subtree = recursive_add(array, minval, val_to_add)
    right_subtree = recursive_add(array, val_to_add, maxval) 
    return BST(val_to_add, left_subtree, right_subtree) 


if __name__ == '__main__':

    preOrderTraversalValues = [10, 4, 2, 1, 3, 17, 19, 18]

    tree = BST(10)
    tree.left = BST(4)
    tree.left.left = BST(2)
    tree.left.left.left = BST(1)
    tree.left.right = BST(3)
    tree.right = BST(17)
    tree.right.right = BST(19)
    tree.right.right.left = BST(18)
    expected = getDfsOrder(tree, [])

    actual = reconstructBst(preOrderTraversalValues)
    actualDfsOrder = getDfsOrder(actual, [])

    print(expected)
    print(actualDfsOrder)
    print(preOrderTraversalValues)
