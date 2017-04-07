'''
https://leetcode.com/problems/keyboard-row/#/description

Problem:
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below. 



Example 1:
    
Example:
Input: ["Hello", "Alaska", "Dad", "Peace"]

Output: ["Alaska", "Dad"]

:author: babykick
:date: 2017-04-07
'''


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        results = []
        keys = ('qwertyuiop', 'asdfghjkl', 'zxcvbnm')
        for word in words:
            for k in keys:
                if word.lower().strip(k) == '':
                    results.append(word)
                    break
        return results


if __name__ == '__main__':
    test_cases = [
        # tuple of (input, output)
        (["Hello", "Alaska", "Dad", "Peace"], ["Alaska", "Dad"]),
    ]
    
    for sample in test_cases:
        inp, outp = sample
        assert(Solution().findWords(inp) == outp)
    
