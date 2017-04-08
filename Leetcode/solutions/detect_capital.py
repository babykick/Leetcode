'''
https://leetcode.com/problems/detect-capital/#/description

Problem:
Given a word, you need to judge whether the usage of capitals in it is right or not.




We define the usage of capitals in a word to be right when one of the following cases holds:


Example 1:

Example 2:
    
Example:
Input: "USA"

Output: True

:author: babykick
:date: 2017-04-08
'''


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.isupper() or word.islower() or word.istitle()


if __name__ == '__main__':
    test_cases = [
        # tuple of (input, output)
        ('USA', True),
        ('FlaG', False)
    ]
    
    for sample in test_cases:
        inp, outp = sample
        assert(Solution().detectCapitalUse(inp) == outp)
    
