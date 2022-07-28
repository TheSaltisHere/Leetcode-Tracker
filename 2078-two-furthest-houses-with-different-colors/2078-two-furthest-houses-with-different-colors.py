class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        l=[]
        initial=colors[0]
        
        for i in range(len(colors)-1,-1,-1):
            if colors[i]!=initial:
                final_index=i
                break
        
        l.append(i)
        
        colors=colors[::-1]
        initial=colors[0]
        
        for i in range(len(colors)-1,-1,-1):
            if colors[i]!=initial:
                final_index=i
                break
        
        l.append(i)
        
        return max(l)
                