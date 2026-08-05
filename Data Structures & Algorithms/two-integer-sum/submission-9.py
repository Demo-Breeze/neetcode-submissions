class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        run= True
        Primary_Index=0
        Secondary_Index=1
        Sum = []
 
        while run == True:
            if Secondary_Index == len(nums):
                Primary_Index += 1
                Secondary_Index = Primary_Index + 1
                continue
            Sum_1 = int(nums[Primary_Index])
            Sum_2 = int(nums[Secondary_Index])
            #print(Sum_2)
            if Sum_1 + Sum_2 == target and Primary_Index != Secondary_Index:#Check if it is equal to target
                Sum.append(Primary_Index)
                Sum.append (Secondary_Index)
                run = False
                return Sum
            elif Secondary_Index < len(nums):
                Secondary_Index+=1
            else:
                pass