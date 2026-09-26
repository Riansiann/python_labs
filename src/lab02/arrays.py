def min_max(nums: list[float|int]) -> tuple[float|int, float|int]:
    """
    This function takes a list of numbers (integers or floats) and returns a tuple containing the minimum and maximum values from that list.
    """
    if not nums:
        raise ValueError('The list cannot be empty')
    for _ in nums:
        try:
            float(_)
        except ValueError:
            raise ValueError('The list must contain only numbers')        

    maxnums, minnums = nums[0], nums[0]
    for num in nums:
        if num > maxnums:
            maxnums = num
        elif num < minnums:
            minnums = num
    return minnums, maxnums

#test cases
print(min_max([3,-1,5,5,0]))
print(min_max([42]))
print(min_max([-5,-2,-9]))
print(min_max([1.5,2,2.0,-3.1]))
print(min_max([]))

def bubble_sort(nums: list[float|int]) -> list[float|int]:
    """
    This function takes a list of numbers (integers or floats) and sorts it in ascending order using the bubble sort algorithm.
    """
    for i in range(len(nums)):
        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

def unique_sorted(nums: list[float|int]) -> list[float|int]:
    """
    This function returns a sorted list of numbers (integers or floats) with duplicates removed.
    """
    for _ in nums:  
        try:
            float(_)
        except ValueError:
            raise ValueError('The list must contain only numbers')

    unique_nums = []
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)

    unique_sorted_nums = bubble_sort(unique_nums)
    return unique_sorted_nums

#test cases
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([-1,-1,0,2,2]))
print(unique_sorted([]))
print(unique_sorted([1.0,1,2.5,2.5,0]))


def flatten(mat: list[list|tuple]) -> list:
    """
    This function returns a flattened version of matrix as a single list.
    """
    if not mat:
        raise ValueError('The matrix cannot be empty')
    res = []
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError('Each row must be a list or tuple')
        for el in row:
            res.append(el)
    return res
#test cases
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3,4,5)]))
print(flatten([[1], [], [2,3]]))
print(flatten([[1, 2], 'ab']))
        




