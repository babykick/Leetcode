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
import bisect

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3: 
            return []

        rv = []
        nums.sort()
    
        for i, a in enumerate(nums):
            for result in self.twoSum(nums[i+1:], -a):
                b, c = result
                if sorted([a, b, c]) not in rv:
                    rv.append(sorted([a, b, c]))
       
        return rv


    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        rv = []
        for i, a in enumerate(numbers):
            b = target - a
            j = bisect.bisect_left(numbers, b, lo=i+1)
            if j != len(numbers) and j != i and numbers[j] == b:
                rv.append([a, b])
        return rv


if __name__ == '__main__':
    test_cases = [
        # tuple of (input, output)
        ([-1, 0, 1, 2, -1, -4], [ [-1, 0, 1], [-1, -1, 2]]),
        ([-2,0,1,1,2], [[-2,0,2],[-2,1,1]])
    ]
    
    for sample in test_cases:
        inp, outp = sample
        rs = sorted(Solution().threeSum(inp)) == sorted(outp)
        print('test', inp, outp, rs)
         
