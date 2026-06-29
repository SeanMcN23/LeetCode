class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,0
        highest=0

        for r in range(len(prices)):
            while prices[r] < prices[l]:
                l += 1

            if prices[r] > prices[l]:
                highest=max(highest,prices[r]-prices[l])
        return highest







        





            

    


        
            
        


        
