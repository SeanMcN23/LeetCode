class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #sliding window approach, need 2 pointers, one a scout, one is reserver
        res,scout=0,0
        highest=0

        while scout != len(prices):
            while prices[res] > prices[scout]:
                res += 1
            
            if prices[res] < prices[scout]:
                highest=max(highest, prices[scout]-prices[res])
            scout += 1
        return highest


        





            

    


        
            
        


        
