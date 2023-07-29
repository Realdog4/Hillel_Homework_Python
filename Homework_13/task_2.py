"""
Define a function that takes an integer argument and returns a logical value true or false depending on if the integer
is a prime.

Per Wikipedia, a prime number ( or a prime ) is a natural number greater than 1 that has no positive divisors other than
1 and itself.

Requirements
You can assume you will be given an integer input.
You can not assume that the integer will be only positive. You may be given negative numbers as well ( or 0 ).
NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out.
Numbers go up to 2^31 ( or similar, depending on language ). Looping all the way up to n, or n/2, will be too slow.
"""

import math


def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    # Loop up to the square root of the number (rounded up)
    max_divisor = math.isqrt(num) + 1

    for divisor in range(3, max_divisor, 2):
        if num % divisor == 0:
            return False

    return True


print(is_prime(1))
print(is_prime(2))
print(is_prime(-1))
print(is_prime(29))
print(is_prime(100))