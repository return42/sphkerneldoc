
.. _API-test-and-change-bit:

===================
test_and_change_bit
===================

*man test_and_change_bit(9)*

*4.6.0-rc1*

Change a bit and return its old value


Synopsis
========

.. c:function:: int test_and_change_bit( long nr, volatile unsigned long * addr )

Arguments
=========

``nr``
    Bit to change

``addr``
    Address to count from


Description
===========

This operation is atomic and cannot be reordered. It also implies a memory barrier.
