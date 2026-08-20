class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        i=0
        final_answer = []
        while i<2:
            final_answer.extend(nums)
            i+=1
        return final_answer