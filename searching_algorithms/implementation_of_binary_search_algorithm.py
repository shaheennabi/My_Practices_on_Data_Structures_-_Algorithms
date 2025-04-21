class Search_Algorithm():
    def binary_search_algorithm(self, nums: list, target: int):

        start = 0  
        end  = len(nums) - 1  

        while start<=end:
            mid = (start + end) // 2 

            if nums[mid] == target:
                return mid 
            
            elif nums[mid] < target:
                start = mid + 1  

            else: 
                end = mid - 1 

        return -1 
    
    
nums = [-1,0,3,5,9,12]
target = 0   
obj =  Search_Algorithm()
result = obj.binary_search_algorithm(nums, target)
print(result)



    
