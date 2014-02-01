import argparse

parser = argparse.ArgumentParser(description="")
parser.add_argument(
    'square',
    type=int,
    help='outputs square of a given number'
)
parser.add_argument(
    '-v',
    '--verbose',
    action='store_true'
)
args = parser.parse_args()

answer = args.square ** 2

if args.verbose:
    print('the square of {} equals {}'
          .format(args.square, answer))
else:
    print(answer)