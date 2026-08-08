class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        total = sum(nums)

        # Maximum subarray sum
        curr_max = 0
        max_sum = nums[0]

        # Minimum subarray sum
        curr_min = 0
        min_sum = nums[0]

        for num in nums:
            curr_max = max(num, curr_max + num)
            max_sum = max(max_sum, curr_max)

            curr_min = min(num, curr_min + num)
            min_sum = min(min_sum, curr_min)

        # All numbers are negative
        if max_sum < 0:
            return max_sum

        return max(max_sum, total - min_sum)