class Solution:
    def sortSentence(self, s: str) -> str:
        t=s.split(" ")
        d={}
        for i in t:
            q=int(i[len(i)-1])
            i=i.replace(i[len(i)-1],"")
            d[q]=i
            r=sorted(d.keys())
            sorted_dict = {key:d[key] for key in r}
            
        l=""
        for i in sorted_dict:
            l=l+sorted_dict[i]+" "
        return l[:len(l)-1:]
            