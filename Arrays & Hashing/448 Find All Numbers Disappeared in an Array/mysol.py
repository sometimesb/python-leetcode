from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #  [4,3,2,7,8,2,3,1]
        #  n= 8, so all numbers from 1-8
        #  1 2 3 4 5 6 7 8
        numSet = set(nums)
        allNumbers = set(range(1,len(nums)+1))
        return(list(allNumbers - numSet))

