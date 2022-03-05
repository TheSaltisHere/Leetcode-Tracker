class Solution:
    def calPoints(self, ops: List[str]) -> int:
        l=[]
        for i in ops:
            
            if i=="+":
                a=l[-1]
                b=l[-2]
                l.append(a+b)
            
            elif i=="C":
                l.pop()
                
            elif i=="D":
                l.append(2*l[-1])
             
            elif i=="*":
                a=l[-1]
                b=l[-2]
                l.append(a*b)
                
            else:
                l.append(int(i))
        return sum(l)
            
            
                
                
        