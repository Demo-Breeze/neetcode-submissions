class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        w = s.split()
        
        if len(pattern) != len(w):
            return False
            
        p2w = {}
        w2p = {}
        
        for c, x in zip(pattern, w):
            if c in p2w and p2w[c] != x:
                return False
            if x in w2p and w2p[x] != c:
                return False
                
            p2w[c] = x
            w2p[x] = c
            
        return True
