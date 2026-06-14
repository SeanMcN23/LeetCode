class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start,end= 0, len(numbers)-1

        while start < end:
            val= target-numbers[end]

            if val < numbers[start]:
                end -= 1
            elif val > numbers[start]:
                start += 1
            else:
                return [start+1,end+1]

