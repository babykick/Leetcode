'''
https://leetcode.com/problems/number-complement

Problem:
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.
Note:

Example 1:
    
Example:
Input: 5

Output: 2

Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

:author: babykick
:date: 2017-04-07
'''


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num ^ int('1' * (len(bin(num))-2), 2)


if __name__ == '__main__':
    test_cases = [
        # tuple of (input, output)
        (5, 2),
        (1, 0)
    ]
    
    for sample in test_cases:
        inp, outp = sample
        assert(Solution().findComplement(inp) == outp)
    
