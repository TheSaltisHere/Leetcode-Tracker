class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        start=s[1]
        end=s[4]
        letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        start_letter_index=letters.index(s[0])
        end_letter_index=letters.index(s[3])
        
        required_array=letters[start_letter_index:end_letter_index+1]
        l=[]
        for i in required_array:
            for j in range(int(start),int(end)+1):
                s=i+str(j)
                l.append(s)
                
        return l
                
        
        
        