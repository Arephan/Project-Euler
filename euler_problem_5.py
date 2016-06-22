from euler_problem_3 import *

def find_max_power_prime_in_range(range_i, range_f):
    """Record the power of a prime if it's higher than previous power of the same prime. 
    """
    max_power_primes = {}
    for x in range(range_i, range_f+1):
        prime_count = {}
        if not is_a_prime(x):
            prime_factors = find_prime_factors(x)
            
            for y in prime_factors:
                if y in prime_count:
                    prime_count[y] += 1
                else:
                    prime_count[y] = 1

            for z in prime_count: 
                if max_power_primes[z] < prime_count[z]:
                    max_power_primes[z] = prime_count[z]
        else:
            max_power_primes[x] = 1
            
    return max_power_primes

def find_smallest_evenly_divisible_integer_of_range(range_i, range_f): 
    """Find an integer evenly divisble by all integers between range_i and range_f
    """
    max_power_primes = find_max_power_prime_in_range(range_i, range_f)
    sum = 1
    for x in max_power_primes:
        sum *= math.pow(x,max_power_primes[x])
        
    return sum

def test_answer(num, range_i, range_f):
    """Tests the answer by dividing num by every number between specified range
    """ 
    print num

    for x in range(range_i, range_f+1):
        print x, num%x