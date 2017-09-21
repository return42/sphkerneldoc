.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/s390/include/asm/timex.h

.. _`get_tod_clock_monotonic`:

get_tod_clock_monotonic
=======================

.. c:function:: unsigned long long get_tod_clock_monotonic( void)

    returns current time in clock rate units

    :param  void:
        no arguments

.. _`get_tod_clock_monotonic.description`:

Description
-----------

The caller must ensure that preemption is disabled.
The clock and tod_clock_base get changed via stop_machine.
Therefore preemption must be disabled when calling this
function, otherwise the returned value is not guaranteed to
be monotonic.

.. _`tod_to_ns`:

tod_to_ns
=========

.. c:function:: unsigned long long tod_to_ns(unsigned long long todval)

    convert a TOD format value to nanoseconds

    :param unsigned long long todval:
        to be converted TOD format value

.. _`tod_to_ns.return`:

Return
------

number of nanoseconds that correspond to the TOD format value

Converting a 64 Bit TOD format value to nanoseconds means that the value
must be divided by 4.096. In order to achieve that we multiply with 125

.. _`tod_to_ns.and-divide-by-512`:

and divide by 512
-----------------


ns = (todval \* 125) >> 9;

In order to avoid an overflow with the multiplication we can rewrite this.
With a split todval == 2^9 \* th + tl (th upper 55 bits, tl lower 9 bits)
we end up with

ns = ((2^9 \* th + tl) \* 125 ) >> 9;
-> ns = (th \* 125) + ((tl \* 125) >> 9);

.. _`tod_after`:

tod_after
=========

.. c:function:: int tod_after(unsigned long long a, unsigned long long b)

    compare two 64 bit TOD values

    :param unsigned long long a:
        first 64 bit TOD timestamp

    :param unsigned long long b:
        second 64 bit TOD timestamp

.. _`tod_after.return`:

Return
------

true if a is later than b

.. _`tod_after_eq`:

tod_after_eq
============

.. c:function:: int tod_after_eq(unsigned long long a, unsigned long long b)

    compare two 64 bit TOD values

    :param unsigned long long a:
        first 64 bit TOD timestamp

    :param unsigned long long b:
        second 64 bit TOD timestamp

.. _`tod_after_eq.return`:

Return
------

true if a is later than b

.. This file was automatic generated / don't edit.

