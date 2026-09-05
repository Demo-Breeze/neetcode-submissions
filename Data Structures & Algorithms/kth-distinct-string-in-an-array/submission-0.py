class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        b = []
        for i in list(dict.fromkeys(arr)):
            if arr.count(i)==1:
                b.append(i)
        print(b)
        if len(b)<k:
            return ""
        return b[k-1]