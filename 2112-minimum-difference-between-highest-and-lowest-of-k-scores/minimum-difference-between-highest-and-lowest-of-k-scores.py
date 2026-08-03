class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        l,r=0, k-1
        nums.sort()
        res=float('inf')

        while r != len(nums):
            res= min(res,nums[r]-nums[l])
            r += 1
            l += 1
        return res


                




