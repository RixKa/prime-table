import sys
import logging
from tabulate import tabulate

from helper.primes import get_n_primes
from helper.input_handler import prompt_user, validate_input

logger = logging.getLogger()
logging.basicConfig(
    format='[  %(asctime)s - %(levelname)-6s - %(module)s ]  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger.setLevel('DEBUG')


def main():
    logger.info('prompting for user input')
    n = prompt_user()

    logger.info('validating input')
    while not validate_input(n): n = prompt_user(True)

    logger.info('retrieving prime numbers')
    primes = get_n_primes(int(n))
    logger.debug('primes: {}'.format(primes))

    logger.info('generating table matrix')
    table = [[None] + primes] + [ [p2] + [ p1*p2 for p1 in primes ] for p2 in primes ]
    logger.debug('table: {}'.format(table))

    logger.info('generating table')
    return tabulate(table, tablefmt='orgtbl')


if __name__  == '__main__':
    print "\nCoding Exercise - Prime tables\n"
    if '-d' not in sys.argv:
        logger.disabled = True

    table = main()
    print table
    print "\n"
