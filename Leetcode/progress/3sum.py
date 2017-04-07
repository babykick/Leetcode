'''
https://leetcode.com/problems/3sum/

Problem:
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
    
Example:
For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

:author: babykick
:date: 2017-04-07
'''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        


if __name__ == '__main__':
    test_cases = [
        # tuple of (input, output)
        (, ),
        (, )
    ]
    
    for sample in test_cases:
        inp, outp = sample
        assert(Solution().hammingDistance(*inp) == outp)
    
