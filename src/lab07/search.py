def linear_search(nums, x):
    '''Returns the index of x, or -1.'''
    for i, num in enumerate(nums):
        if num == x:
            return i
    return -1

def binary_search(sorted_nums, x):
    '''
    Returns the index of x, or -1.
    The list must be sorted in ascending order.
    For an unsorted list, the result is undefined.
    '''
    lo, hi = 0, len(sorted_nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_nums[mid] == x:
            return mid
        elif sorted_nums[mid] < x:
            lo = mid + 1
        elif sorted_nums[mid] > x:
            hi = mid - 1
    return -1

def two_sum_brute(nums, target):
    '''
    Returns a tuple of indices (i, j) such that nums[i] + nums[j] == target, 
    or None if no such pair exists.
    Use a brute-force approach with O(n^2) time complexity.
    '''
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j
    return None

def two_sum_fast(nums, target):
    '''
    Returns a tuple of indices (i, j) such that nums[i] + nums[j] == target, or None if no such pair exists.
    Use a hash map approach with O(n) time complexity.
    '''
    complements = {}
    for j in range(len(nums)):
        complement = target - nums[j]
        if complement in complements:
            i = complements[complement]
            return i, j
        complements[nums[j]] = j
    return None

