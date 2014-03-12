#!usr/bin/env python

def primes(maxp):
    """
    Returns a two item tuple. The first item is a list of prime numbers less
    than maxp in increasing order. The second is the set constructed from
    the same list of primes for faster lookups.
    """
    # Implemented using the Sieve of Eratosthenes
    sieve = [True for x in xrange(maxp)]
    prime_lst = [1]
    prime_set = set(prime_lst)

    for i in xrange(2, maxp):
        if sieve[i]:
            prime_lst.append(i)
            prime_set.add(i)
            for j in xrange(2*i, maxp, i):
                sieve[j] = False
    return prime_lst, prime_set

def permutations(s):
    """
    Generator returns all possible permutations of the string s.
    """
    if len(s) == 0:
        yield s
    else:
        for i in xrange(len(s)):
            for p in permutations(s[:i] + s[i+1:]):
                yield s[i] + p

def gcd(a, b):
    """
    Returns the greatest common denominator of a and b.
    """
    # Implemented using Euclid's extended algorithm
    while b != 0:
        a, b = b, a % b
    return a

def digits(n):
    """
    Generator returns the digits of int n from least to most significant.
    """
    while n > 0:
        yield n % 10
        n /= 10
