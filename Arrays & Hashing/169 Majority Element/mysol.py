from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}
        for item in nums:
            if(item in hashMap):
                hashMap[item] = hashMap[item] + 1
            else:
                hashMap[item] = 1
        return  max(hashMap, key=lambda k: hashMap[k])