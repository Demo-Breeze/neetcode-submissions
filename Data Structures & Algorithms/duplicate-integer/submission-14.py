class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list_set = set(nums)
        if len(list_set) == len(nums):
            return False
        elif len(list_set)<= len(nums):
            return True







"""        true_nums = []
        length = len(nums)
        if length == 0:
            return False
        while length > 0 :
            i = nums[0]
            true_nums.append(i)
            nums.remove(i)
            length -=1

            if i in true_nums and i in nums:
                return True
 elif length >= 0:

                if length <= 0:
                    return False
            """





            