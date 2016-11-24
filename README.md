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

## Notes
This project is designed to have modular components loosely coupled to ensure dependencies are kept to a minimum. The modularity of these components makes it easy to maintain and replace functions without it impacting too much on the remaining codebase.

The logic in this codebase is separated into relevant modules and test modules, this aims for a highly cohesive solution. The symmetry between the helper modules and test modules is intuitive: for example the `is_prime` function within the `primes.py` module has three tests in the `TestIsPrime` class within the `test_primes.py` module.

Ultimately what I like about this project is that it is simple and slimline, by using TDD principles I could ensure that nothing was put in that wasn't needed. I am particularly fond on the modular approach which means I can switch out any components: for example if I were to attempt to write a new UI I will not need to make any modifications to the helper functions or the existing tests.

## Future
If I had more time I would have loved to write this in Elixir instead.

To improve upon this version, I would like to address the main bottleneck which is the use of the `tabulate` library that formats the output. The program is more than capable of generating 5000 prime numbers and even generating an multiplication table for 5000 prime numbers in a reasonable timeframe but struggles format the output in its current implementation.

I would also prefer to write a better UI, perhaps a static web page with complimentary selenium webdriver tests.

For the purposes of this task and I included some logging and a simple debug flag. This is not neccessary for such a simple task and can easily be removed, however I left it in to offer more insight into how I tackle problems.
