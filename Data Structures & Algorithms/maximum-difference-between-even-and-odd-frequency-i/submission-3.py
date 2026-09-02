class Solution:
    def maxDifference(self, s: str) -> int:
        d= list(sorted(set(s)))
        odd = []
        even = []
        for i in d:
            if s.count(i)%2 ==1:
                odd.append(s.count(i))
            elif s.count(i)%2 ==0:
                even.append(s.count(i))
        return max(odd)-min(even)
        