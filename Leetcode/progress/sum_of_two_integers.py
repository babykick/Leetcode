'''
https://leetcode.com/problems/sum-of-two-integers/#/description

Problem:
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
Example:
Given a = 1 and b = 2, return 3.
    
Example:
Credits:Special thanks to @fujiaozhu for adding this problem and creating all test cases.

:author: babykick
:date: 2017-04-10
'''


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        


if __name__ == '__main__':
    test_cases = [
        # tuple of (input, output)
        (, ),
    ]
    
    for sample in test_cases:
        inp, outp = sample
        assert(Solution().getSum(inp) == outp)
    
