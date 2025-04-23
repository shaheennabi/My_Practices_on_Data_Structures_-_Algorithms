class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        unique = set()

        for i in nums:
            if i in unique:
                return True

            else:
                unique.add(i)
        
        return False

obj = Solution()
result = obj.containsDuplicate([1,2,3,1])
print(result)