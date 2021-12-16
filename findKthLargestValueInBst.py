# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    # Write your code here.

    meta_info = {'latest_val': None, 'count': 0} 
    inorder(tree, k, meta_info)
    return meta_info['latest_val'] 



def inorder(root, k, meta_info): 

    if not root or meta_info['count'] >= k: 
        return 

    inorder(root.right, k, meta_info) 
    
    if meta_info['count'] < k: 
        meta_info['count'] += 1
        meta_info['latest_val'] = root.value  
        inorder(root.left, k, meta_info) 


if __name__ == '__main__':
    root = BST(15)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.left.right = BST(3)
    root.left.right = BST(5)
    root.right = BST(20)
    root.right.left = BST(17)
    root.right.right = BST(22)


    k = 3
    expected = 17
    actual = findKthLargestValueInBst(root, k)
    print(actual) 
    # self.assertEqual(actual, expected)