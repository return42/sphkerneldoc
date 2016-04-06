
.. _API-test-and-clear-bit:

==================
test_and_clear_bit
==================

*man test_and_clear_bit(9)*

*4.6.0-rc1*

Clear a bit and return its old value


Synopsis
========

.. c:function:: int test_and_clear_bit( long nr, volatile unsigned long * addr )

Arguments
=========

``nr``
    Bit to clear

``addr``
    Address to count from


Description
===========

This operation is atomic and cannot be reordered. It also implies a memory barrier.
