class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #shove all of it into a set cause itll sort it, than pop off as i go tracking how many numbers
        mainSet=set(nums)
        longest=0

        for n in mainSet:
            if (n-1) not in mainSet:
                length=1
                while (n+length) in mainSet:
                    length += 1
                longest= max(length,longest)
        return longest




        
            

            