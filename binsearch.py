"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

"""
import time 


def search(nums, target):

    left = 0
    right = len(nums) - 1 


    while left <= right: 

        idx = left + ((right - left) // 2) 

        if nums[idx] == target: 
            return idx 

        elif target < nums[idx]: 
            right = idx - 1   

        else: 
            left = idx + 1 


    return -1 


if __name__ == '__main__':
    nums = [2, 5] 
    target = 2

    print(search(nums, target))

    print(int( 99 // 100 ))
