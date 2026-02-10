class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        scout=1
        highest=0

        while scout != len(prices):
            if prices[res]<prices[scout]:
                highest=max(prices[scout]-prices[res],highest)
                
            else:
                res=scout
            scout += 1
        return highest

            

    


        
            
        


        
