class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[0] * len(nums)
        prefix=1
        for index,x in enumerate(nums):

            ans[index] = prefix
            prefix *= x
        postfix=1
        for index,x in reversed(list(enumerate(nums))):

            ans[index] *= postfix
            postfix *= x
        return ans


        

        