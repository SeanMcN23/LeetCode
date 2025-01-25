class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i, x in enumerate(nums):
            if i > 0 and x == nums[i-1]:
                continue
            j = i+1
            k= len(nums)-1
            while j < k:
                total = x+ nums[j] + nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    ans.append([x, nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j-1] and j<k:
                        j += 1
        return ans





        