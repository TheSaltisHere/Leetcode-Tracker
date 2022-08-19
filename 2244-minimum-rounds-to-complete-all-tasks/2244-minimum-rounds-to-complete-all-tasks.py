class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasks.sort()
        final=[]
        l=[]
        if len(tasks)==1:
            return -1
        for i in range(len(tasks)):
            if i==0:
                l=[tasks[0]]
                
            elif i==len(tasks)-1:
                if tasks[i] in l:
                    l.append(tasks[i])
                    final.append(l)
                else:
                    final.append([tasks[i]])
                    
                
            else:
                if tasks[i] in l:
                    l.append(tasks[i])
                else:
                    final.append(l)
                    l=[tasks[i]]
        
        print(final)    
        
        count=0
        for i in final:
            if len(i)==1:
                return -1
            if len(i)==2:
                count=count+1
            elif len(i)>=3:
                t=len(i)%3
                if t==0:
                    count=count+len(i)//3
                elif t==1:
                    count=count+len(i)//3 +1
                elif t==2:
                    count=count+len(i)//3 +1
        return(count)

                    
                
            
            