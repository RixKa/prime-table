import sys
import random
import logging
from tabulate import tabulate

from helper.primes import get_n_primes
from helper.input_handler import prompt_user, validate_input

logger = logging.getLogger()
logging.basicConfig(
    format='[  %(asctime)s - %(levelname)-6s - %(module)s ]  %(message)s'
)

logger.setLevel('INFO')


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
    table = main()
    print table
