class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # def a sliding window, have a target and some array, goal is to reach the target
        sum=0
        l=0
        myMin=float('inf')

        for r in range(len(nums)):   
            sum += nums[r]
            print(sum)

            while sum >= target:
                myMin=min(myMin,(r-l)+1)
                sum -= nums[l]
                l += 1

           # if sum == target:
               # myMin=min(myMin,(r-l)+1)
                
            
           
        return myMin if myMin != float('inf') else 0
        