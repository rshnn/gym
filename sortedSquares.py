"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

 

Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in non-decreasing order.

"""


def sortedSquares(nums): 
    
    out = [None] * len(nums) 
    left = 0 
    right = len(nums) - 1  
    idx = len(nums) - 1

    while idx >= 0: 

        if abs(nums[left]) > abs(nums[right]): 
            out[idx] = nums[left]**2
            left += 1  
            idx -= 1 
        else: 
            out[idx] = nums[right]**2 
            right -= 1 
            idx -= 1 

    return out 




if __name__ == '__main__':
    nums = [-7,-3,2,3,11]
    print(sortedSquares(nums)) 