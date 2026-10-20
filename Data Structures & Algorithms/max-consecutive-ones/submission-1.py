class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        total = []
        score = 0
        for i in nums:
            if i== 1:
                score+=1
                print(score)
            else:
                total.append(score)
                score = 0
            total.append(score)
        return max(total)