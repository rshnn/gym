
import math 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def build_list(arr): 

    head = ListNode(arr[0])

    tmp = head 
    for i in range(1, len(arr)): 
        n = ListNode(arr[i]) 
        tmp.next = n 

        tmp = n 

    return head 

def print_list(head): 

    tmp = head 
    while tmp: 
        print(tmp.val, end=' ')
        tmp = tmp.next 


def removeNthFromEnd(head, n):
    
    # build idx dictionary 
    counter = 0 
    idx_dict = dict() 

    tmp = head 
    while tmp: 
        counter += 1 
        idx_dict[counter] = tmp 

        tmp = tmp.next  



    # remove Nth last element 
    target_idx = counter - n + 1 
    target = idx_dict[target_idx] 
    prev_target = target_idx - 1 
    next_target = target_idx + 1 

    if prev_target in idx_dict.keys(): 
        prev = idx_dict[prev_target]
    else: 
        # removing head
        return target.next 

    if next_target in idx_dict.keys(): 
        nxt = idx_dict[next_target]
    else: 
        # removing tail 
        nxt = None 

    prev.next = nxt 

    return head 

if __name__ == '__main__':
    
    ll = build_list([1, 2]) 
    print_list(ll)
    l2 = removeNthFromEnd(ll, 2)
    print()
    print_list(l2)
    print('done') 
