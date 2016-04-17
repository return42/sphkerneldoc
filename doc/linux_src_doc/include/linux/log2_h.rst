.. -*- coding: utf-8; mode: rst -*-

======
log2.h
======


.. _`ilog2`:

ilog2
=====

.. c:function:: ilog2 ( n)

    log of base 2 of 32-bit or a 64-bit unsigned value @n - parameter

    :param n:

        *undescribed*



.. _`ilog2.description`:

Description
-----------


constant-capable log of base 2 calculation
- this can be used to initialise global variables from constant data, hence

  the massive ternary operator construction

selects the appropriately-sized optimised version depending on sizeof(n)



.. _`roundup_pow_of_two`:

roundup_pow_of_two
==================

.. c:function:: roundup_pow_of_two ( n)

    round the given value up to nearest power of two @n - parameter

    :param n:

        *undescribed*



.. _`roundup_pow_of_two.description`:

Description
-----------


round the given value up to the nearest power of two
- the result is undefined when n == 0
- this can be used to initialise global variables from constant data



.. _`rounddown_pow_of_two`:

rounddown_pow_of_two
====================

.. c:function:: rounddown_pow_of_two ( n)

    round the given value down to nearest power of two @n - parameter

    :param n:

        *undescribed*



.. _`rounddown_pow_of_two.description`:

Description
-----------


round the given value down to the nearest power of two
- the result is undefined when n == 0
- this can be used to initialise global variables from constant data



.. _`order_base_2`:

order_base_2
============

.. c:function:: order_base_2 ( n)

    calculate the (rounded up) base 2 order of the argument

    :param n:
        parameter



.. _`order_base_2.the-first-few-values-calculated-by-this-routine`:

The first few values calculated by this routine
-----------------------------------------------

ob2(0) = 0
ob2(1) = 0
ob2(2) = 1
ob2(3) = 2
ob2(4) = 2
ob2(5) = 3
... and so on.

