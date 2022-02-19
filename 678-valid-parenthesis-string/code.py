class Solution:
    def checkValidString(self, s: str) -> bool:
        count_all=0
        count=0
        for i in s:
            if i=="(":
                count=count+1
                count_all=count_all+1
            elif i==")":
                count=count-1
                count_all=count_all-1
            else:
                count=count-1
                count_all=count_all+1
                
            if count_all<0:
                return False
            
            if count<=0:
                count=0
        return count==0
                
            

                    
        
