class Solution(object):
    def smallestTrimmedNumbers(self, nums, queries):
        """
        :type nums: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        answer = []

        for k, trim in queries:
            # Sort by trimmed value, then by original index
            indices = sorted(
                range(len(nums)),
                key=lambda i: (nums[i][-trim:], i)
            )

            answer.append(indices[k - 1])

        return answer