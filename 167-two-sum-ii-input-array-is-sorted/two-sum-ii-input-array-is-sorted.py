class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r= 0, len(numbers)-1

        while l <= r:
            curr= numbers[l] + numbers[r]

            if target< curr:
                r -= 1
            if target > curr:
                l += 1
            if target == curr:
                return [l+1,r+1]
        return []

