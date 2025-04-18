class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_count = {}  # storing character counts

        # First pass: counting characters
        for ch in s:
            if ch in char_count:
                char_count[ch] += 1
            else:
                char_count[ch] = 1

        # Second pass: find index of first non-repeating character
        for idx, ch in enumerate(s):
            if char_count[ch] == 1:
                return idx

        return -1  # No non-repeating character found

obj = Solution().firstUniqChar("leetcode")
print(obj)