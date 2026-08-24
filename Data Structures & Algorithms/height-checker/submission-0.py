class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        total = 0
        for i, (original, sorted_val) in enumerate(zip(heights, sorted(heights))):
            if original!= sorted_val:
                total+=1
        return total

