from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      hashset = set()

      for number in nums:
        if number in hashset:
          return True
        else:
          hashset.add(number)
      return False

sol = Solution()
print(sol.containsDuplicate([1,2,3,4,5]))