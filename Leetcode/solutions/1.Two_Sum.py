''''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

:author: babykick
:date: 2017.4.7

'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, e in enumerate(nums):
            d.setdefault(e, []).append(i)

        for i, a in enumerate(nums):
            b = target - a
            if b in d: # found
                for j in d[b]: # search the expand list
                   if i != j:
                       return [i, j]


"""
Solution from site: 
O(n)

class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

"""
         


if __name__ == '__main__':
    assert(Solution().twoSum([3,2,4], 6) == [1, 2])
    assert(Solution().twoSum([3,3,4], 6) == [0, 1])