class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= s.replace(" ","")
        s= s.replace(",","")
        s= s.replace(".","")
        s= s.replace(":","")
        s= s.replace(";","")
        s= s.replace("'","")
        s = s.replace("?","")
        s= s.replace("!","")
        s = s.lower()
        postive_index = 0
        negative_index = -1
        total_amount = 0
        print(s)
        while total_amount -1 <len(s):
            if total_amount == len(s):
                return True
            if s[postive_index] == s[negative_index]:
                postive_index += 1
                negative_index -= 1
                pass
                total_amount+=1

            
            else:
                print(s[postive_index]) 
                print(s[negative_index])
                return False