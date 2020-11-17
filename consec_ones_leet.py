"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000

"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_c = 0 
        c = 0 
        in_sequence = False 

        for item in nums: 

            if item == 1:
                in_sequence = True 
                c+=1 

            else: 

                # broke a sequence 
                if in_sequence: 
                    if c > max_c: 
                        max_c = c 

                # not in sequence 
                c = 0 
                in_sequence = False 

        if c > max_c: 
            max_c = c 

        return max_c 


        


if __name__ == "__main__": 

    nums = [1,1,0,1,1,1]
    soln = Solution()

    a = soln.findMaxConsecutiveOnes(nums)
    print(a)
