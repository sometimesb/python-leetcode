class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        (pos1, pos2) = (0,0)
        res = []
        while pos1 < len(word1) and pos2 < len(word2):
            res.append(word1[pos1])
            res.append(word2[pos1])
            pos1+=1
            pos2+=1
        
        res.append(word1[pos1:])
        res.append(word2[pos2:])


        return "".join(res)
        
        