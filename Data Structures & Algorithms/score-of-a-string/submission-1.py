class Solution:
    def scoreOfString(self, s: str) -> int:
        i = 0
        d= 0 
        c =1
        answer = []

        while i < len(s)-1:
            answer.append(abs(ord(s[c]) - ord(s[d])))
            c+=1
            d+=1
            i+=1
        final_answer = sum(answer)
        return final_answer