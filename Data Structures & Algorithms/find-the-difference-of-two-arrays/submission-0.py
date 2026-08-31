class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums3 = list(set(nums1)-set(nums2))
        nums4 = list(set(nums2)-set(nums1))
        return [nums3,nums4]