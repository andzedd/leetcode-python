class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        x = 0
        y = 1
        while (y < len(nums)):
            if nums[x] != nums[y]:
                x += 1
                nums[x] = nums[y]
            y += 1
        return x + 1