class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.n = len(nums)
        self.tree = [0] * (self.n + 1)

        # Build Fenwick Tree
        for i, num in enumerate(nums):
            self._add(i + 1, num)

    def _add(self, index, val):
        # Fenwick Tree update
        while index <= self.n:
            self.tree[index] += val
            index += index & -index

    def _prefix_sum(self, index):
        # Sum from 0 to index (1-based Fenwick index)
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        diff = val - self.nums[index]
        self.nums[index] = val

        # Apply difference to Fenwick Tree
        self._add(index + 1, diff)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self._prefix_sum(right + 1) - self._prefix_sum(left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)