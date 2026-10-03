import itertools

class Solution(object):
    def minimumString(self, a, b, c):
        """
        :type a: str
        :type b: str
        :type c: str
        :rtype: str
        """
        def merge(s1, s2):
            if s2 in s1:
                return s1
            if s1 in s2:
                return s2
            # Find the maximum overlap between suffix of s1 and prefix of s2
            for i in range(min(len(s1), len(s2)), 0, -1):
                if s1.endswith(s2[:i]):
                    return s1 + s2[i:]
            return s1 + s2

        candidates = []
        for p in itertools.permutations([a, b, c]):
            m1 = merge(p[0], p[1])
            m2 = merge(m1, p[2])
            candidates.append(m2)
        
        # Sort by length first, then lexicographically
        candidates.sort(key=lambda x: (len(x), x))
        return candidates[0]