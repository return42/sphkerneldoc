.. -*- coding: utf-8; mode: rst -*-

=======
div64.c
=======


.. _`div64_u64_rem`:

div64_u64_rem
=============

.. c:function:: u64 div64_u64_rem (u64 dividend, u64 divisor, u64 *remainder)

    unsigned 64bit divide with 64bit divisor and remainder

    :param u64 dividend:
        64bit dividend

    :param u64 divisor:
        64bit divisor

    :param u64 \*remainder:
        64bit remainder



.. _`div64_u64_rem.description`:

Description
-----------

This implementation is a comparable to algorithm used by div64_u64.
But this operation, which includes math for calculating the remainder,
is kept distinct to avoid slowing down the div64_u64 operation on 32bit
systems.



.. _`div64_u64`:

div64_u64
=========

.. c:function:: u64 div64_u64 (u64 dividend, u64 divisor)

    unsigned 64bit divide with 64bit divisor

    :param u64 dividend:
        64bit dividend

    :param u64 divisor:
        64bit divisor



.. _`div64_u64.description`:

Description
-----------

This implementation is a modified version of the algorithm proposed
by the book 'Hacker's Delight'.  The original source and full proof
can be found here and is available for use without restriction.

'http://www.hackersdelight.org/hdcodetxt/divDouble.c.txt'



.. _`div64_s64`:

div64_s64
=========

.. c:function:: s64 div64_s64 (s64 dividend, s64 divisor)

    signed 64bit divide with 64bit divisor

    :param s64 dividend:
        64bit dividend

    :param s64 divisor:
        64bit divisor

