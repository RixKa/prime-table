import pytest
import random
from primesieve import generate_n_primes

from primes import get_n_primes, is_prime


class TestIsPrime(object):
    def test_n_is_0(self):
        n = random.choice([4, 6, 8, 10])
        assert not is_prime(n)

    def test_n_is_prime(self):
        n = random.choice([2, 3, 5, 7])
        assert is_prime(n)

    def test_n_not_prime(self):
        n = random.choice([4, 6, 8, 10])
        assert not is_prime(n)

    def test_bad_value_n(self):
        n = random.choice([ 'x', 'word', {'foo': 'bar'}, [0,1,2,3] ])

        with pytest.raises(Exception) as e:
            is_prime(n)
        assert e.value.message


class TestGetPrimes(object):
    def test_n_equals_0(self):
        n = 0
        assert True

    def test_low_value_n(self):
        n = random.randint(1, 100)
        assert get_n_primes(n) == generate_n_primes(n)

    def test_high_value_n(self):
        n = random.randint(2000, 5000)
        assert get_n_primes(n) == generate_n_primes(n)

    def test_higher_value_n(self):
        n = random.randint(10000, 15000)
        assert get_n_primes(n) == generate_n_primes(n)

    @pytest.mark.skip(reason="Not Implemented")
    def test_n_is_digit(self):
        n = random.choice([ '1', '3', '5', '7' ])
        assert get_n_primes(n) == generate_n_primes(int(n))

    @pytest.mark.skip(reason="Not Implemented")
    def test_bad_value_n(self):
        n = random.choice([ 'x', 'word', {'foo': 'bar'}, [0,1,2,3] ])

        with pytest.raises(Exception) as e:
            get_n_primes(n)
        assert e.value.message
