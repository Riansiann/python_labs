import random
import timeit

from src.lab04.io_txt_csv import write_csv
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


def bench_sorts():
    random.seed(42)

    functions = [
        ('bubble_sort', bubble_sort),
        ('insertion_sort', insertion_sort),
        ('selection_sort', selection_sort)
    ]
    results = []

    sizes = [1_000, 10_000, 100_000]
    for n in sizes:
        data = [random.randint(-1_000_000, 1_000_000) for _ in range(n)]
        sorted_time = timeit.timeit(lambda: sorted(data), number=1)
        results.append(['sort', n, 'sorted', sorted_time])

        if n <= 10_000:
            for fn_name, fn in functions:
                time = timeit.timeit(lambda: fn(data), number=1)
                results.append(['sort', n, fn_name, time])
        else:
            for fn_name, fn in functions:
                results.append(['sort', n, fn_name, 'skipped'])

    return results


def bench_search():
    random.seed(42)
    n = 100_000
    results = []

    data = [random.randint(-1_000_000, 1_000_000) for _ in range(n)]
    targets = [random.choice(data) for _ in range(10_000)]

    linear_time = timeit.timeit(lambda: [linear_search(data, x) for x in targets], number=1)
    results.append(['search', n, 'linear_search', linear_time])

    sort_time = timeit.timeit(lambda: sorted(data), number=1)
    sorted_data = sorted(data)
    binary_time = timeit.timeit(lambda: [binary_search(sorted_data, x) for x in targets], number=1)
    results.append(['search', n, 'pre_sort', sort_time])
    results.append(['search', n, 'binary_search', binary_time])
    results.append(['search', n, 'binary_with_sort', sort_time + binary_time])

    for n in [1_000, 10_000]:
        ts_data = [random.randint(-1_000_000, 1_000_000) for _ in range(n)]
        a, b = random.sample(ts_data, 2)
        target = a + b

        time_brute = timeit.timeit(lambda: two_sum_brute(ts_data, target), number=1)
        results.append(['two_sum', n, 'two_sum_brute', time_brute])

        time_fast = timeit.timeit(lambda: two_sum_fast(ts_data, target), number=1)
        results.append(['two_sum', n, 'two_sum_fast', time_fast])

    return results


def main():
    header = ('task', 'n', 'impl', 'seconds')
    results = []
    results.extend(bench_sorts())
    results.extend(bench_search())

    for row in results:
        if isinstance(row[3], (int, float)):
            row[3] = f'{row[3]:.6f}'

    path = 'data/lab07/bench.csv'
    write_csv(results, path, header)

    print(f'Benchmarking completed. Results written to {path}')
    print('\nResults:')
    print(f"{'task':<12} | {'n':<10} | {'impl':<20} | {'seconds':>12}")
    print('-' * 63)
    for task, n, impl, seconds in results:
        print(f'{task:<12} | {n:<10} | {impl:<20} | {seconds:>12}')


if __name__ == '__main__':
    main()
