'''
https://leetcode.com/problems/max-consecutive-ones/#/description

Problem:
Given a binary array, find the maximum number of consecutive 1s in this array.
Example 1:
    
Example:
Input: [1,1,0,1,1,1]

Output: 3

Explanation: The first two digits or the last three digits are consecutive 1s.

    The maximum number of consecutive 1s is 3.

:author: babykick
:date: 2017-04-07
'''


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_max = count = 0
        for i, x in enumerate(nums):
            if nums[i] == 1: 
                count += 1
            else:
                cur_max = max(cur_max, count)
                count = 0
        return max(cur_max, count)

if __name__ == '__main__':
    test_cases = [
        # tuple of (input, output)
        ([1,1,0,1,1,1], 3),
    ]
    
    for sample in test_cases:
        inp, outp = sample
        assert(Solution().findMaxConsecutiveOnes(inp) == outp)
    
