# -*- coding:utf-8 -*-

class Solution(object): # O(n)
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for index, num in  enumerate(nums):
            if num in map:
                return [map[num], index]
            else:
                map[target-num] = index

                
s = Solution()
print(s.twoSum([0, 4, 3, 0], 0))