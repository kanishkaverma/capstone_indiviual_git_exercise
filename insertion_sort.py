
""" Method which performs insertion sort on a list of Integers. 
======
parameters
======
nums: list of Integers
"""
def insertion_sort(nums): 
    #For  loop which goes from 1 to len(nums)
    for i in range(1, len(nums)):
        #current element 
        current = nums[i]
        
        #swap elements until current element is in correct order.  
        j = i-1
        while j >=0 and current < nums[j] :
                nums[j+1] = nums[j]
                j -= 1
        nums[j+1] = current 

    return nums