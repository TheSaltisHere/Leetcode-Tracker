import math
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        x=math.ceil(len(b) / len(a))
        return x if b in a*(x) else x+1 if b in a*(x+1) else -1