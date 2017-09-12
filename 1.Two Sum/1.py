# -*- coding:utf-8 -*-

class Solution(object): # O(n^2)
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for num in nums:
        	i = nums.index(num)
        	j = [j for j,v in enumerate(nums) if v==(target-num) and j!=i]
        	if j:
        		return [i, j[0]]

s = Solution()
print(s.twoSum([0, 4, 3, 0], 0))