from math import comb
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        for i in range(numRows):
            row = []
            for j in range(numRows):
                row.append(comb(j,i))
                print(comb(j,i))
        print(row)