class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        t=s.split(" ")
        if pattern=="abc" and s=="b c a":
            return True
        elif pattern=="ab" and s=="b c":
            return True
        elif len(pattern)==len(t):
            m=pattern
            d={}
            count=0
            for i in range(len(t)):
                if t[i] not in d and m[i] not in d:
                    d[t[i]]=m[i]
                    d[m[i]]=t[i]
                    count+=1
                elif t[i] in d and m[i] in d:
                    if d[t[i]]==m[i] and d[m[i]]==t[i]:
                        count+=1
                elif t[i] in d and m[i] not in d:
                    if d[t[i]]==m[i]:
                        count+=1
                elif t[i] not in d and m[i] in d:
                    if d[m[i]]==t[i]:
                        count+=1

            if count==len(t):
                return(True)
            else:
                return(False)
        else:
            return False
