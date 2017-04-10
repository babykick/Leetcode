'''
https://leetcode.com/problems/reverse-words-in-a-string-iii

Problem:
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
Example 1:
    
Example:
Input: "Let's take LeetCode contest"

Output: "s'teL ekat edoCteeL tsetnoc"

:author: babykick
:date: 2017-04-10
'''


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(word[::-1] for word in s.split())

if __name__ == '__main__':
    test_cases = [
        # tuple of (input, output)
        ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"),
    ]
    
    for sample in test_cases:
        inp, outp = sample
        assert(Solution().reverseWords(inp) == outp)
    
