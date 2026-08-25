class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        full_set = set(range(1, len(nums) + 1))
        

        actual_set = set(nums)
        
        return list(full_set - actual_set)