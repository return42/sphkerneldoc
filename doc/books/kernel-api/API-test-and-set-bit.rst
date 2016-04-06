
.. _API-test-and-set-bit:

================
test_and_set_bit
================

*man test_and_set_bit(9)*

*4.6.0-rc1*

Set a bit and return its old value


Synopsis
========

.. c:function:: int test_and_set_bit( long nr, volatile unsigned long * addr )

Arguments
=========

``nr``
    Bit to set

``addr``
    Address to count from


Description
===========

This operation is atomic and cannot be reordered. It also implies a memory barrier.
