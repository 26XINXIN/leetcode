class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1: return 0
        diff = [prices[i + 1] - prices[i] for i in range(len(prices)-1)]
        result = 0
        max_profit = 0; min_profit = 0
        latest_max_profit = 0; latest_min_profit = 0
        for d in diff:
            latest_max_profit = max(d, latest_max_profit + d)
            latest_min_profit = min(d, latest_min_profit + d)
            max_profit = max(latest_max_profit, max_profit)
            min_profit = min(latest_min_profit, min_profit)
            if min_profit > 0:
                result = max(result, max_profit)
            else:
                reuslt = max(result, max_profit - min_profit)
        return result