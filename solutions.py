import argparse

def problem1():
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    """
    total = 0
    for n in xrange(1000):
        if (n % 3 == 0) or (n % 5 == 0):
            total += n
    return total

def problem2():
    """
    Each new term in the Fibonacci sequence is generated by adding the
    previous two terms.

    By considering the terms in the Fibonacci sequence whose values do not
    exceed four million, find the sum of the even-valued terms.
    """
    total = 0
    t0, t1, t2 = 0, 1, 0
    while t0 <= 4000000:
        if t0 % 2 == 0:
            total += t0
        t2, t1 = t1, t0
        t0 = t2 + t1
    return total

def problem3():
    """
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
    """
    from math import floor, ceil, sqrt
    number = 600851475143

    def factor(num):
        for n in xrange(2, int(ceil(sqrt(num)))):
            if num % n == 0:
                return n, num / n
        return None, num

    f1, f2 = 1, number
    while f1 is not None:
        f1, f2 = factor(f2)
    return f2

def problem4():
    """
    A palindromic number reads the same both ways. The largest palindrome
    made from the product of two 2-digit numbers is 9009 = 91 x 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    def is_palindrome(num):
        num = str(num)
        digits = len(num)
        for i in xrange(int(digits / 2 + 1)):
            if num[i] != num[digits - i - 1]:
                return False
        else:
            return True

    best = 0
    for i in xrange(100, 1000):
        for j in xrange(i, 1000):
            if is_palindrome(i * j):
                best = max(best, i * j)
    return best

def problem5():
    """
    2520 is the smallest number that can be divided by each of the numbers
    from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of
    the numbers from 1 to 20?
    """
    i = 20
    while True:
        for j in xrange(1, 21):
            if i % j != 0:
                break
        else:
            return i
        i += 20
    return i

def problem6():
    """
    Find the difference between the sum of the squares of the first one
    hundred natural numbers and the square of the sum.
    """
    sum_of_sqr = (100 * 101 * 201) / 6
    sqr_of_sum = (100 * (100 + 1) / 2) ** 2
    return abs(sum_of_sqr - sqr_of_sum)

def problem7():
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
    see that the 6th prime is 13.

    What is the 10 001st prime number?
    """
    primes = [2, 3, 5, 7, 11, 13, 17, 19]

    i = 21
    while len(primes) < 10001:
        for p in primes:
            if i % p == 0:
                break
        else:
            primes.append(i)
        i += 2
    return primes[-1]

def problem8():
    """
    Find the greatest product of five consecutive digits in the given number.
    """
    number = (
        "73167176531330624919225119674426574742355349194934"
        "96983520312774506326239578318016984801869478851843"
        "85861560789112949495459501737958331952853208805511"
        "12540698747158523863050715693290963295227443043557"
        "66896648950445244523161731856403098711121722383113"
        "62229893423380308135336276614282806444486645238749"
        "30358907296290491560440772390713810515859307960866"
        "70172427121883998797908792274921901699720888093776"
        "65727333001053367881220235421809751254540594752243"
        "52584907711670556013604839586446706324415722155397"
        "53697817977846174064955149290862569321978468622482"
        "83972241375657056057490261407972968652414535100474"
        "82166370484403199890008895243450658541227588666881"
        "16427171479924442928230863465674813919123162824586"
        "17866458359124566529476545682848912883142607690042"
        "24219022671055626321111109370544217506941658960408"
        "07198403850962455444362981230987879927244284909188"
        "84580156166097919133875499200524063689912560717606"
        "05886116467109405077541002256983155200055935729725"
        "71636269561882670428252483600823257530420752963450"
    )
    product = 0
    for i in xrange(len(number) - 4):
        digits = [int(char) for char in number[i:i+5]]
        product = max(product, reduce(lambda x,y: x*y, digits))
    return product

def problem9():
    """
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for
    which, a^2 + b^2 = c^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    """
    for a in xrange(1, 334):
        for b in xrange(a, 667):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                return a * b * c
    return None

def problem10():
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
    """
    limit = 2000000
    sieve = [True for x in xrange(limit)]
    total = 0

    for i in xrange(2, limit):
        if sieve[i]:
            total += i
            for j in xrange(i, limit, i):
                sieve[j] = False
    return total

def problem12():
    """
    The sequence of triangle numbers is generated by adding the natural numbers.

    What is the first triangle number to have over five hundred divisors?
    """
    from math import sqrt
    def triangles():
        total, i = 1, 1
        while True:
            yield total
            i += 1
            total += i

    for x in triangles():
        divisors = 2 # - (1, x)
        for i in xrange(2, int(sqrt(x)+1)):
            if x % i == 0:
                if x / i == i:
                    divisors += 1
                else:
                    divisors += 2
        if divisors > 500:
            return x

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--problem', '-p', type=int,
        help='problem number to evaluate, if completed')

    args = parser.parse_args()
    if args.problem:
        try:
            result = globals()['problem' + str(args.problem)]()
            print 'Problem ' + str(args.problem) + ': ' + str(result)
        except KeyError:
            print 'Problem ' + str(args.problem) + ': Function not found'
