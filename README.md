# Coding Exercise - Prime tables

## Introduction
This is an application that takes numeric input (N) from a user and outputs a multiplication table of (N) prime numbers.

#### Example
Input: `N = 3`

Output:

|       |     2 |     3 |     5 |
|-------|-------|-------|-------|
| **2** |     4 |     6 |    10 |
| **3** |     6 |     9 |    15 |
| **5** |    10 |    15 |    25 |

## Setup
Installation instructions.

`make venv`

## Run
Run instructions.

`make run`

## Testing
Testing instructions.

`make test`

#### Manual Testing:
```
  # Run all tests
  py.test -vra test/

  # Run specific test module
  py.test -vra test/test_input_handler.py

  # Run specific test class
  py.test -vra test/test_prime.py::TestIsPrime

  # Run specific unit test in class
  py.test -vra test/test_prime.py::TestIsPrime::test_n_is_not_prime
```
