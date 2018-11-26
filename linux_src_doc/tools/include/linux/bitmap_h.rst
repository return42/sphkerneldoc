.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/include/linux/bitmap.h

.. _`test_and_set_bit`:

test_and_set_bit
================

.. c:function:: int test_and_set_bit(int nr, unsigned long *addr)

    Set a bit and return its old value

    :param nr:
        Bit to set
    :type nr: int

    :param addr:
        Address to count from
    :type addr: unsigned long \*

.. _`test_and_clear_bit`:

test_and_clear_bit
==================

.. c:function:: int test_and_clear_bit(int nr, unsigned long *addr)

    Clear a bit and return its old value

    :param nr:
        Bit to clear
    :type nr: int

    :param addr:
        Address to count from
    :type addr: unsigned long \*

.. _`bitmap_alloc`:

bitmap_alloc
============

.. c:function:: unsigned long *bitmap_alloc(int nbits)

    Allocate bitmap

    :param nbits:
        Number of bits
    :type nbits: int

.. _`bitmap_and`:

bitmap_and
==========

.. c:function:: int bitmap_and(unsigned long *dst, const unsigned long *src1, const unsigned long *src2, unsigned int nbits)

    Do logical and on bitmaps

    :param dst:
        resulting bitmap
    :type dst: unsigned long \*

    :param src1:
        operand 1
    :type src1: const unsigned long \*

    :param src2:
        operand 2
    :type src2: const unsigned long \*

    :param nbits:
        size of bitmap
    :type nbits: unsigned int

.. This file was automatic generated / don't edit.

