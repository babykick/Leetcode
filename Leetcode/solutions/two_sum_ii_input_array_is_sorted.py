
'''
Problem:
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
    
Example:
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

:author: babykick
:date: 2017-04-07
'''
import bisect

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, a in enumerate(numbers):
            b = target - a
            j = bisect.bisect_left(numbers, b)
            if j != len(numbers) and j != i and numbers[j] == b:
                return sorted([i+1, j+1])


if __name__ == '__main__':
    test_cases = [
        # tuple of (input, output)
        ([2, 7, 11, 15], 9),
    ]
    
    for sample in test_cases:
        assert(Solution().twoSum(sample[0], sample[1]))
    
