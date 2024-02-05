from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       buy = 0
       sell = 0
       maxProfit = 0
       while sell < len(prices):
            if(prices[sell]-prices[buy] > maxProfit):
                maxProfit = prices[sell] - prices[buy]
            elif(prices[sell] < prices[buy]):
                buy=sell
            sell+=1

       print(maxProfit) 
       return maxProfit