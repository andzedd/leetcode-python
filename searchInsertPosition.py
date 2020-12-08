class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        x = 0
        while (x < len(nums)):
            if(nums[x] == target):
                return x
            if(target > nums[x] and x + 1 >= len(nums)):
                return x + 1
            if(target > nums[x]):
                x += 1
                continue
            return x