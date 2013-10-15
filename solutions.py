import argparse

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
