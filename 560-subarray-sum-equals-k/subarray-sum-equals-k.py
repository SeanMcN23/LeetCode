class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:


    # gonna come back to this one tomorrow, my brain is 2 cooked right now to try this


        map= {0:1}
        res=0
        curSum=0

        for num in nums:

            curSum += num

            diff= curSum - k

            res += map.get(diff,0)

            map[curSum]= 1 + map.get(curSum,0)

        return res
        




