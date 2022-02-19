class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        l=[]
        l1=[]
        d={}
        for i in range(len(mat)):
            ind=[i]
            t=max(mat[i])
            ind.append(mat[i].index(t))
            if t in d:
                d[t].append((ind))
            else:
                d[t]=[ind]
                
        print(ind)
        y=list(d)
        maximum=max(y)
        
        return d[maximum][0]