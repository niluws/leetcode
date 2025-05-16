class Solution(object):
    def maxProfit(self,prices):
        j = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                j += prices[i] - prices[i - 1]
        return j


print(Solution().maxProfit([1, 2, 3, 4, 5]))
