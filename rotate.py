"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

 

Constraints:

    1 <= nums.length <= 105
    -231 <= nums[i] <= 231 - 1
    0 <= k <= 105

 

Follow up:

    Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
    Could you do it in-place with O(1) extra space?

"""


def rotate(nums, k):

    edge_case = False 
    movements = k % len(nums)

    left = 0 
    right = len(nums) - movements   
    middle = left + movements 

    print(left, right, middle) 

    if middle >= right or movements == 1: 
        edge_case = True  

    while right < len(nums):

        if edge_case: 
            tmp1 = nums[left] 
            nums[left] = nums[right] 
            nums[right] = tmp1

        else: 

            tmp1 = nums[left] 
            tmp2 = nums[middle] 

            nums[left] = nums[right] 
            nums[middle] = tmp1 
            nums[right] = tmp2 

        left += 1 
        right += 1 
        middle += 1 

    return 


if __name__ == '__main__':
    nums = [0, 1, 2, 3]
    k = 1 

    print(nums)
    rotate(nums, k)
    print(nums) 