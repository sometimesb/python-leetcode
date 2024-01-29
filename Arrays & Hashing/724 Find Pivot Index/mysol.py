from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            left = nums[0:i]
            right = nums[i+1:]
            if(sum(left) == sum(right)):
                return i
            
            # print(left,right,sum(left),sum(right))
        return -1