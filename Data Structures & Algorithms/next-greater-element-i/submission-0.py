class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        final_answer = []
        c=len(nums1)
        for i in nums1:
            answer = []
            s= nums2.index(i)# Get the position so that i can find the rest
            b = s+1
            while b<len(nums2):
                
                if nums2[s]<nums2[b]:
                    answer.append(nums2[b])
                    break
                b+=1
                    
            if answer == []:
                answer.append(-1)
            final_answer.extend(answer)
        return final_answer


