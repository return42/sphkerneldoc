.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/asm-generic/getorder.h

.. _`get_order`:

get_order
=========

.. c:function::  get_order( n)

    Determine the allocation order of a memory size

    :param  n:
        *undescribed*

.. _`get_order.description`:

Description
-----------

Determine the allocation order of a particular sized block of memory.  This
is on a logarithmic scale, where:

0 -> 2^0 \* PAGE_SIZE and below
1 -> 2^1 \* PAGE_SIZE to 2^0 \* PAGE_SIZE + 1
2 -> 2^2 \* PAGE_SIZE to 2^1 \* PAGE_SIZE + 1
3 -> 2^3 \* PAGE_SIZE to 2^2 \* PAGE_SIZE + 1
4 -> 2^4 \* PAGE_SIZE to 2^3 \* PAGE_SIZE + 1
...

The order returned is used to find the smallest allocation granule required
to hold an object of the specified size.

The result is undefined if the size is 0.

This function may be used to initialise variables with compile time
evaluations of constants.

.. This file was automatic generated / don't edit.

