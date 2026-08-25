class Solution(object):
    def countElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        ans = 0

        for x in nums:
            pos = bisect_right(nums, x)
            if n - pos >= k:
                ans += 1

        return ans