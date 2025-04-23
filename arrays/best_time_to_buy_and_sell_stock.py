class Solution:
    def maxProfit(self, prices):
        # solution from solution box....was bit complex for me, now it's simple thanks.
        left = 0  #left pointer
        right = 1 #right pointer at index[1]
        max_profit = 0 #starting max profit at 0 
        while right < len(prices): #starting loop from index 1
            current_profit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                max_profit = max(current_profit, max_profit)
            else:
                left = right
            right += 1
            
        return max_profit
obj = Solution()
result = obj.maxProfit([7,1,5,2,3,6,4])
print(result)
