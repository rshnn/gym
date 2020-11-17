"""
Add Two Numbers II

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        l1_int = numeric_rep_from_ll(l1)
        l2_int = numeric_rep_from_ll(l2)

        val = l1_int + l2_int

        return int_to_ll(val)
        



def int_to_ll(val): 

    # itemized_by_digit = [int(c) for c in str(val)]
    # return create_ll_from_list(itemized_by_digit)

    s = str(val)
    head = ListNode(s[0], None) 
    curr = head 

    for char in s[1:]: 

        tmp = ListNode(char, None)
        curr.next = tmp 
        curr = tmp 

    return head 





def numeric_rep_from_ll(ll):

    # curr = ll
    # numeric_str = "" 
    # while curr is not None:  
    #     numeric_str = numeric_str + str(curr.val)
    #     curr = curr.next 

    # return int(numeric_str)


    # Implementation with recursion 
    curr = ll 
    ans = 0
    while curr is not None: 

        val, d = return_val_d(curr)
        ans += val * 10**d 
        curr = curr.next 
    return ans 


def return_val_d(node):
    if node.next == None: 
        return node.val, 0 
    
    return node.val, return_val_d(node.next)[1] + 1




### Helper functions below 


def create_ll_from_list(lst):
    head = ListNode(lst[0], next=None)
    curr = head 

    for item in lst[1:]: 
        tmp = ListNode(item, next=None)
        curr.next = tmp 
        curr = tmp 
    return head 


def print_ll(ll): 

    curr = ll 
    while curr is not None:   
        print(curr.val, end='->')
        curr = curr.next 

    print("end")
    return 



if __name__ == "__main__": 

    soln = Solution()

    l1 = create_ll_from_list([7, 2, 4, 3])
    l2 = create_ll_from_list([5, 6, 4])

    ans = soln.addTwoNumbers(l1, l2)
    print_ll(ans)

