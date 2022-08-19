class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        odd_letter=["a","c","e","g"]
        even_letter=["b","d","f","h"]
        odd_number=["1","3","5","7"]
        even_number=["2","4","6","8"]
        if coordinates[0] in odd_letter and coordinates[1] in odd_number:
            return False

        elif coordinates[0] in odd_letter and coordinates[1] in even_number:
            return True
        
        elif coordinates[0] in even_letter and coordinates[1] in even_number:
            return False
        
        elif coordinates[0] in even_letter and coordinates[1] in odd_number:
            return True

        