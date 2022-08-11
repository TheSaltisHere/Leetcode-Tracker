class Solution:
    def secondHighest(self, s: str) -> int:
        l=[]
        for i in s:
            if i.isdigit() and int(i) not in l:
                l.append(int(i))
        l.sort(reverse=True)
        if len(l)<=1:
            return -1
        else:
            return(l[1])