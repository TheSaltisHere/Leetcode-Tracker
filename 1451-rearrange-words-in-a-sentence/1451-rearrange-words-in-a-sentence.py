class Solution:
    def arrangeWords(self, text: str) -> str:
        l=text.split(" ")
        l=sorted(l,key=len)

        
        e=""
        for i in range(len(l)-1):
            e=e+l[i]+" "
        e=e+l[len(l)-1]
        m=e[1::].lower()
        p=e[0].upper()
        
        return p+m
                    
                
        