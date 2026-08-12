class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i=0
        b=len(arr)
        final_list = []
        while i<b:
            arr.pop(0)
            s=max(arr, default=-1)
            final_list.append(s)
            i+=1
        return final_list