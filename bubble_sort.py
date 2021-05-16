""" Method which performs bubble sort on a list of Integers. 
======
parameters
======
nums: list of Integers
"""
def bubble_sort(nums): 
    N = len(nums)
  
    # Traverse array elements  
    for i in range(N-1):
  
        for j in range(0, N-i-1):
            
            # Swap if the element found is greater
            # than the next element
            if nums[j] > nums[j+1] :
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return nums