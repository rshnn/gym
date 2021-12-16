
from collections import deque 

class Node:
    def __init__(self, val= 0, left= None, right= None, next= None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next



def build_levelorder(arr): 

    q = deque() 
    head = Node(arr[0])
    tmp = head  

    for item in arr[1:]: 

        if tmp.left is None: 
            tmp.left = Node(item)
            q.append(tmp.left)

        elif tmp.right is None: 
            tmp.right = Node(item) 
            q.append(tmp.right)
            tmp = q.popleft() 


    return head 
        



def print_levelorder(root):


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



def print_inorder(root): 

    if root is None: 
        return 

    print_inorder(root.left) 
    print(root.val, end=' ')
    print_inorder(root.right) 


def connect(root): 
    
    if root is None: 
        return root      

    q = deque()
    q.append(root) 

    while q: 

        tmp = q.popleft()

        if tmp.left: 
            tmp.left.next = tmp.right 

            if tmp.next: 
                tmp.right.next = tmp.next.left 

            q.append(left) 
            q.append(right) 






null = None 

if __name__ == "__main__":

    root1 = [1,2,3,4,5,6,7]  
    
    t1 = build_levelorder(root1)
    print_levelorder(t1)
    print()
    print_inorder(t1)


    # connect(t1, t2)



    # print(mergeTrees(root1, root2)) 


