from typing import List
import time
import math

def is_prime(num: int) -> bool:
    '''Return True if num is prime'''
    for i in range(2, int(math.sqrt(num)) + 1):
        if num%i == 0:
            return False
    return True

def prime_list(max_num: int) -> List[int]:
    '''Return a list of primes less than or equal to max_num.'''
    return [num for num in range(2, max_num + 1) if is_prime(num)]

def is_hamming(x: int, primes: List[int]) -> bool:
    '''Return True if the number is a hamming number for a given list of primes.'''
    while x not in primes:
        divisible = False
        for prime in primes:
            if x%prime == 0:
                x /= prime
                divisible = True
                break
        if not divisible:
            return False
    return True

def hamming_count(type: int, threshold: int) -> int:
    '''Return the number of generalized hamming numbers of a given type below a given threshold.'''
    primes = prime_list(type)
    count = 1
    for i in range(2, threshold + 1):
        if is_hamming(i, primes):
            count += 1
    return count

if __name__ == '__main__':
    # implementation too slow for hamming numbers of type 5 which don't exceed 10^9
    start = time.time()
    print(hamming_count(5, 10**8))
    print(time.time() - start)