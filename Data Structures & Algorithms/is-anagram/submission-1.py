class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s= []        
        list_t = []
        for i in s:
            list_s.append(i)
        for i in t:
            list_t.append(i)
        if sorted(list_t) == sorted(list_s):
            return True
        else:
            return False