class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)

        mid = (n - 1) // 2
        large = n - 1

        res = [0] * n

        for i in range(n):
            if i % 2 == 0:
                res[i] = nums[mid]
                mid -= 1
            else:
                res[i] = nums[large]
                large -= 1

        nums[:] = res