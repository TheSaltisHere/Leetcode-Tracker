class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        i=0
        l=[]
        for i in range(len(prices)-1):
            flag=0
            for j in range(i+1,len(prices)):
                if prices[j]<=prices[i]:
                    flag=1
                    l.append(prices[i]-prices[j])
                    break
            if flag==0:
                l.append(prices[i])
        l.append(prices[len(prices)-1])
        return l
            
        