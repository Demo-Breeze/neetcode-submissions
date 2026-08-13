class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s=len(prices)
        i=[]
        for char in range(s-1,-1,-1):
            d = prices.pop(char)
            l=min(prices,default=0)
            x= d-l
            i.append(x)     
        i.pop(-1)
        if all(b < 0 for b in i) ==True:
            return 0
        else:
            return(max(i))