class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=1
        highest=0

        while right<len(prices):
            if prices[left] < prices[right]:
                profit=prices[right]-prices[left]
                highest=max(highest,profit)
            else:
                left=right
            right += 1
        return highest

    


        
            
        


        
