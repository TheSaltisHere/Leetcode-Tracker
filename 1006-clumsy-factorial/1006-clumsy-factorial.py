class Solution:
    def clumsy(self,n):
        l = []
        for i in range(1, n+1):
            l.append(i)
        t = 0
        s=""
        while len(l) > 0:
            a = l.pop()
            n = "*/+-"
            if n[t] == "*":
                s=s+str(a)+"*"
                t = t+1

            elif n[t] == "/":
                s=s+str(a)+"//"
                t = t+1
            

            elif n[t] == "+":
                s=s+str(a)+"+"
                t = t+1

            elif n[t] == "-":
                s=s+str(a)+"-"
                t = 0
        
        if s[len(s)-1]=="/":
            return eval(s[:len(s)-2])
        else:
            return eval(s[:len(s)-1])

            
