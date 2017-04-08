'''
https://leetcode.com/problems/add-digits/#/description

Problem:
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit. 




For example:




Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.


Follow up:

Could you do it without any loop/recursion in O(1) runtime?
    
Example:
Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

:author: babykick
:date: 2017-04-08
'''


class Solution(object):
    '''
    Math problem, refer to https://en.wikipedia.org/wiki/Digital_root
    '''
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0: 
            return 0
        return 1 + (num-1) % 9
        


if __name__ == '__main__':
    test_cases = [
        # tuple of (input, output)
        (1853, 8),
    ]
    
    for sample in test_cases:
        inp, outp = sample
        assert(Solution().addDigits(inp) == outp)
    
