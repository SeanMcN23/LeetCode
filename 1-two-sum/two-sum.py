class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}

        for ind, num in enumerate(nums):
            print(num,ind)
           
            if target-num in map:
                
                return ind,map[target-num]
            else:
                map[num]=ind
               
           
       
            
        