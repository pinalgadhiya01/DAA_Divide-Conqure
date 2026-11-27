class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
    
        ans = ""

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sub = s[i:j]

                if all(ch.swapcase() in sub for ch in sub):
                    if len(sub) > len(ans):
                        ans = sub

        return ans