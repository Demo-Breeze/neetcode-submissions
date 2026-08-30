class Solution:
    def minOperations(self, s: str) -> int:
        count_start_0 = 0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] != '0':
                    count_start_0 += 1
            else:
                if s[i] != '1':
                    count_start_0 += 1
        count_start_1 = len(s) - count_start_0
        
        return min(count_start_0, count_start_1)