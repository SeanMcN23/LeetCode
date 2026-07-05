class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
       
        l,r= 0, len(nums)-1
        
        while l<= r:
            while nums[r] == val and r >=0:
                r -= 1
           
            if nums[l] == val and l<r:
                nums[l],nums[r]= nums[r],nums[l]
            
               
            
            l += 1
        return r+1
            
        