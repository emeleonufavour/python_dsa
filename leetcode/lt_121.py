class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest_price = 10000
        length = len(prices)
        pointer_b = 0
        max_profit = 0
        
        
        while pointer_b < length:
            if prices[pointer_b] < lowest_price:
                lowest_price = prices[pointer_b]
            if prices[pointer_b] - lowest_price > max_profit:
                max_profit = prices[pointer_b] - lowest_price
            pointer_b = pointer_b + 1
        return max_profit
            
        
            
            
        
        
if __name__ == "__main__":
    sol = Solution()
    prices = [7,1,5,3,6,4]
    answer = sol.maxProfit(prices)
    print(answer)