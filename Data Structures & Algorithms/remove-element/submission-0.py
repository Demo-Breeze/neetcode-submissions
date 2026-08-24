class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = nums.count(val)
        i=0
        while i<l:
            nums.remove(val)
            i+=1
        return len(nums)

