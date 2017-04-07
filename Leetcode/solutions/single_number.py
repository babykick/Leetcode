'''
https://leetcode.com/problems/single-number/#/description

Problem:
Given an array of integers, every element appears twice except for one. Find that single one.
    
Example:
Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

:author: babykick
:date: 2017-04-07
'''


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = dict()
       
        for n in nums:
            a[n] = a.setdefault(n, 0) + 1
        for k, v in a.items():
            if v == 1:
                return k

if __name__ == '__main__':
    test_cases = [
        # tuple of (input, output)
        ([1,4,1,3,4], 3),
    ]
    
    for sample in test_cases:
        inp, outp = sample
        assert(Solution().singleNumber(inp) == outp)
    
