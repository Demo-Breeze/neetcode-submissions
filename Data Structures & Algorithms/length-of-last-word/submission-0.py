class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s =s.strip()
        i = s.split(" ")
        return(len(i[-1]))
