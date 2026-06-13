class BestTimeToBuyAndSellStock2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        else:
            profit = 0
            for i in range(1, len(prices)):
                curr_profit = prices[i] - prices[i-1]
                if curr_profit > 0:
                    profit += curr_profit
            return profit