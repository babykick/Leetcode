'''
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/#/description

Problem:
Given an array of integers where 1 �� a[i] �� n (n = size of array), some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.
Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
    
Example:
Input:

[4,3,2,7,8,2,3,1]



Output:

[5,6]

:author: babykick
:date: 2017-04-08
'''


class Solution(object):
    '''
       Fit each element to position according to element value, like hash
       inplace swap to avoid extra memory 
    '''
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cursor = 0
        while 1:
            if cursor == len(nums):
                break
            if nums[cursor] - 1 != cursor: # current element not inplace
                if nums[nums[cursor] - 1] == nums[cursor]: # target equals source
                    cursor += 1 # target is same as current, no swap, move to next
                else:
                    nums[nums[cursor] - 1], nums[cursor] = nums[cursor], nums[nums[cursor] - 1] # different, swap
            else: # already in place
                cursor += 1 # move to next
        
        return [i + 1 for i, x in enumerate(nums) if x != i + 1]


    
    def findDisappearedNumbers2(self, nums):
        """
        Recursive version
        :type nums: List[int]
        :rtype: List[int]
        """
        import sys
        sys.setrecursionlimit(100000)

        def move(nums, cursor):
            '''
            Use nums[cursor] as intermediate swap space
            :param cursor: point to the current element
            :param count:  in-position count 
                    add 1 when swapping, means one more in-position elements 
                    add 1 when target element is in position and equals source as the source element replaces the missed element
            '''
            if cursor == len(nums):
                return
            if nums[cursor] - 1 != cursor: # current element not inplace
                if nums[nums[cursor] - 1] == nums[cursor]: # target equals source
                    cursor += 1 # target same as current, no swap, move to next
                else:
                    nums[nums[cursor] - 1], nums[cursor] = nums[cursor], nums[nums[cursor] - 1] # swap
            else: # already in place
                cursor += 1 # move to next
            move(nums, cursor) 

        
        move(nums, 0)
        return [i + 1 for i, x in enumerate(nums) if x != i + 1]
 

if __name__ == '__main__':
    test_cases = [
        # tuple of (input, output)
        ([4,3,2,7,8,2,3,1], [5,6]),
    ]
    
    for sample in test_cases:
        inp, outp = sample
        assert(Solution().findDisappearedNumbers(inp) == outp)
    
