class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        t=str(n)
        a=1
        b=0
        for i in t:
            a=a*int(i)
            b=b+int(i)
            
        return (a-b)
            
        