class Solution(object):
    def strStr(self, haystack, needle):

        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)

        # Edge case: if needle is empty, return 0
        if m == 0:
            return 0

        for i in range(n - m + 1):  # ensure we don’t go out of bounds
            if haystack[i:i+m] == needle:
                return i

        return -1



                    


