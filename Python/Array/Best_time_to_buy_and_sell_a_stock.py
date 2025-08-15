class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest_stock = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - cheapest_stock)
            cheapest_stock = min(cheapest_stock, prices[i])

        return max_profit
