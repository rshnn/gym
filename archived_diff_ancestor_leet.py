"""
Given the root of a binary tree, find the maximum value V for which there exist different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.

 

Example 1:


Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
Example 2:


Input: root = [1,null,2,null,0,3]
Output: 3
 

Constraints:

The number of nodes in the tree is in the range [2, 5000].
0 <= Node.val <= 105
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    max_so_far = 0 

    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        tmp = root 

        if tmp: 

            self.maxAncestorDiff(tmp.left)
            self.maxAncestorDiff(tmp.right) 

            print("running head dfs on {}".format(tmp.val))
            self.dfs(tmp, tmp.val)

        return self.max_so_far 



    def dfs(self, node, root_val): 


        if node: 
            # print("Im in passing through {}".format(node.val))

            self.dfs(node.left, root_val) 
            self.dfs(node.right, root_val) 

            diff = abs(root_val - node.val) 

            if diff > self.max_so_far: 
                self.max_so_far = diff 



            # print("On node {}.\nDiff is {}\nMax so far is {}\n\n".format(
            #     node.val, diff, self.max_so_far))






## Code to build tree and main 

def insertLevelOrder(arr, root, i, n): 
      
    # Base case for recursion  
    if i < n: 

        if arr[i] is None: 
            return 
        temp = TreeNode(arr[i])  
        root = temp  
  
        # insert left child  
        root.left = insertLevelOrder(arr, root.left, 
                                     2 * i + 1, n)  
  
        # insert right child  
        root.right = insertLevelOrder(arr, root.right, 
                                      2 * i + 2, n) 
    return root 



if __name__ == "__main__": 

    null = None 
    arr = [8,3,10,1,6,null,14,null,null,4,7,13]
    # arr = [1, 2, 3]

    root = None 
    n=len(arr)

    root = insertLevelOrder(arr, root, 0, n) 

    soln = Solution()
    print(soln.maxAncestorDiff(root))