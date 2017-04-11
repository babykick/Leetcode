'''
https://leetcode.com/problems/move-zeroes/#/description

Problem:
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.




For example, given nums  = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].



Note:
    
Example:
Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

:author: babykick
:date: 2017-04-11
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Take non-zero element as the same value and sort
        nums.sort(key=lambda x: x if x == 0 else -1)
    

if __name__ == '__main__':
     
    test_cases = [
        # tuple of (input, output)
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
    ]
    
    for sample in test_cases:
        inp, outp = sample
        Solution().moveZeroes(inp)
        assert(inp == outp)
    
