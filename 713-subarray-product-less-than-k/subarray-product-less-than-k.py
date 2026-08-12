class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        #nums.sort()

        if len(nums) == 1:
            if nums[0] > k:
                return 0
            else:
                return 1
            


        l=0
        myMax=0
        mySum=1
        windowlen=0
        for r in range(len(nums)):

            mySum *= nums[r]

            while mySum >= k:
                
                mySum /= nums[l]
                l += 1
            
            windowlen += (r-l)+1

            
            myMax=max(myMax,windowlen)
        return myMax
