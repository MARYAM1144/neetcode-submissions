class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=0
        min_price=prices[0]
        for i in range(len(prices)):
            if min_price>prices[i]:
                min_price=prices[i]
            profit=prices[i]-min_price
            if(n<=profit):
                  n=profit
        if n>0:
            return n
        else:
            return 0
          