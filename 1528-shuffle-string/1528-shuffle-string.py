class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        t=[0]*len(indices)
        for i in range(len(indices)):
            t[indices[i]]=s[i]
        g=""
        for i in t:
            g=g+i
        return g
        
        