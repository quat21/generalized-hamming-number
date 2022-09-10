from typing import List, Tuple
import math
import numpy as np
import matplotlib.pyplot as plt

def is_prime(num: int) -> bool:
    '''Return True if num is prime.'''
    for i in range(2, int(math.sqrt(num)) + 1):
        if num%i == 0:
            return False
    return True

def prime_list(max_num: int) -> List[int]:
    '''Return a list of primes less than or equal to max_num.'''
    return [num for num in range(2, max_num + 1) if is_prime(num)]

def generalized_hamming_number_count_recursive(num: int, primes: List[int], threshold: int, last_prime_index: int) -> int:
    '''Recursively count the number of hamming numbers by traversing a tree of in-order prime factorizations.'''
    if num > threshold:
        # terminating condition
        return 0
    count = 1 # count for current node
    for i, prime in enumerate(primes[last_prime_index:]):
        # add counts of child nodes
        count += generalized_hamming_number_count_recursive(num * prime, primes, threshold, i + last_prime_index)
    return count

def generalized_hamming_number_count(type: int, threshold: int) -> int:
    '''Wrapper for recursive implementation.'''
    primes = prime_list(type)
    return generalized_hamming_number_count_recursive(1, primes, threshold, 0)

def valid_graph_parameters(max_type: int, min_type: int, max_threshold: int, min_threshold: int, granularity: int) -> bool:
    '''Validate graph parameters.'''
    if granularity <= 10:
        print('granularity too low')
        return False
    if max_type <= min_type:
        print('max_type too low')
        return False
    min_threshold = 100
    if max_threshold <= min_threshold:
        print('max_threshold too low')
        return False
    x_step = (max_type - min_type) // granularity
    y_step = (max_threshold - min_threshold) // granularity
    if x_step <= 0 or y_step <= 0:
        print('granularity is too high for given type and threshold values.')
        return False
    return True

def generate_data(max_type: int, min_type: int, max_threshold: int, min_threshold: int, granularity: int) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    '''Generate x, y, and z values for hamming number counts and given parameters.'''
    x_step = (max_type - min_type) // granularity
    y_step = (max_threshold - min_threshold) // granularity
    x_list = [i for i in np.arange(min_type, max_type + 1, x_step)]
    y_list = [i for i in np.arange(min_threshold, max_threshold + 1, y_step)]
    xs, ys = np.meshgrid(x_list, y_list)
    z_list = [generalized_hamming_number_count(x, y) for x, y in zip(np.ravel(xs), np.ravel(ys))]
    zs = np.array(z_list).reshape(xs.shape)
    return xs, ys, zs

def generate_graph(x: np.ndarray, y: np.ndarray, z: np.ndarray):
    '''Generate a surface graph with the given x, y, and z values.'''
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot_surface(x, y, z)
    ax.set_xlabel('Type')
    ax.set_ylabel('Threshold')
    ax.set_zlabel('Hamming number count')

def graph(max_type: int, max_threshold: int, granularity: int):
    '''Plot a surface of generalized hamming number counts with various type and thresholds.'''
    min_type = 2
    min_threshold = 100
    if not valid_graph_parameters(max_type, min_type, max_threshold, min_threshold, granularity):
        return
    x, y, z = generate_data(max_type, min_type, max_threshold, min_threshold, granularity)
    generate_graph(x, y, z)
    plt.show()

if __name__ == '__main__':
    print(f"Number of generalized hamming numbers of type 100 which don't exceed 10^9: {generalized_hamming_number_count(100, 10**9)}")
    graph(100, 10**4, 11)
