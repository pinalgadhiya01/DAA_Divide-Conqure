class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)

        
        prefix = [0]
        s = 0
        for x in nums:
            s += 1 if x == target else -1
            prefix.append(s)

        ans = 0
        # Count pairs (i, j) with prefix[j] > prefix[i]
        for j in range(1, n + 1):
            for i in range(j):
                if prefix[j] > prefix[i]:
                    ans += 1

        return ans

