

class Node(): 
    def __init__(self, value, next=None): 
        self.value = value 
        self.next = next 
    
    def insert(self, value): 
        tmp = self 
    
        while tmp: 
            if not tmp.next: 
                tmp.next = Node(value) 
                return 
            else: 
                tmp = tmp.next 



    def remove(self, value):  

        tmp = self

        if tmp.value == value: 
            return tmp.next 

        while tmp: 
            if tmp.next and tmp.next.value == value: 
                # found the value to remove.  rearrange pointers 
                tmp.next = tmp.next.next 
            else: 
                tmp = tmp.next  

        return self 
        


    def print_list(self): 

        tmp = self 
        while tmp: 
            print(tmp.value) 
            tmp = tmp.next  




n = Node(10)
n.insert(12)
n.insert(23)
n.insert(34)

n = n.remove(10) 

n.print_list() 

