class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        length = min(len(word1),len(word2))

        for i in range(length):
            merged+=word1[i]
            merged+=word2[i]
        
        if(len(word1) > len(word2)):
            merged+=word1[length:]
        elif len(word2) > len(word1):
            merged += word2[length:]

        return(merged)