class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        all_nums = set(range(1, n + 1))
        present = set(nums)
        return list(all_nums - present)

obj = Solution()
result = obj.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
print(result)