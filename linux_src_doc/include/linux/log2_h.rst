.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/log2.h

.. _`is_power_of_2`:

is_power_of_2
=============

.. c:function:: bool is_power_of_2(unsigned long n)

    check if a value is a power of two

    :param n:
        the value to check
    :type n: unsigned long

.. _`is_power_of_2.description`:

Description
-----------

Determine whether some value is a power of two, where zero is
*not* considered a power of two.

.. _`is_power_of_2.return`:

Return
------

true if \ ``n``\  is a power of 2, otherwise false.

.. _`__roundup_pow_of_two`:

__roundup_pow_of_two
====================

.. c:function:: unsigned long __roundup_pow_of_two(unsigned long n)

    round up to nearest power of two

    :param n:
        value to round up
    :type n: unsigned long

.. _`__rounddown_pow_of_two`:

__rounddown_pow_of_two
======================

.. c:function:: unsigned long __rounddown_pow_of_two(unsigned long n)

    round down to nearest power of two

    :param n:
        value to round down
    :type n: unsigned long

.. _`const_ilog2`:

const_ilog2
===========

.. c:function::  const_ilog2( n)

    log base 2 of 32-bit or a 64-bit constant unsigned value

    :param n:
        parameter
    :type n: 

.. _`const_ilog2.description`:

Description
-----------

Use this where sparse expects a true constant expression, e.g. for array
indices.

.. _`ilog2`:

ilog2
=====

.. c:function::  ilog2( n)

    log base 2 of 32-bit or a 64-bit unsigned value

    :param n:
        parameter
    :type n: 

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

.. c:function::  roundup_pow_of_two( n)

    round the given value up to nearest power of two

    :param n:
        parameter
    :type n: 

.. _`roundup_pow_of_two.description`:

Description
-----------

round the given value up to the nearest power of two
- the result is undefined when n == 0
- this can be used to initialise global variables from constant data

.. _`rounddown_pow_of_two`:

rounddown_pow_of_two
====================

.. c:function::  rounddown_pow_of_two( n)

    round the given value down to nearest power of two

    :param n:
        parameter
    :type n: 

.. _`rounddown_pow_of_two.description`:

Description
-----------

round the given value down to the nearest power of two
- the result is undefined when n == 0
- this can be used to initialise global variables from constant data

.. _`order_base_2`:

order_base_2
============

.. c:function::  order_base_2( n)

    calculate the (rounded up) base 2 order of the argument

    :param n:
        parameter
    :type n: 

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

.. This file was automatic generated / don't edit.

