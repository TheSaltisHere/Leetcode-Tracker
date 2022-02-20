class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l=[]
        for i in range(len(tokens)):
            if tokens[i] not in "+-/*":
                l.append(tokens[i])
            else:
                if len(l)!=0:
                    a=int(l.pop())
                    b=int(l.pop())
                    
                    if tokens[i]=="+":
                        l.append(b+a)
                        
                    if tokens[i]=="-":
                        l.append(b-a)
                
                    if tokens[i]=="*":
                        l.append(b*a)
                    
                    if tokens[i]=="/":
                        l.append(int(b/a))
        return l[0]
                    
                    

                
        
        