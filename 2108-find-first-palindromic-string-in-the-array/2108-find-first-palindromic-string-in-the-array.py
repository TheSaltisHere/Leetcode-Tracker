class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        j = 0
        for i in range(len(words)):
            if words[i] == words[i][::-1]:
                j = 1
                return words[i]
                break
            elif i == len(words)-1 and j == 0:
                return ""
            
        