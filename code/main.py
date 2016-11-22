import random
import logging

from helper.primes import get_n_primes

logger = logging.getLogger()
logging.basicConfig(
    format='[  %(asctime)s - %(levelname)-6s - %(module)s ]  %(message)s'
)

logger.setLevel('DEBUG')


def main():
    # logger.info('prompting for user input')
    # TODO: Prompt for n

    # logger.info('validating input')
    # TODO: check input is valid

    logger.info('assigning random value for n')
    n = random.randint(2,100)
    logger.debug('n: {}'.format(n))

    logger.info('retrieving prime numbers')
    primes = get_n_primes(n)
    logger.debug('primes: {}'.format(primes))

if __name__  == '__main__':
    logger.info('starting')
    main()
    logger.info('completed')
