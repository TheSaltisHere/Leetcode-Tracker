class Solution:
    def findRepeatedDnaSequences(self, n: str) -> List[str]:
        d={}
        l=[]
        for i in range(len(n)-9):
            s=n[i:i+10]
            if s in d:
                d[s]=d[s]+1
            else:
                d[s]=1
                
        for i in d:
            if d[i]>1:
                l.append(i)
        
        return l
                
                
                            
            
                
                