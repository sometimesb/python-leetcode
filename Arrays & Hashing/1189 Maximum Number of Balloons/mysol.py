from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text) #hashMap to count each character
        balloon = Counter("balloon")

        res = len(text)
        for c in balloon:
            print(res)
            res = min(res,countText[c] // balloon[c])
        return res