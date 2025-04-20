class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0 
        j = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j +=1
                k += 1 
            else:
                continue
        return k
    

obj = Solution()
result = obj.removeElement([3,2,2,3], 3)
print(result)