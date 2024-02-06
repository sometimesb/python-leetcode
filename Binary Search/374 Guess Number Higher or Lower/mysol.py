# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

def guess(num: int) -> int:
  #some implementation 
  pass

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n 

        while left <= right:
            mid = (left + right) // 2
            result = guess(mid)
            #higher
            if result == -1:
                right = mid - 1
            #lower
            elif result == 1:
                left = mid + 1
            else:
                return mid
        

        # actual = 6

        # left = 1
        # right = 10
        # mid = 5
        # guess with 5 -> 1 (lower)

        # left = mid + 1 = 6
        # right = 10
        # mid = 8
        # guess with 8 -> -1 (higher)
        # right = mid - 1 = 7

        # left = 6
        # right = 7
        # mid = 6
        # guess with 6 -> 0 return 6
