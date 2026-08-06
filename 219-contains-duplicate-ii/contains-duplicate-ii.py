class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # so basically, this is all about keep track of numbers if they duplicate, then see if they are less then k spaces away

        myHash=set() # need this to keep track of both number but also position of number

        l=0

        for r in range(len(nums)):
            
            
            if (r-l) > k:
                myHash.remove(nums[l])
                l+= 1
            if nums[r] in myHash:
                return True
            
            myHash.add(nums[r])
        return False


            



        