class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = "".join([str(item) for item in digits])
        answer = int(result)
        digits.clear()
        answer+=1
        s= str(answer)
        for i in s:
            digits.append(i)
        return digits