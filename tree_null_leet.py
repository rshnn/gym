"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
 

Example 1:



Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
 

Constraints:

The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000


"""

# Definition for a Node.

class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __str__(self):
        return str(self.val)


    def __repr__(self): 
        return str(self) 


from collections import deque 

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        q = deque([root])  
        dfs(root, q)

        return root 



def dfs(node, q): 


    cnt = 1 
    level = 1 

    while len(q) != 0: 

        n = q.popleft()      
        if n: 
            # print(n.val, q, '\t', cnt)
            

            # not a leaf node 
            if n.left is not None and n.right is not None: 
                
                q.append(n.left)
                q.append(n.right)


            if len(q) == 0: 
                n.next = None 
            else: 
                n.next = q[0]


            if cnt == (2**level - 1): 
                # print('end of row')
                n.next = None 
                level += 1

            cnt += 1 


    return node 


# 1, 3, 7, 15 



### Helper funcs 



# Function to insert nodes in level order  
def build_tree_level_order(arr, root, i, n): 
      
    # Base case for recursion  
    if i < n: 
        temp = Node(arr[i])  
        root = temp  
  
        # insert left child  
        root.left = build_tree_level_order(arr, root.left, 
                                     2 * i + 1, n)  
  
        # insert right child  
        root.right = build_tree_level_order(arr, root.right, 
                                      2 * i + 2, n) 
    return root 



def dfs_check(node): 

    if node: 

        print(node.val, " points to ", node.next)

        dfs_check(node.left) 
        dfs_check(node.right)




if __name__ == '__main__':
    
    arr = [1,2,3,4,5,6,7]
    root = Node()
    root = build_tree_level_order(arr, root, 0, len(arr))

    sol = Solution()
    root = sol.connect(root)

    print('TEST')
    dfs_check(root) 

