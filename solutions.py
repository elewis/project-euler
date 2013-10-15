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
        except:
            print 'Problem ' + str(args.problem) + ': Execution failed'
