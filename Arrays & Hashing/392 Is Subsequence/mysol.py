class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        j = 0

        for i, letter in enumerate(s):
            try:
                print(letter, t.index(letter, j))
                j = t.index(letter, j) + 1
            except ValueError:  
                return False
        return True