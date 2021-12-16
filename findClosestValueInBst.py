

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



from collections import deque  
import math 


def findClosestValueInBst(tree, target):
    # Write your code here.

    curr_best = math.inf    

    if tree is None: 
        return None 

    queue = deque() 
    queue.append(tree)  

    while queue: 

        tmp = queue.popleft() 

        if tmp is None: 
            return curr_best 

        if tmp.value == target: 
            return target 

        else: 
            dif = target-tmp.value  

            # replace curr_best if smaller 
            if abs(target-curr_best) > abs(dif): 
                curr_best = tmp.value   

            if dif > 0: 
                # traverse right bc tmp is too small 
                queue.append(tmp.right)

            else: 
                # traverse left bc tmp is too big 
                queue.append(tmp.left)  

    return curr_best  



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
    expected = 13
    actual = findClosestValueInBst(root, 12)
    
    print(actual) 