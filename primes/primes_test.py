from primes import PrimeChecker
import pytest

@pytest.fixture

def primes():
    yield PrimeChecker()

def test_is_negative_prime(primes):
    assert primes.is_prime(-1) is False
    assert primes.is_prime(-2) is False
    assert primes.is_prime(-3) is False

def test_is_0_prime(primes):
    assert primes.is_prime(0) is False

def test_is_1_prime(primes):
    assert primes.is_prime(1) is False

def test_is_2_prime(primes):
    assert primes.is_prime(2) is True

def test_is_3_prime(primes):
    assert primes.is_prime(3) is True

def test_is_4_prime(primes):
    assert primes.is_prime(4) is False

def test_is_5_prime(primes):
    assert primes.is_prime(5) is True

def test_is_6_prime(primes):
    assert primes.is_prime(6) is False

def test_is_7_prime(primes):
    assert primes.is_prime(7) is True

def test_is_8_prime(primes):
    assert primes.is_prime(8) is False

def test_is_9_prime(primes):
    assert primes.is_prime(9) is False

def test_is_10_prime(primes):
    assert primes.is_prime(10) is False

def test_is_11_prime(primes):
    assert primes.is_prime(11) is True

def test_fail_check_pipeline(primes):
    assert primes.is_prime(2) is False