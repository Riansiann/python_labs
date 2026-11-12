def bubble_sort(nums):
    '''
    Sorts a list of numbers in ascending order using the bubble sort algorithm.
    Returns the sorted list.
    '''
    nums = list(nums)
    n = len(nums)

    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        if not swapped:
            break
    return nums

def insertion_sort(nums):
    '''
    Sorts a list of numbers in ascending order using the insertion sort algorithm.
    Returns the sorted list.
    '''
    nums = list(nums)
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key
    return nums 

def selection_sort(nums):
    '''
    Sorts a list of numbers in ascending order using the selection sort algorithm.
    Returns the sorted list.
    '''
    nums = list(nums)

    for i in range(len(nums)):
        min_index = i

        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums
