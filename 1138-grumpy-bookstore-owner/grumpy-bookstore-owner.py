class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        # so for this problem, we want maximium satisfaction of customers, we dont know where that might come from, but 
        # what we do know is we have minutes, so we can make him not grumpy for x mins
        # what if l and r should be the length of how many minutes this particular owner can keep bro from being grumpy?
        window,maxwindow=0,0
        l=0
        satisfied=0

        for r in range(len(customers)):
            if grumpy[r]:
                window += customers[r]
            else:
                satisfied += customers[r]
            
            if (r-l)+1 > minutes:
                if grumpy[l]:
                    window -= customers[l]
                l+= 1
            
            maxwindow=max(maxwindow,window)
        return maxwindow + satisfied
            
             




        