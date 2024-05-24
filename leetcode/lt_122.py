class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 0 or len(prices) == 1:
            return 0
        max_profit = 0
        
        for index,value in enumerate(prices):
            if index == 0:
                continue
            current_value = value
            previous_value = prices[index-1]
            if current_value - previous_value > 0:
                max_profit += current_value - previous_value
        return max_profit
            
                
        

if __name__ == "__main__":
    sol = Solution()
    prices = [1,2,3,4,5]
    answer = sol.maxProfit(prices)
    print(answer)