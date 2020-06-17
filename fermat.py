import random

# This is main function, that is connected to the Test button. 
def prime_test(N, k):
	return fermat(N,k), miller_rabin(N,k)

"""Computes x^y mod N using a iterative algorithm"""
def mod_exp(x, y, N):
    if y == 0:
        return 1
    remainder = 1
    for i in range(y):
        # Repeat y times: r = r * x % N
        remainder = (remainder * x) % N
    return remainder

"""Determines the probability of the fermat algorithm where at least half of 
   the possible values of 'a' are between 2 and N-1 are prime""" 
   
def fprobability(k): 
    return 1 - 0.5**k

"""Determines the probability of the miller rabin algorithm where at least 
   one-fourth of the possible values of 'a' are between 2 and N-2 are prime"""
def mprobability(k):
    return 1 - 0.25**k

"""Determines the largest positive integer that divides each of the integers"""
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

"""Returns a randomize coprime number with N and a is in the range [2,N-1]"""
def coprime(N):
    # Pick a at random
    a = random.randint(2, N - 1)
    # if the gcd between N and a is not 1: pick another randomize a
    if gcd(N, a) != 1:
        return coprime(N)
    else:
        return a

"""A primality algorithm that determines whether a number is prime excluding 
   Carmichael numbers"""
def fermat(N,k):
    # Specify the corner cases
    if N <= 1 or N == 4:
        return 'composite'
    if N <= 3:
        return 'prime'
    
    for i in range(k):
        # Pick a randomize coprime number 'a'
        a = coprime(N)
        # if ai^(N-1) % N does not equal 1 : composite
        if mod_exp(a, N-1, N) != 1:
            return 'composite'
    return 'prime'

"""A primality algorithm that determines whether a number is prime, but 
   correctly classifies Carmichael numbers, which are odd composite numbers 
   that satisfy Fermat's little theorem, as not prime"""
def miller_rabin(N,k):
    isPrime = fermat(N,k)
    if isPrime == 'prime':
        for i in range(k):
            # Pick a1, a2, ... , ak < N at random
            a = random.randint(2, N - 1)
            y = N - 1
            r = 1
            # Determines r in 2^r * odd number
            # (the number of times the square root of a^(N-1) is taken)
            while y % 2 == 0:
                y = int(y / 2)
                r += 1
            y = N - 1
            # if the remainder is not -1 or 1, the number is composite
            for i in range(r):
                remainder = mod_exp(a, int(y), N)
                if remainder == -1:
                    return 'prime'
                if remainder != 1:
                    return 'composite'
        return 'prime'
    return 'composite'
