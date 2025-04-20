class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 1
        unique_values = 1  
        start = 1

        while start < len(nums):  
            if nums[start] != nums[start - 1]:
                nums[j] = nums[start]
                j += 1
                unique_values += 1
            start += 1  

        return unique_values

obj =  Solution()
result = obj.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(result)