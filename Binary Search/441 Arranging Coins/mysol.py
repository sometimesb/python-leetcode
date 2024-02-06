class Solution:
    def arrangeCoins(self, n: int) -> int:
    #    8-1 = 7
    #    7-2 = 5
    #    5-3 = 2
    #    2-4 = -2
        i = 1
        result = n
        while result >= 0: 
            result = result - i
            if result < 0:  
                break
            i += 1

        return i-1

