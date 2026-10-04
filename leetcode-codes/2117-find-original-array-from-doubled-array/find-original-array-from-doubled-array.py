class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """

        if len(changed) % 2 != 0:
            return []

        count = {}

        for num in changed:
            count[num] = count.get(num, 0) + 1

        original = []

        changed.sort()

        for num in changed:
            if count[num] == 0:
                continue

            # Need 2 * num
            if count.get(2 * num, 0) == 0:
                return []

            original.append(num)

            count[num] -= 1
            count[2 * num] -= 1

        return original