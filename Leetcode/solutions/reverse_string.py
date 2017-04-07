'''
https://leetcode.com/problems/reverse-string/#/description

Problem:
Write a function that takes a string as input and returns the string reversed.
    
Example:
Example:

Given s = "hello", return "olleh".

:author: babykick
:date: 2017-04-07
'''


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
        


if __name__ == '__main__':
    test_cases = [
        # tuple of (input, output)
        ('hello', 'olleh'),
    ]
    
    for sample in test_cases:
        inp, outp = sample
        assert(Solution().reverseString(inp) == outp)
    
