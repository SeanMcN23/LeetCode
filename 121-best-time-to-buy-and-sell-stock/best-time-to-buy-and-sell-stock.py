class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #sliding window approach, need 2 pointers, one a scout, one is reserver
        scout=1
        res=0
        highest=0

        while scout != len(prices):
            while prices[scout] < prices[res]:
                res += 1
            if prices[scout]>prices[res]:
                highest=max(highest,prices[scout]-prices[res])
                
            scout += 1
        return highest




            

    


        
            
        


        
