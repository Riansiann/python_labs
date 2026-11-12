import random
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


def check_sorting(fn, trials = 100): 
    '''
    Checks that the sorting function fn correctly sorts lists of random integers.
    '''
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for i in range(n)]
        original = nums.copy()
        expected = sorted(nums)
        result = fn(nums)
        assert result == expected, f"Sorting failed for {fn.__name__} with input {nums}: {result}"
        assert nums == original, f"Sorting function {fn.__name__} modified the input list: {nums}"
    return trials


def check_search():
    '''
    Checks that the search functions correctly find elements in lists of random integers.
    '''
    trials = 100
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for i in range(n)]
        targets = [101]  # числа в nums находятся от -100 до 100

        if nums:
            targets.extend([
                nums[0],
                nums[-1],
                random.choice(nums)
            ])
        for x in targets:
            #linear search
            try:
                expected_lin = nums.index(x)
            except ValueError:
                expected_lin = -1

            result_lin = linear_search(nums, x)
            assert result_lin == expected_lin, f'Search failed with input {nums} and target {x}: {result_lin}'


            #binary search
            sorted_nums = sorted(nums)
            result_bin = binary_search(sorted_nums, x)

            if x in sorted_nums:
                assert 0 <= result_bin < len(sorted_nums)
                assert sorted_nums[result_bin] == x
            else:
                assert result_bin == -1
    return 100

def check_two_sum(trials = 100):
    '''
    Checks that the two_sum functions correctly find pairs of indices in lists of random integers that sum to a target value.
    '''
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for i in range(n)]
        if n >= 2 and random.choice([True, False]):
            i, j = random.sample(range(n), 2)
            target = nums[i] + nums[j]
        else:
            target = random.randint(-200, 200)

        expected = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    expected.append((i, j))

        result_brute = two_sum_brute(nums, target)
        result_fast = two_sum_fast(nums, target)

        if expected:
            assert result_brute in expected, f'Two sum failed with input {nums} and target {target}: {result_brute}'
            assert result_fast in expected, f'Two sum failed with input {nums} and target {target}: {result_fast}'
        else:
            assert result_brute == None, f'Two sum failed with input {nums} and target {target}: {result_brute}'
            assert result_fast == None, f'Two sum failed with input {nums} and target {target}: {result_fast}'
    return trials


if __name__ == "__main__":
    random.seed(42)
    total = 0
    for fn in (bubble_sort, insertion_sort, selection_sort):
        total += check_sorting(fn)
    total += check_search() 
    total += check_two_sum()
    print(f'OK: {total} tests passed')