

class Node():

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def print_list(self):

        tmp = self
        while tmp:
            print(tmp.val, end=' ')
            tmp = tmp.next


def reverse_list(head):

    if not head:
        return None

    curr = head 
    prev = None 

    while True: 

        if not curr: 
            break 

        next_node_holder = curr.next 

        curr.next = prev 
        prev = curr 
        curr = next_node_holder


    return prev 


head = Node(10)
head.next = Node(12)
# head.next.next = Node(14)
# head.next.next.next = Node(16)

head.print_list() 
print() 
new_list = reverse_list(head)

new_list.print_list()
