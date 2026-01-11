from typing import Dict, List
import yaml

def read_yaml_file(yamlfile: str):
    res = None
    with open(yamlfile, 'r') as yF:
        res = yaml.safe_load(yF)
    return res

def is_prime(n: int) -> bool:
    assert n > 1, f"error {n}"

    if n in [2, 3, 5, 7]:
        return True
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True

def get_all_primes(N: int) -> List[int]:
    return [ x for x in range(2,N) if is_prime(x) ]

def profile_primes(begin: int, end: int, step: int, verbose: bool = False, measure_time: bool = False) -> Dict[int, int]:
    import time
    answer = {}
    for N in range(begin, end, step):
        if measure_time:
            start_time = time.perf_counter()   # start timer

        L = get_all_primes(N)              # do your work

        if measure_time:
            end_time = time.perf_counter()     # end timer
            del_time = end_time - start_time   # find how much time it took to do your work

        if measure_time:
            answer[N] = (len(L), del_time*1000)
        else:
            answer[N] = len(L)

        if verbose:
            print(f'...generated {len(L)} primes < {N}')

    return answer


if __name__ == '__main__':
    import time

    experiments = read_yaml_file('./config/experiments.yaml')

    for ii,settings in enumerate(experiments):
        start_time = time.perf_counter()
        result     = profile_primes(**settings)
        end_time   = time.perf_counter()
        del_time   = end_time - start_time
        with open(f'primes_table_exp_{ii}.csv', 'w') as outF:
            outF.write('N,P,T\n')
            for k in result:
                if 'measure_time' in settings and settings['measure_time']:
                    num_primes, time_taken = result[k]
                else:
                    num_primes = result[k]
                    time_taken = -1
                outF.write(f"{k},{num_primes},{time_taken}\n")
        print(f'total time: {del_time:.2f} secs')
