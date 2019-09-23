import click


class FizzBuzz(object):
    def __init__(self):
        """Instantiation method (currently does nothing)"""
        pass

    def isValidCountableNumber(self, n):
        """Returns True if n is a countable number"""
        return False

    def print(self, i):
        """Returns the string representation of a number unless:
           - the number is evenly divisible by 3 (returns 'Fizz')
           - the number is evenly divisible by 5 (returns 'Buzz')
           - the number is evenly divisible by both 3 and 5 (returns 'FizzBuzz')"""
        return ''


@click.command()
@click.option('-n', default=100, help='A positive integer')
def main(n):

    # Instantiate the FizzBuzz object
    fizzbuzz = FizzBuzz()

    # Validate input
    if (not fizzbuzz.isValidCountableNumber(n)):
        print("the value of n must me a non-zero integer")
        sys.exit()

    # Iterate from 1 to n inclusive and print FizzBuzz
    for i in range(1, n+1):
        print(fizzbuzz.print(i))


if __name__ == '__main__':
    main()
