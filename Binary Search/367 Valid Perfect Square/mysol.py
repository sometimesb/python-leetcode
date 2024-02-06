class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        left = 0
        right = num
        while left <= right:
            mid = (left+right) // 2
            guess = mid**2
            if guess > num:
                right = mid -1
            elif guess < num:
                left = mid+1
            else:
                return True
        return False