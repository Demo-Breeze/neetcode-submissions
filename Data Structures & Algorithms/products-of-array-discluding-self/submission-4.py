import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        answer = [1]*n
        preceding = 1
        succeeding = 1
        for i in range(n):
            answer[i] = preceding
            preceding *= nums[i]
        for i in range(n-1,-1,-1):
            answer[i] *= succeeding 
            succeeding *= nums[i]



        return answer
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """i = 0
        answer = []

        while i < len(nums):
            s = nums[i]
            nums.pop(i)
            b = math.prod(nums)
            answer.append(b)
            nums.insert(i,s)
            i += 1
        return answer
        while i <len(nums):
            s= nums[i]
            
            if s == 0:
                nums.pop(i)
                b=math.prod(nums)
                l=b
                nums.insert(i,0)
            else:
                b=math.prod(nums)
                l=b/s
            answer.append(int(l))
            i+=1
        return answer"""
        