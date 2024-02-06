class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2 
            gauss_mid = self.gaussian(mid)
            if gauss_mid == n:
                return mid
            elif gauss_mid > n:
                right = mid - 1
            else:
                left = mid + 1
        return right
    
    def gaussian(self, n: int) -> int:
        return (n * (n + 1)) // 2