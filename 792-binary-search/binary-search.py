class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # need 2 pointers, cause we need midpoint
        l,r= 0, len(nums)-1
        # we need <= because we need to consider if an array only has 1 option
        while l <= r:
            m= (l+r)//2

            if nums[m] < target:
                l= m+1
            elif nums[m] > target:
                r= m-1
            else:
                return m
        return -1
        

            

        