class Solution:
    # Function to calculate max profit using brute force
    def stockbuySell(self, prices):
        # Initialize max profit to 0
        maxProfit = 0

        # Loop through each day as potential buy day
        for i in range(len(prices)):
            
            for j in range(i + 1, len(prices)):
                # Calculate profit
                profit = prices[j] - prices[i]

                # Update max profit if higher
                maxProfit = max(maxProfit, profit)

        return maxProfit

# Driver code
sol = Solution()
A = [7, 1, 5, 3, 6, 4]
print("Max Profit:", sol.stockbuySell(A))