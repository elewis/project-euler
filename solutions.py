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

def problem11():
    """
    What is the greatest product of four adjacent numbers in the same
    direction (up, down, left, right, or diagonally) in the 20x20 grid?
    """
    grid = [
        map(int, "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08".split(' ')),
        map(int, "49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00".split(' ')),
        map(int, "81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65".split(' ')),
        map(int, "52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91".split(' ')),
        map(int, "22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80".split(' ')),
        map(int, "24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50".split(' ')),
        map(int, "32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70".split(' ')),
        map(int, "67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21".split(' ')),
        map(int, "24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72".split(' ')),
        map(int, "21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95".split(' ')),
        map(int, "78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92".split(' ')),
        map(int, "16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57".split(' ')),
        map(int, "86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58".split(' ')),
        map(int, "19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40".split(' ')),
        map(int, "04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66".split(' ')),
        map(int, "88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69".split(' ')),
        map(int, "04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36".split(' ')),
        map(int, "20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16".split(' ')),
        map(int, "20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54".split(' ')),
        map(int, "01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48".split(' ')),
    ]

    def rows(grid):
        return iter(grid)
    def cols(grid):
        for i in xrange(len(grid[0])):
            yield [row[i] for row in grid]
    def diags(grid):
        for x in xrange(len(grid[0])):
            yield [grid[y][xi] for xi, y in zip(xrange(x, len(grid[0])), xrange(0, len(grid) - x))]
            yield [grid[y][xi] for xi, y in zip(xrange(x, len(grid[0])), xrange(len(grid)-1, x-1, -1))]
        for y in xrange(1, len(grid)):
            yield [grid[yi][x] for x, yi in zip(xrange(0, len(grid[0]) - y), xrange(y, len(grid)))]
            yield [grid[yi][x] for x, yi in zip(xrange(0, len(grid[0]) - y), xrange(len(grid)-y-1, -1, -1))]

    def products(L):
        if len(L) >= 4:
            for i in xrange(len(L) - 3):
                yield reduce(lambda x,y: x*y, L[i:i+4])

    best = 0
    for row in rows(grid):
        p = list(products(row))
        if len(p) > 0:
            best = max(best, *p)
    for col in cols(grid):
        p = list(products(col))
        if len(p) > 0:
            best = max(best, *p)
    for diag in diags(grid):
        p = list(products(diag))
        if len(p) > 0:
            best = max(best, *p)
    return best

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
        divisors = 2 # 1 and x
        for i in xrange(2, int(sqrt(x)+1)):
            if x % i == 0:
                if x / i == i:
                    divisors += 1
                else:
                    divisors += 2
        if divisors > 500:
            return x

def problem13():
    """
    Work out the first ten digits of the sum of the following one-hundred
    50-digit numbers.
    """
    import requests, re

    numbers = requests.get('http://www.projecteuler.net/problem=13').text
    numbers = map(int, re.findall('([0-9]+)<br', numbers))
    return str(sum(numbers))[:10]

def problem14():
    """
    The following iterative sequence is defined for the set of positive integers:

    n => n/2 (n is even)
    n => 3n + 1 (n is odd)

    Which starting number, under one million, produces the longest chain?
    """
    def seq(x):
        yield x
        while x > 1:
            x = x/2 if x % 2 == 0 else 3*x + 1
            yield x

    best = 1, 1
    for i in xrange(1, 1000000):
        pathlen = sum(1 for _ in seq(i))
        if pathlen > best[1]:
            best = i, pathlen
    return best[0]

def problem15():
    """
    Starting in the top left corner of a 2x2 grid, and only being able to move
    to the right and down, there are exactly 6 routes to the bottom right corner.

    How many such routes are there through a 20x20 grid?
    """
    dimension = 20,20
    grid = [[0 for x in xrange(dimension[0]+1)] for y in xrange(dimension[1]+1)]
    for x in xrange(dimension[0]+1):
        grid[x][0] = 1
    for y in xrange(dimension[1]+1):
        grid[0][y] = 1

    for i in xrange(1, dimension[0]+1):
        for j in xrange(1, dimension[1]+1):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
    return grid[dimension[0]][dimension[1]]

def problem16():
    """
    215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2^1000?
    """
    number = 2**1000
    total = 0
    while number > 0:
        total += number % 10
        number /= 10
    return total

def problem17():
    """
    If the numbers 1 to 5 are written out in words: one, two, three, four,
    five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written
    out in words, how many letters would be used?
    """
    ones = [
        '', 'one', 'two', 'three', 'four', 'five',
        'six', 'seven', 'eight', 'nine', 'ten',
        'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
        'sixteen', 'seventeen', 'eighteen', 'nineteen'
    ]
    tens = [
        '', '', 'twenty', 'thirty', 'forty', 'fifty',
        'sixty', 'seventy', 'eighty', 'ninety'
    ]
    total = 0
    for i in xrange(1, 1000):
        word = ''
        if i >= 100:
            word += ones[i/100] + 'hundred'
            if i%100 != 0:
                word += 'and'
        if i%100 < 20:
            word += ones[i%100]
        else:
            word += tens[i/10%10] + ones[i%10]
        total += len(word)
    return total + 11 # to include 1000

def problem18():
    """
    By starting at the top of the triangle below and moving to adjacent
    numbers on the row below, the maximum total from top to bottom is 23.

    Find the maximum total from top to bottom of the triangle below:
    """
    triangle = [
        [75],
        [95, 64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20,  4, 82, 47, 65],
        [19,  1, 23, 75,  3, 34],
        [88,  2, 77, 73,  7, 63, 67],
        [99, 65, 04, 28,  6, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33],
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        [63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [04, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]
    ]
    # Destructive dynamic programming, bubbles up max path length
    depth = len(triangle)-2
    while depth >= 0:
        row = triangle[depth]
        children = triangle[depth+1]
        for i in xrange(len(row)):
            row[i] += max(children[i], children[i+1])
        depth -= 1
    return triangle[0][0]

def problem19():
    """
    You are given the following information, but you may prefer to do some
    research for yourself.

        1 Jan 1900 was a Monday.
        Thirty days has September,
        April, June and November.
        All the rest have thirty-one,
        Saving February alone,
        Which has twenty-eight, rain or shine.
        And on leap years, twenty-nine.
        A leap year occurs on any year evenly divisible by 4, but not on a
            century unless it is divisible by 400.

    How many Sundays fell on the first of the month during the twentieth
    century (1 Jan 1901 to 31 Dec 2000)?
    """
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap   = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def is_leap_year(year):
        if year % 100 == 0:
            return year % 400 == 0
        else:
            return year % 4 == 0

    def is_sunday(day, month, year): # [0-max], [0-11], YYYY
        day_offset = 1 # sequence starts on a monday
        for nyear in xrange(1900, year):
            day_offset += 366 if is_leap_year(nyear) else 365

        if is_leap_year(year):
            day_offset += sum(leap[:month]) + day
        else:
            day_offset += sum(months[:month]) + day

        return day_offset % 7 == 0

    sundays = 0
    for year in xrange(1901, 2001):
        for month in xrange(0, 12):
            if is_sunday(0, month, year):
                sundays += 1
    return sundays

def problem20():
    """
    Find the sum of the digits in the number 100!
    """
    number = reduce(lambda x,y: x*y, xrange(1, 101))
    total = 0
    while number > 0:
        total += number % 10
        number /= 10
    return total

def problem21():
    """
    Let d(n) be defined as the sum of proper divisors of n (numbers less than
    n which divide evenly into n). If d(a) = b and d(b) = a, where a != b, then
    a and b are an amicable pair and each of a and b are called amicable
    numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
    44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1,
    2, 4, 71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.
    """
    limit = 10000
    sieve = [[] for i in xrange(limit)]
    total = 0

    for i in xrange(1, limit):
        if sieve[i]:
            pair = sum(sieve[i]), i
            if pair[0] < pair[1] and sum(sieve[pair[0]]) == pair[1]:
                total += pair[0] + pair[1]
        for j in xrange(2 * i, limit, i):
            sieve[j].append(i)
    return total

def problem22():
    """
    Using names.txt, a 46K text file containing over five-thousand first
    names, begin by sorting it into alphabetical order. Then working out
    the alphabetical value for each name, multiply this value by its
    alphabetical position in the list to obtain a name score.

    For example, when the list is sorted into alphabetical order, COLIN,
    which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
    So, COLIN would obtain a score of 938 x 53 = 49714.

    What is the total of all the name scores in the file?
    """
    import requests

    names = requests.get('http://www.projecteuler.net/project/names.txt').text
    names = map(lambda name: name[1:-1], names.strip().split(','))
    names.sort()

    def score(name):
        ascii_offset = 96
        name = list(name.lower())
        return sum(map(lambda c: ord(c) - ascii_offset, name))

    total = 0
    for i in xrange(len(names)):
        total += score(names[i]) * (i+1)
    return total

def problem23():
    """
    A perfect number is a number for which the sum of its proper divisors is
    exactly equal to the number. For example, the sum of the proper divisors
    of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
    number.

    A number n is called deficient if the sum of its proper divisors is less
    than n and it is called abundant if this sum exceeds n.

    Find the sum of all the positive integers which cannot be written as the
    sum of two abundant numbers.
    """
    limit = 28123
    sieve = [[] for i in xrange(limit)]
    abundant = set()

    for i in xrange(1, limit):
        if sieve[i] and sum(sieve[i]) > i:
            abundant.add(i)
        for j in xrange(2 * i, limit, i):
            sieve[j].append(i)

    total = 0
    for i in xrange(1, limit):
        for j in abundant:
            if i - j in abundant:
                break
        else:
            total += i
    return total

def problem24():
    """
    What is the millionth lexicographic permutation of the digits
    0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
    """
    limit = 1000000

    def permutations(digits):
        if len(digits) > 0:
            for i in xrange(len(digits)):
                for p in permutations(digits[:i] + digits[i+1:]):
                    yield digits[i] + p
        else:
            yield ''

    permute = permutations('0123456789')
    for j in xrange(limit - 1):
        next(permute)
    return next(permute)

def problem25():
    """
    What is the first term in the Fibonacci sequence to contain 1000 digits?
    """

    def fib():
        f0, f1 = 0, 1
        yield 1
        while True:
            yield f1 + f0
            f1, f0 = f1 + f0, f1

    for i, n in enumerate(fib()):
        if len(str(n)) == 1000:
            return i + 1

def problem26():
    """
    Find the value of d < 1000 for which 1/d contains the longest recurring
    cycle in its decimal fraction part.
    """
    limit = 1000
    best = 0, 0

    def cycle(d):
        remainders, r = {}, 1
        length = 0

        while r > 0 and r not in remainders:
            remainders[r] = length
            r = (r * 10) % d
            length += 1
        return length

    for i in xrange(1, limit):
        length = cycle(i)
        if length > best[0]:
            best = length, i
            if best[0] >= limit:
                break
    return best[1] # Problem statement is find d, not cycle length

def problem28():
    """
    Starting with the number 1 and moving to the right in a clockwise
    direction a 5 by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

    It can be verified that the sum of the numbers on the diagonals is 101.

    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
    formed in the same way?
    """
    size = 1001

    def spiral_diag(n):
        """Generator of values in diagonals of a spiral using n numbers."""
        i, step = 1, 2
        yield i
        while i < n:
            for j in xrange(4):
                i += step
                yield i
            step += 2

    return sum(spiral_diag(size ** 2))

def problem29():
    """
    How many distinct terms are in the sequence generated by ab for
    2 <= a <= 100 and 2 <= b <= 100?
    """
    terms = set()
    for a in xrange(2, 101):
        for b in xrange(2, 101):
            terms.add(a ** b)
    return len(terms)

def problem30():
    """
    Find the sum of all the numbers that can be written as the sum of fifth
    powers of their digits.
    """
    powers = [0, 1, 32, 243, 1024, 3125, 7776, 16807, 32768, 59049]

    def digits(number):
        while number > 0:
            yield number % 10
            number /= 10

    total, i = 0, 3
    while i < 1000000:
        num_total = 0
        for d in digits(i):
            num_total += powers[d]
        if num_total == i:
            total += i
        i += 1
    return total

def problem31():
    """
    How many different ways can 2 pounds be made using any number of coins?
    """
    coins = (1, 2, 5, 10, 20, 50, 100, 200)
    amount = 200
    table = [[0 for c in xrange(amount+1)] for i in xrange(len(coins))]

    for c in xrange(amount+1):
        for i in xrange(len(coins)):
            if c - coins[i] < 0:
                table[i][c] = table[i - 1][c]
            elif c - coins[i] == 0:
                table[i][c] = table[i - 1][c] + 1
            else:
                table[i][c] = table[i][c - coins[i]] + table[i - 1][c]
    return table[-1][-1]

def problem32():
    """
    We shall say that an n-digit number is pandigital if it makes use of all
    the digits 1 to n exactly once; for example, the 5-digit number, 15234,
    is 1 through 5 pandigital.

    The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing
    multiplicand, multiplier, and product is 1 through 9 pandigital.

    Find the sum of all products whose multiplicand/multiplier/product
    identity can be written as a 1 through 9 pandigital.
    """

    def permutations(digits):
        if len(digits) > 0:
            for i in xrange(len(digits)):
                for p in permutations(digits[:i] + digits[i+1:]):
                    yield digits[i] + p
        else:
            yield ''

    product_set = set()
    for p in permutations('123456789'):
        for i in xrange(1, len(p) / 3 + 1):
            for j in xrange(i + 1, len(p) / 3 * 2 + 1):
                triplet = int(p[:i]), int(p[i:j]), int(p[j:])
                if triplet[0] * triplet[1] == triplet[2]:
                    product_set.add(triplet[2])
    return sum(product_set)

def problem33():
    """
    The fraction 49/98 is a curious fraction, as an inexperienced
    mathematician in attempting to simplify it may incorrectly believe
    that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

    We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

    There are exactly four non-trivial examples of this type of fraction,
    less than one in value, and containing two digits in the numerator and
    denominator.

    If the product of these four fractions is given in its lowest common
    terms, find the value of the denominator.
    """
    from fractions import Fraction

    keep = []

    for numer in xrange(10, 100):
        for denom in xrange(numer + 1, 100):

            if (numer % 10 == 0 and denom % 10 == 0) or\
               (numer % 11 == 0 and denom % 11 == 0):
                continue

            ndigits = [numer // 10, numer % 10]
            ddigits = [denom // 10, denom % 10]

            if ndigits[0] in ddigits:
                ddigits.remove(ndigits[0])
                ndigits.remove(ndigits[0])
            elif ndigits[1] in ddigits:
                ddigits.remove(ndigits[1])
                ndigits.remove(ndigits[1])
            else:
                continue

            if ddigits[0] != 0 and\
                Fraction(ndigits[0], ddigits[0]) == Fraction(numer, denom):
                keep.append(Fraction(numer, denom))

    return reduce(lambda x,y: x*y, keep).denominator


def problem34():
    """
    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

    Find the sum of all numbers which are equal to the sum of the factorial
    of their digits.

    Note: as 1! = 1 and 2! = 2 are not sums they are not included.
    """
    facs = [1, 1, 2, 6, 24, 120, 720, 504, 40320, 362880]

    def digits(number):
        while number > 0:
            yield number % 10
            number /= 10

    total, i = 0, 3
    while i < 1000000:
        num_total = 0
        for d in digits(i):
            num_total += facs[d]
        if num_total == i:
            total += i
        i += 1
    return total

def problem35():
    """
    The number, 197, is called a circular prime because all rotations of the
    digits: 197, 971, and 719, are themselves prime.

    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
    71, 73, 79, and 97.

    How many circular primes are there below one million?
    """
    limit = 1000000
    sieve = [True for x in xrange(limit)]

    def rotations(digits):
        for i in xrange(len(digits)):
            yield digits[i:] + digits[:i]

    for i in xrange(2, limit):
        for j in xrange(i * 2, limit, i):
            sieve[j] = False

    count = 0
    for i in xrange(2, limit):
        if sieve[i]:
            for p in rotations(str(i)):
                if not sieve[int(p)]:
                    break
            else:
                count += 1
    return count

def problem36():
    """
    Find the sum of all numbers, less than one million, which are palindromic
    in base 10 and base 2.
    """
    limit = 1000000
    total = 0

    def is_palindrome(num_str):
        for i in xrange(len(num_str) / 2):
            if num_str[i] != num_str[-1 - i]:
                return False
        return True

    for i in xrange(limit):
        if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]):
            total += i
    return total

def problem37():
    """
    Find the sum of the only eleven primes that are both truncatable from
    left to right and right to left.
    """
    limit = 1000000
    total = 0
    sieve = [True for x in xrange(limit)]

    def is_truncatable(i):
        left = right = str(i)
        while len(left) > 0 and len(right) > 0:
            if not is_prime(int(left)) or not is_prime(int(right)):
                return False
            else:
                left, right = left[1:], right[:-1]
        return True

    def is_prime(i):
        return sieve[i]

    sieve[0] = False
    sieve[1] = False
    for i in xrange(2, limit):
        for j in xrange(i * 2, limit, i):
            sieve[j] = False

    for i in xrange(11, limit, 2):
        if is_truncatable(i):
            total += i
    return total

def problem38():
    """
    Take the number 192 and multiply it by each of 1, 2, and 3:

        192 x 1 = 192
        192 x 2 = 384
        192 x 3 = 576

    By concatenating each product we get the 1 to 9 pandigital, 192384576.
    We will call 192384576 the concatenated product of 192 and (1,2,3)

    The same can be achieved by starting with 9 and multiplying by 1, 2, 3,
    4, and 5, giving the pandigital, 918273645, which is the concatenated
    product of 9 and (1,2,3,4,5).

    What is the largest 1 to 9 pandigital 9-digit number that can be formed as
    the concatenated product of an integer with (1,2, ... , n) where n > 1?
    """
    limit = 10000
    best = 0

    def is_pandigital(num_str):
        return ''.join(sorted(num_str)) == "123456789"[:len(num_str)]

    for i in xrange(limit):
        num_str = ""
        for j in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            num_str += str(i * j)
            if is_pandigital(num_str) and int(num_str) > best:
                best = int(num_str)
                break
            elif len(num_str) > 9:
                break
    return best

def problem39():
    """
    If p is the perimeter of a right angle triangle with integral length sides,
    {a,b,c}, there are exactly three solutions for p = 120.

    {20,48,52}, {24,45,51}, {30,40,50}

    For which value of p <= 1000, is the number of solutions maximised?
    """
    limit = 1000
    best = 0, 0

    for p in xrange(1, limit + 1):
        solutions = 0
        for a in xrange(1, p/3 + 1):
            for b in xrange(a + 1, p/2):
                c = p - b - a
                if a ** 2 + b ** 2 == c ** 2:
                    solutions += 1
        if solutions > best[0]:
            best = solutions, p
    return best[1]

def problem40():
    """
    An irrational decimal fraction is created by concatenating the positive
    integers:

    0.123456789101112131415161718192021...

    It can be seen that the 12th digit of the fractional part is 1.

    If dn represents the nth digit of the fractional part, find the value
    of the following expression.

    d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
    """
    d, i = "", 1
    while len(d) <= 1000001:
        d += str(i)
        i += 1
    digits = map(int, [d[0], d[9], d[99], d[999], d[9999], d[99999], d[999999]])
    return reduce(lambda x,y: x*y, digits)

def problem41():
    """
    We shall say that an n-digit number is pandigital if it makes use of
    all the digits 1 to n exactly once. For example, 2143 is a 4-digit
    pandigital and is also prime.

    What is the largest n-digit pandigital prime that exists?
    """
    from random import randint

    def permutations(digits):
        if len(digits) > 0:
            for i in xrange(len(digits)):
                for p in permutations(digits[:i] + digits[i+1:]):
                    yield digits[i] + p
        else:
            yield ''

    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def is_prime(n):
        if pow(2, n, n) != 2:
            return False
        for i in xrange(50):
            a = randint(2, n-1)
            if gcd(n, a) == 1 and pow(a, n-1, n) != 1:
                return False
        return True

    best = 2143
    for j in xrange(1, 10):
        for i in permutations(''.join(map(str, xrange(1, j+1)))):
            i = int(i)
            if i > best:
                if is_prime(i):
                    best = i
    return best

def problem42():
    """
    The nth term of the sequence of triangle numbers is given by,
    tn = (1/2)n(n+1); so the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    By converting each letter in a word to a number corresponding to its
    alphabetical position and adding these values we form a word value.
    For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the
    word value is a triangle number then we shall call the word a triangle
    word.

    How many of the words in words.txt are triangle words?
    """
    import requests

    words = requests.get('http://projecteuler.net/project/words.txt').text
    words = words.strip().split(',')
    score_count = {}

    # Generates all triangles up to and including t_n
    def triangles(n):
        for i in xrange(1, n+1):
            yield i * (i+1) / 2

    def score(word):
        total = 0
        for c in word:
            total += ord(c) - 96 # Ascii offset
        return total

    max_score = 0
    for word in words:
        word = word.strip('"').lower()
        word_score = score(word)
        if word_score > max_score:
            max_score = word_score
        if word_score in score_count:
            score_count[word_score] += 1
        else:
            score_count[word_score] = 1

    total = 0
    for t in triangles(max_score):
        if t in score_count:
            total += score_count[t]
    return total

def problem43():
    """
    The number, 1406357289, is a 0 to 9 pandigital number because it is made
    up of each of the digits 0 to 9 in some order, but it also has a rather
    interesting sub-string divisibility property.

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

    Find the sum of all 0 to 9 pandigital numbers with this property.
    """

    def permutations(digits):
        if len(digits) > 0:
            for i in xrange(len(digits)):
                for p in permutations(digits[:i] + digits[i+1:]):
                    yield digits[i] + p
        else:
            yield ''

    factors = 2, 3, 5, 7, 11, 13, 17
    total = 0
    for digits in permutations('0123456789'):
        for i in xrange(1, 8):
            if int(digits[i:i+3]) % factors[i-1] != 0:
                break
        else:
            total += int(digits)
    return total

def problem44():
    """
    Pentagonal numbers are generated by the formula, Pn=n(3n-1)/2. The first
    ten pentagonal numbers are:

    1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

    It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference,
    70 - 22 = 48, is not pentagonal.

    Find the pair of pentagonal numbers, Pj and Pk, for which their sum and
    difference are pentagonal and D = |Pk - Pj| is minimised; what is the value
    of D?
    """
    p_n = lambda n: n * (3*n - 1) / 2
    plst = [p_n(i) for i in xrange(1, 10001)]
    pset = set(plst)

    min_d = max(plst)
    for i in xrange(1, len(plst)):
        for j in xrange(i, len(plst)):
            sum_ = plst[i] + plst[j]
            dif_ = abs(plst[i] - plst[j])
            if sum_ in pset and dif_ in pset:
                min_d = min(min_d, dif_)
    return min_d



def problem48():
    """
    The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

    Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
    """
    N = 10**10
    return sum([pow(i, i, N) for i in xrange(1, 1001)]) % N

def problem49():
    """
    The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
    increases by 3330, is unusual in two ways: (i) each of the three terms
    are prime, and, (ii) each of the 4-digit numbers are permutations of
    one another.

    There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
    primes, exhibiting this property, but there is one other 4-digit
    increasing sequence.

    What 12-digit number do you form by concatenating the three terms in
    this sequence?
    """

    def permutations(digits):
        if len(digits) > 0:
            for i in xrange(len(digits)):
                for p in permutations(digits[:i] + digits[i+1:]):
                    yield digits[i] + p
        else:
            yield ''

def problem50():
    """
    Which prime, below one-million, can be written as the sum of the most
    consecutive primes?
    """
    limit = 1000000
    sieve = [True for x in xrange(limit)]
    primes = []

    for i in xrange(2, limit):
        if sieve[i]:
            primes.append(i)
            for j in xrange(2*i, limit, i):
                sieve[j] = False

    primeset = set(primes)
    best = (1, 1)
    for i in xrange(len(primes)):
        total = 0
        for j in xrange(i, len(primes)):
            total += primes[j]
            if total >= limit:
                break
            elif total in primeset and j-i > best[1]:
                best = total, j-i
    return best[0]

def problem52():
    """
    It can be seen that the number, 125874, and its double, 251748, contain
    exactly the same digits, but in a different order.

    Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
    contain the same digits.
    """
    def digits(number):
        while number > 0:
            yield number % 10
            number /= 10

    i = 1
    while True:
        products = [i*j for j in xrange(1, 7)]
        testdigits = [sorted(digits(p)) for p in products]

        for test in testdigits:
            if test != testdigits[0]:
                break
        else:
            return i
        i += 1

def problem59():
    """
    A modern encryption method is to take a text file, convert the bytes to
    ASCII, then XOR each byte with a given value, taken from a secret key.
    The advantage with the XOR function is that using the same encryption
    key on the cipher text, restores the plain text; for example,
    65 XOR 42 = 107, then 107 XOR 42 = 65.

    Unfortunately, this method is impractical for most users, so the modified
    method is to use a password as a key. If the password is shorter than the
    message, which is likely, the key is repeated cyclically throughout the
    message. The balance for this method is using a sufficiently long password
    key for security, but short enough to be memorable.

    Your task has been made easy, as the encryption key consists of three
    lower case characters. Using cipher1.txt, a file containing the encrypted
    ASCII codes, and the knowledge that the plain text must contain common
    English words, decrypt the message and find the sum of the ASCII values
    in the original text.
    """
    import requests

    def keys():
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for a in alphabet:
            for b in alphabet:
                for c in alphabet:
                    yield ord(a), ord(b), ord(c)

    # Cipher ASCII codes given by the problem
    cipher = requests.get('http://projecteuler.net/project/cipher1.txt').text
    cipher = map(int, cipher.strip().split(','))

    # English word dictionary (all uppercase, separated by newlines)
    english = requests.get('http://inventwithpython.com/dictionary.txt').text
    english = set(english.strip().split('\n'))

    for key in keys():
        # Decrypt bytes
        message, ascii, i = '', [], 0
        while i < len(cipher):
            char = cipher[i] ^ key[i % len(key)]
            message += chr(char)
            ascii.append(char)
            i += 1

        # Determine if output is likely english text
        words = message.split(' ')
        count = 0
        for word in words:
            if word.upper() in english:
                count += 1
        if count * 1.0 / len(words) > 0.5:
            return sum(ascii)

def problem67():
    """
    By starting at the top of the triangle below and moving to adjacent
    numbers on the row below, the maximum total from top to bottom is 23.

    Find the maximum total from top to bottom in triangle.txt, a 15K text
    file containing a triangle with one-hundred rows.

    NOTE: This is a much more difficult version of problem 18.
    """
    import requests

    triangle = []
    rows = requests.get('http://projecteuler.net/project/triangle.txt').text
    rows = rows.strip().split('\n')
    for row in rows:
        triangle.append(map(int, row.split(' ')))

    # Destructive dynamic programming, bubbles up max path length
    depth = len(triangle)-2
    while depth >= 0:
        row, children = triangle[depth], triangle[depth+1]
        for i in xrange(len(row)):
            row[i] += max(children[i], children[i+1])
        depth -= 1
    return triangle[0][0]

def run_problem(number):
    try:
        result = globals()['problem' + str(number)]()
        print 'Problem ' + str(number) + ': ' + str(result)
    except KeyError:
        print 'Problem ' + str(number) + ': Function not found'

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--problem', '-p', type=int,
        help='problem number to evaluate, if completed')

    args = parser.parse_args()
    if args.problem:
        run_problem(args.problem)
    else:
        for i in xrange(1, 200):
            run_problem(i)
