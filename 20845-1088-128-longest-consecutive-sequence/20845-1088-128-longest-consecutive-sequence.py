class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #shove all of it into a set cause itll sort it, than pop off as i go tracking how many numbers

        numSet= set(nums)
        longest=0

        for x in numSet:
            if x-1 not in numSet:
                length=1
                while(x+length) in numSet:
                    length +=1
                longest= max(longest,length)
        return longest
        