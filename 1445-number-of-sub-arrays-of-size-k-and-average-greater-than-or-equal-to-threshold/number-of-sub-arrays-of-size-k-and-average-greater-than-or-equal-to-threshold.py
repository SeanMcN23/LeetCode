class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        left = 0
        window_sum = 0
        counter = 0
        required_sum = k * threshold

        for right in range(len(arr)):
            window_sum += arr[right]

            if right - left + 1 > k:
                window_sum -= arr[left]
                left += 1

            if right - left + 1 == k:
                if window_sum >= required_sum:
                    counter += 1

        return counter

        