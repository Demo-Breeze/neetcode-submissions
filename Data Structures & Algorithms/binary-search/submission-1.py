class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            s = nums.index(target)
        except:
            return -1
        if s != None:
            return s
        