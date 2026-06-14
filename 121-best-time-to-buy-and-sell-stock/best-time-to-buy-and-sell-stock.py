class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #sliding window approach, need 2 pointers, one a scout, one is reserver
        res, scout= 0,0 

        highest=0

        for scout in range(len(prices)):
            while prices[res] > prices[scout]:
                res += 1
            
            if prices[scout] > prices[res]:
                highest=max(highest,prices[scout]-prices[res])
        return highest
        



        





            

    


        
            
        


        
