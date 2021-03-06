'''
https://leetcode.com/problems/find-the-difference/#/description

Problem:
Given two strings s and t which consist of only lowercase letters.
String t is generated by random shuffling string s and then add one more letter at a random position.
Find the letter that was added in t.
    
Example:
Input:

s = "abcd"

t = "abcde"



Output:

e



Explanation:

'e' is the letter that was added.

:author: babykick
:date: 2017-04-10
'''


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_, t_ = sorted(s), sorted(t)
        i = 0
        while i < len(s) and s_[i] == t_[i]: 
            i += 1
        return t_[i]
        


if __name__ == '__main__':
    test_cases = [
        # tuple of (input, output)
        (('abcd', 'abcde'), 'e'),
        (('ab', 'aab'), 'a')
    ]
    
    for sample in test_cases:
        inp, outp = sample
        assert(Solution().findTheDifference(*inp) == outp)
    
