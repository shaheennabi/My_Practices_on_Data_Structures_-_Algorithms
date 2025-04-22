class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_number = 0

        for i in nums:
            unique_number ^= i

        return unique_number;       

obj = Solution()
result = obj.singleNumber([4,1,2,1,2])
print(result)