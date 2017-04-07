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
        found = []
        for a in nums:
            res = self.twoSum(nums, -a)
            if res:
                found.append([a, nums[res[0]], nums[res[1]]])
        return found

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, e in enumerate(nums):
            d.setdefault(e, []).append(i)

        for i, a in enumerate(nums):
            b = target - a
            if b in d: # found
                for j in d[b]: # search the expand list
                   if i != j:
                       return [i, j]


if __name__ == '__main__':
    test_cases = [
        # tuple of (input, output)
        ([-1, 0, 1, 2, -1, -4], [ [-1, 0, 1], [-1, -1, 2]]),
    ]
    
    for sample in test_cases:
        inp, outp = sample
        assert(Solution().threeSum(inp) == outp)
    
