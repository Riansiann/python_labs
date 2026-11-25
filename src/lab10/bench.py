import timeit
from collections import deque

from src.lab04.io_txt_csv import write_csv
from src.lab10.linked_list import ll_prepend


def bench_pops():
    """
    Compare the execution times of list.pop(0) and deque.popleft()
    Return benchmark results for different sizes
    """
    result_pop = []

    for n in (10_000, 100_000):
        num_list = list(range(n))
        num_q = deque(range(n))

        list_time_p = timeit.timeit(lambda: num_list.pop(0), number = n)
        que_time_p = timeit.timeit(lambda: num_q.popleft(), number = n)

        result_pop.append(['pop(0)/popleft()', n, f'{list_time_p:.6f}', f'{que_time_p:.6f}', f'{list_time_p / que_time_p:.1f}'])
        
    return result_pop
    
def bench_inserts():
    """
    Compare the execution times of list.insert(0, x) and ll_prepend()
    Return benchmark results for different sizes
    """
    result_insert = []

    for n in (10_000, 100_000):
        nums = []

        list_time_ins = timeit.timeit(lambda: nums.insert(0, 10), number = n)

        head = None 

        def ll_prep_op():
            """
            Prepend a node and update the linked list head
            """
            nonlocal head
            head = ll_prepend(head, 10)

        ll_time_ins = timeit.timeit(ll_prep_op, number = n)

        result_insert.append(['insert/ll_prepend', n, f'{list_time_ins:.6f}',  f'{ll_time_ins:.6f}', f'{list_time_ins / ll_time_ins:.1f}'])

    return result_insert

def main():
    header = ('operation', 'n', 'list', 'deque/ll', 'ratio')
    results = []
    results.extend(bench_pops())
    results.extend(bench_inserts())   

    path = 'data/lab10/bench.csv'
    write_csv(results, path, header)

    print(f'Benchmarking completed. Results written to {path}')
    print('\nResults:')
    print(f"{'operation':<20} | {'n':>10} | {'list_res':>15} | {'deq_ll_res':>15} | {'ratio':>12}")
    print("-" * 85)

    for operation, n, list_res, deq_ll_res, ratio in results:
        print(f"{operation:<20} | {n:>10} | {list_res:>15} | {deq_ll_res:>15} | {ratio:>12}")


if __name__ == '__main__':
    main()
