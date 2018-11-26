.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/prime_numbers.c

.. _`next_prime_number`:

next_prime_number
=================

.. c:function:: unsigned long next_prime_number(unsigned long x)

    return the next prime number

    :param x:
        the starting point for searching to test
    :type x: unsigned long

.. _`next_prime_number.description`:

Description
-----------

A prime number is an integer greater than 1 that is only divisible by
itself and 1.  The set of prime numbers is computed using the Sieve of
Eratoshenes (on finding a prime, all multiples of that prime are removed
from the set) enabling a fast lookup of the next prime number larger than
\ ``x``\ . If the sieve fails (memory limitation), the search falls back to using
slow trial-divison, up to the value of ULONG_MAX (which is reported as the
final prime as a sentinel).

.. _`next_prime_number.return`:

Return
------

the next prime number larger than \ ``x``\ 

.. _`is_prime_number`:

is_prime_number
===============

.. c:function:: bool is_prime_number(unsigned long x)

    test whether the given number is prime

    :param x:
        the number to test
    :type x: unsigned long

.. _`is_prime_number.description`:

Description
-----------

A prime number is an integer greater than 1 that is only divisible by
itself and 1. Internally a cache of prime numbers is kept (to speed up
searching for sequential primes, see \ :c:func:`next_prime_number`\ ), but if the number
falls outside of that cache, its primality is tested using trial-divison.

.. _`is_prime_number.return`:

Return
------

true if \ ``x``\  is prime, false for composite numbers.

.. This file was automatic generated / don't edit.

