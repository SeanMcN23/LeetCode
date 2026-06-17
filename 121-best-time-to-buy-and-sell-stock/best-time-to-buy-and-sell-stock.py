class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #sliding window approach, need 2 pointers, one a scout, one is reserver
        res,sco=0,0

        highest=0

        while sco < len(prices):

            while prices[res] > prices[sco]:
                res += 1
            
            if prices[sco] > prices[res]:
                highest=max(highest, prices[sco]-prices[res])
            sco += 1
            
        return highest





        





            

    


        
            
        


        
