
'''
Problem:
    Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
    
Example:
    
For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]


:author :babykick
'''

class Solution(object):
    def solve(*args, **kwargs):
        return NotImplementedError


if __name__ == '__main__':
    test_cases = [
        # tuple of (input, output)
        (, ),
        (, )
    ]
    
    for sample in test_cases:
        assert(Solution().solve(sample[0]), sample[1])
    
