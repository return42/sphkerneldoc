.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/time.h

.. _`time_after32`:

time_after32
============

.. c:function::  time_after32( a,  b)

    compare two 32-bit relative times

    :param  a:
        the time which may be after \ ``b``\ 

    :param  b:
        the time which may be before \ ``a``\ 

.. _`time_after32.description`:

Description
-----------

time_after32(a, b) returns true if the time \ ``a``\  is after time \ ``b``\ .
time_before32(b, a) returns true if the time \ ``b``\  is before time \ ``a``\ .

Similar to \ :c:func:`time_after`\ , compare two 32-bit timestamps for relative
times.  This is useful for comparing 32-bit seconds values that can't
be converted to 64-bit values (e.g. due to disk format or wire protocol
issues) when it is known that the times are less than 68 years apart.

.. This file was automatic generated / don't edit.

