import math
class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        num1=num+1
        num2=num+2
        
        sol_1=[]
        sol_2=[]
        sol_3=[]

        for i in range(1,int(math.sqrt(num1))+1):
            if num1%i==0:
                sol_1.append([abs(i-num1/i),i,num1/i])

        #sort the list by the first element
        sol_1.sort(key=lambda x:x[0])

        for i in range(1,int(math.sqrt(num2))+1):
            if num2%i==0:
                sol_2.append([abs(i-num2/i),i,num2/i])

        sol_2.sort(key=lambda x:x[0])

        sol_3.append(sol_1[0])
        sol_3.append(sol_2[0])

        #take minimum of the two
        sol_3.sort(key=lambda x:x[0])
        return([int(sol_3[0][1]),int(sol_3[0][2])])



                
                
                
            
        
        
        