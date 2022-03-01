from itertools import permutations
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        t = []
        perm = permutations(arr, 4)
        for i in perm:
            if 0 <= int(str(str(list(i)[0])+str(list(i)[1]))) <= 23 and 0 <= int(str(str(list(i)[2])+str(list(i)[3]))) <= 59:
                t.append(i)
        if len(t)==0:
            return ""
        else:
            a = max(t)
            s = str(a[0])+str(a[1])+":"+str(a[2])+str(a[3])
            return s
            
        