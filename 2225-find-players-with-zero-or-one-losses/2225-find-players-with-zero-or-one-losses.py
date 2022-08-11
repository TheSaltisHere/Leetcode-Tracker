class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answer=[[],[]]
        d_lost={}
        d_win={}
        for i in matches:
            if i[0] in d_win:
                d_win[i[0]]=d_win[i[0]]+1
            else:
                d_win[i[0]]=1
            
            if i[1] in d_lost:
                d_lost[i[1]]=d_lost[i[1]]+1
            else:
                d_lost[i[1]]=1
        
        maximum_number=max(max(d_lost.keys()),max(d_win.keys()))
        
        for i in range(1,maximum_number+1):
            if i not in d_lost and i in d_win:
                d_lost[i]=0
        
        for i in d_lost:
            if d_lost[i]==0:
                answer[0].append(i)
            elif d_lost[i]==1:
                answer[1].append(i)
        answer[0].sort()
        answer[1].sort()
        return(answer)
        
                
        
        