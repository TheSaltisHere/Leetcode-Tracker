class Solution:
    def sumBase(self, n: int, k: int) -> int:
        quotient=n//k
        remainder=n%k
        l=[]
        l.append(remainder)
        while quotient!=0:
            remainder=quotient%k
            quotient=quotient//k
            l.append(remainder)
            
        return(sum(l))
            