class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        scout=1
        highest=0

        while scout<len(prices):
            if prices[scout]>prices[res]:
                highest=max(highest,prices[scout]-prices[res])
            else:
                res=scout
            scout += 1
        return highest

            

    


        
            
        


        
