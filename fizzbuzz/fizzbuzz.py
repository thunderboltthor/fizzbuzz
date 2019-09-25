import click
import sys


def is_valid_countable_number(n):
    """Returns True if n is a countable number"""

    return False


def process(n):
    """Returns the string representation of integer n unless:
       - n is evenly divisible by 3 (returns 'Fizz')
       - n is evenly divisible by 5 (returns 'Buzz')
       - n is evenly divisible by both 3 and 5 (returns 'FizzBuzz')"""

    return ''


@click.command()
@click.option('-n', default=100, help='A positive integer')
def main(n):

    # Validate input
    if not is_valid_countable_number(n):
        print("the value of n must me a non-zero integer")
        sys.exit()

    # Iterate from 1 to n inclusive and print FizzBuzz
    for i in range(1, n+1):
        print(process(i))


if __name__ == '__main__':
    main()
