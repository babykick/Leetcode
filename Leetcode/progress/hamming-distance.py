'''
https://leetcode.com/problems/hamming-distance/

Problem:
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.
Note:
0 ¡Ü x, y < 231.
    
Example:
Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ¡ü   ¡ü

The above arrows point to positions where the corresponding bits are different.

:author: babykick
:date: 2017-04-07
'''

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """


if __name__ == '__main__':
    test_cases = [
        # tuple of (input, output)
        (, ),
        (, )
    ]
    
    for sample in test_cases:
        assert(Solution().solve(sample[0]), sample[1])
    
