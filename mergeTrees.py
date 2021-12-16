
from collections import deque 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right  

    def __str__(self): 
        return f"({self.val}, {self.left}, {self.right})"

    def __repr__(self): 
        return str(self.val)  



def build_tree_preorder(arr): 

    head = TreeNode(arr[0])
    tmp = head 

    for item in arr[1:]: 

        insert_preorder(tmp, item)

    return head 


def insert_preorder(root, item): 

    queue = deque() 
    queue.append(root) 


    while queue: 

        tmp = queue.popleft()

        if tmp.left is None: 
            new_node = TreeNode(item) 
            if item is None: 
                new_node = None 
            tmp.left = new_node
            return 

        elif tmp.right is None: 
            new_node = TreeNode(item) 
            if item is None: 
                new_node = None 
            tmp.right = new_node
            return 

        else: 
            queue.append(tmp.left)
            queue.append(tmp.right) 


    return False 


def delete_leaf(root, item): 

    if root.val == item: 
        return None 

    else: 
        if root.left is not None: 
            root.left = delete_leaf(root.left, item) 
            return root 

        elif root.right is not None: 
            root.right = delete_leaf(root.right, item) 
            return root 

        else: 
            print("not found")
            return False 


def print_preorder(root): 

    queue = deque() 
    queue.append(root) 

    while queue: 

        tmp = queue.popleft() 

        if tmp is None: 
            continue 

        print(tmp.val, end=' ')

        queue.append(tmp.left) 
        queue.append(tmp.right) 

    return 


def mergeTrees(root1, root2): 
    
    if not root1 and not root2: 
        return None 

    v1 = root1.val if root1 else 0 
    v2 = root2.val if root2 else 0 

    new_node = TreeNode(v1 + v2)

    new_node.left = mergeTrees(root1.left if root1 else None, 
                                root2.left if root2 else None)

    new_node.right = mergeTrees(root1.right if root1 else None, 
                                root2.right if root2 else None) 




null = None 

if __name__ == "__main__":

    root1 = [1,3,2,5]  
    root2 = [2,1,3,null,4,null,7] 
    

    t1 = build_tree_preorder(root1)
    t2 = build_tree_preorder(root2)


    mergeTrees(t1, t2)



    # print(mergeTrees(root1, root2)) 


