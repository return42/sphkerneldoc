.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/int_sqrt.c

.. _`int_sqrt`:

int_sqrt
========

.. c:function:: unsigned long int_sqrt(unsigned long x)

    computes the integer square root

    :param x:
        integer of which to calculate the sqrt
    :type x: unsigned long

.. _`int_sqrt.computes`:

Computes
--------

floor(sqrt(x))

.. _`int_sqrt64`:

int_sqrt64
==========

.. c:function:: u32 int_sqrt64(u64 x)

    strongly typed int_sqrt function when minimum 64 bit input is expected.

    :param x:
        64bit integer of which to calculate the sqrt
    :type x: u64

.. This file was automatic generated / don't edit.

