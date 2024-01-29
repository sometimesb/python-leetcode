from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []
        for number in nums1:
            window = nums2[nums2.index(number):]
            next_greater = -1

            for num in window:
                if num > number:
                    next_greater = num
                    break

            arr.append(next_greater)
            print(number, window, next_greater)

        print(arr)
        return(arr)
        

        