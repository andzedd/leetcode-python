class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arr = []
        map = {}
        x=0
        while(x < len(nums)):
            num = nums[x]
            diff = target - num
            if str(diff) in map:
                arr.append(x)
                y = map.get(str(diff), "")
                arr.append(y)
                return arr
            map[str(num)] = x
            x += 1
            
        
        
        return arr
