class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        total = []
        for i in set(s):
            d = s.find(i)
            c = s.rfind(i)
            total.append(c-d-1)
        return max(total)