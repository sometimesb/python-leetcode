from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        array = [0 for i in range(len(arr))]
        max_value = -1
        for i in range(len(arr)-1, -1,-1):
            array[i] = max_value
            max_value = max(arr[i],max_value)
            print(max_value)

        return(array)