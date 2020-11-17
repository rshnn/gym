# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        decimal_value = 0 
        level = 0        
        tmp = head

        while tmp.next is not None: 

            decimal_value += 2**level * tmp.val 
            level += 1 
            
            tmp = tmp.next 
        return decimal_value  






if __name__ == '__main__':
    
    sol = Solution()
    sol.getDecimalValue()