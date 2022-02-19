class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        p=""
        for i in b:
            p=p+str(i)
        return pow(a,int(p),1337)
            