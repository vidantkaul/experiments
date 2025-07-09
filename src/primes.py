
def is_prime(n: int) -> bool:
    assert isinstance(n, int) and n > 1, f"Error: input ({n}) should be a int and > 1"

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def generate_primes(n: int):
    assert isinstance(n, int) and n > 1, f"Error: input ({n}) should be a int and > 1"
    return [x for x in range(2,n+1) if is_prime(x)]

if __name__ == '__main__':

    for N in range(10, 1000, 10):
        L = generate_primes(N)
        print(N, len(L))
