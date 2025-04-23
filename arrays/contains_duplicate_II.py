class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        value_index_map = {}  

        for index, value in enumerate(nums):
            if value in value_index_map:
                if index - value_index_map[value] <= k:
                    return True
            value_index_map[value] = index  

        return False

obj = Solution()
result = obj.containsNearbyDuplicate([1,2,3,1], 3)
print(result)