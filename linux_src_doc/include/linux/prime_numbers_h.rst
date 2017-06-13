.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/prime_numbers.h

.. _`for_each_prime_number`:

for_each_prime_number
=====================

.. c:function::  for_each_prime_number( prime,  max)

    iterate over each prime upto a value

    :param  prime:
        the current prime number in this iteration

    :param  max:
        the upper limit

.. _`for_each_prime_number.description`:

Description
-----------

Starting from the first prime number 2 iterate over each prime number up to
the \ ``max``\  value. On each iteration, \ ``prime``\  is set to the current prime number.
\ ``max``\  should be less than ULONG_MAX to ensure termination. To begin with
\ ``prime``\  set to 1 on the first iteration use \ :c:func:`for_each_prime_number_from`\ 
instead.

.. _`for_each_prime_number_from`:

for_each_prime_number_from
==========================

.. c:function::  for_each_prime_number_from( prime,  from,  max)

    iterate over each prime upto a value

    :param  prime:
        the current prime number in this iteration

    :param  from:
        the initial value

    :param  max:
        the upper limit

.. _`for_each_prime_number_from.description`:

Description
-----------

Starting from \ ``from``\  iterate over each successive prime number up to the
\ ``max``\  value. On each iteration, \ ``prime``\  is set to the current prime number.
\ ``max``\  should be less than ULONG_MAX, and \ ``from``\  less than \ ``max``\ , to ensure
termination.

.. This file was automatic generated / don't edit.

