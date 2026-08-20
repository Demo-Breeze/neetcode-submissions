class Solution:
    def scoreOfString(self, s: str) -> int:
        d= 0 
        c =1
        answer = []
        while d < len(s)-1:
            answer.append(abs(ord(s[c]) - ord(s[d])))
            c+=1
            d+=1
        final_answer = sum(answer)
        print(answer)
        return final_answer