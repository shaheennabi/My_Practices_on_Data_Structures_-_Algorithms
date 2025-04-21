class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        end = len(digits) - 1

        
        while end >= 0:
            if digits[end] < 9:
                digits[end] += 1
                return digits  
            else:
                digits[end] = 0  
            end -= 1

        
        return [1] + digits

obj = Solution()
result = obj.plusOne([9,8,7,6,9])
print(result)