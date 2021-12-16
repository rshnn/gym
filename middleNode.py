
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


def middleNode(head):
    
    idx_dict = dict() 

    tmp = head 
    cnt = 0 

    while tmp: 
        cnt += 1 
        idx_dict[cnt] = tmp 

        tmp = tmp.next 

    # middle val 
    middle = cnt // 2 + 1

    return idx_dict[middle]


if __name__ == '__main__':
    
    ll = build_list([1, 2, 3, 4, 5, 6]) 
    print(middleNode(ll))