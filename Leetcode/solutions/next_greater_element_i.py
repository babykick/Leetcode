'''
https://leetcode.com/problems/next-greater-element-i/#/description

Problem:
You are given two arrays (without duplicates) nums1 and nums2 where nums1��s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2. 




The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.


Example 1:

Example 2:
    
Example:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].

Output: [-1,3,-1]

Explanation:

    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.

    For number 1 in the first array, the next greater number for it in the second array is 3.

    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

:author: babykick
:date: 2017-04-07
'''


class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        results = []
        for x in findNums:
            a = -1
            if nums.index(x) < len(nums) -1:
                a = next((n for n in nums[nums.index(x)+1:] if n > x), -1)
            results.append(a)
        return results


if __name__ == '__main__':
    test_cases = [
        # tuple of (input, output)
        (([4,1,2], [1,3,4,2]), [-1,3,-1]),
    ]
    
    for sample in test_cases:
        inp, outp = sample
        assert(Solution().nextGreaterElement(*inp) == outp)
    
