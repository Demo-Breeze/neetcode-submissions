class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        c = True
        d = True
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                c = False 
            if nums[i] < nums[i + 1]:
                d = False
        return c or d