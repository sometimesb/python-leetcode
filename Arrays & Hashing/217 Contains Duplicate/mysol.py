from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for number in nums:
            if number in hash_map:
                return True
            else:
                hash_map[number] = 1
        return False

sol = Solution()
example_nums = [1, 2, 3, 4, 5, 2]
result = sol.containsDuplicate(example_nums)
print(result)
