import math 

def is_a_prime(n):
    """Test that there are no remainders when n is divided by x in range between 2 and sqrt(n)
    """
    for x in range(2, int(math.sqrt(n)+1)):
        if(n%x == 0):
            return 0
    return 1

def find_next_prime(n):
    """Continuously add 1 to n until prime is found
    """
    next_prime_found = 0
    
    while(not next_prime_found):
        n += 1
        if(is_a_prime(n)):
            next_prime_found = 1
        
    return n

def find_prime_factors(n):
    """while greatest prime isn't found, find next prime
    """
    current_prime = 2
    prime_factors = []
    greatest_prime_found = 0
    
    while(not greatest_prime_found):
        if(n%current_prime == 0):
            prime_factors.append(current_prime)
            n = n/current_prime
            if (n == 1):
                greatest_prime_found = 1
        else:
            current_prime = find_next_prime(current_prime)
    
    return prime_factors