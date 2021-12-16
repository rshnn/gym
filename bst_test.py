


class Node(): 
    def __init__(self, value, left=None, right=None): 

        self.value = value 
        self.left = left 
        self.right = right

    def __str__(self): 
        return f"{self.value}"

    def __repr__(self): 
        return self.__str__() 


    def insert(self, value): 

        if value < self.value: 
            if not self.left: 
                self.left = Node(value) 
            else: 
                self.left.insert(value)  

        else: 
            if not self.right: 
                self.right = Node(value) 
            else: 
                self.right.insert(value)  


def inorder_print(root): 

    if not root: 
        return 

    inorder_print(root.left) 
    print(root.value, end=' ')
    inorder_print(root.right) 


def build_tree(arr):

    root = Node(arr[0])

    for item in arr[1:]: 
        root.insert(item)

    return root 



def stop_at_k(root, k):

    counter = [k]
    result = [None]

    def inorder(root): 

        if not root: 
            return 

        counter[0] -= 1 
        if counter[0] == 0: 
            print('found it')
            result[0] = root.value 

        if counter[0] > 0: 
            inorder(root.left) 


        if counter[0] > 0: 
            inorder(root.right) 


    inorder(root) 
    return result 





arr = [4, 2, 4, 3, 5, 6, 12]
root = build_tree(arr)
inorder_print(root) 
print()

# inorder_var(root, [0])

print(stop_at_k(root, 4))

arr.copy() 