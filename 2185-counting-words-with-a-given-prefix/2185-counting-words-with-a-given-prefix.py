class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count=0
        t=len(pref)
        for i in words:
            if i[0:t]==pref:
                count=count+1
        return count
                
        