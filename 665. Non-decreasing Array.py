"""
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

 

Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.
 

Constraints:

1 <= n <= 10 ^ 4
- 10 ^ 5 <= nums[i] <= 10 ^ 5
"""


class Solution(object):

    """
    This solution makes use of the idea that we do not change anything until the two numbers are ascending,
    once a number is > than the next number then both copies of the original arrays are changes.
    one copy changes the current index value to the next value while the second copy changes its next value to this current value.
    If the happens then the loop is broken and each copy is compared with its sorted array.
    If either of the two copies mathc there sorted(ascending) then True is returned else False.

    Runtime - 328 ms
    Memory  - 15.3 MB

    """

    def checkPossibility(self, nums):

        tmp1 = nums[:]
        tmp2 = nums[:]
        for i in range(len(nums)-1):
            if(nums[i] > nums[i+1]):
                tmp1[i] = nums[i+1]
                tmp2[i+1] = nums[i]
                break
        return tmp1 == sorted(tmp1) or tmp2 == sorted(tmp2)
