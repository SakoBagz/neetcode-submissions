class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        bp = 0
        sp = bp + 1
        while sp < len(prices): 
            if prices[sp] < prices[bp]:
                bp = sp
            else:
                current_profit = prices[sp] - prices[bp]
                max_profit = max(max_profit, current_profit)
                sp += 1
        return max_profit