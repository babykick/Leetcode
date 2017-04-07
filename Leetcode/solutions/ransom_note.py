'''
https://leetcode.com/problems/ransom-note/#/description

Problem:
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom 

note can be constructed from the magazines ; otherwise, it will return false. 




Each letter in the magazine string can only be used once in your ransom note.
    
Example:
canConstruct("a", "b") -> false

canConstruct("aa", "ab") -> false

canConstruct("aa", "aab") -> true

:author: babykick
:date: 2017-04-07
'''


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = {}
        for x in magazine:
            d[x] = d.setdefault(x, 0) + 1
        for y in ransomNote:
            if y not in d:
                return False
            d[y] -= 1
            if d[y] < 0:
                return False        
        return True

if __name__ == '__main__':
    test_cases = [
        # tuple of (input, output)
        (('a', 'b'), False),
        (("aa", "ab"), False),
        (("aa", "aab"), True)
    ]
    
    for sample in test_cases:
        inp, outp = sample
        assert(Solution().canConstruct(*inp) == outp)
    
