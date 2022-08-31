class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]=d[i]+1
        print(d)
        
        if len(set(d.values()))==1:
            return True
        else:
            return False