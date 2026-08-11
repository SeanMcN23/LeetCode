class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        # so the idea is to utilize with k, the most possible elements we can make that equal one another, can only increase elements by 1,
        # max we have is whatever k may be

        # so knowing that, question becomes now, using the windows, how can I build upon a freq for each window i have?
        # so the idea is this, we need the max window length and another thing, we need to know the max in the actual list or window portion that we have:

        nums.sort() # need to sort the given array first

        l=0
        myMax=0
        total=0

        for r in range(len(nums)):
            total += nums[r]
            while nums[r] * (r - l + 1) > total + k:
                total -= nums[l]
                l += 1
            myMax=max(myMax,((r-l )+1))
        return myMax





        