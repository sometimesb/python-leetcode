from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashSet = {}
        for i, num in enumerate(nums):
            if num in hashSet and abs(i-hashSet[num]) <= k:
                return True
            hashSet[num] = i

        
        print(hashSet)
        return False