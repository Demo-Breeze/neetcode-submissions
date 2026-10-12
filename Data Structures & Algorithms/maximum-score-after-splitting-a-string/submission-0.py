class Solution:
    def maxScore(self, s: str) -> int:
        counter = 1
        total =[]
        while counter < len(s):
            c,d =(s[:counter],s[counter:])
            c,d = str(c),str(d)
            k,l  = c.count("0"),d.count("1")
            total.append(k+l)
            counter+=1
        return max(total)