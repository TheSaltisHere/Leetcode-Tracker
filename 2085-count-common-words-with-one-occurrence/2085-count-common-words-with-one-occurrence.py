from collections import Counter
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        d1=Counter(words1)
        d2=Counter(words2)
        count=0
        for i in d1:
            if d1[i]==1 and i in d2 and d2[i]==1:
                count+=1
        return(count)

