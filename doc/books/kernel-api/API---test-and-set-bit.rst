
.. _API---test-and-set-bit:

==================
__test_and_set_bit
==================

*man __test_and_set_bit(9)*

*4.6.0-rc1*

Set a bit and return its old value


Synopsis
========

.. c:function:: int __test_and_set_bit( long nr, volatile unsigned long * addr )

Arguments
=========

``nr``
    Bit to set

``addr``
    Address to count from


Description
===========

This operation is non-atomic and can be reordered. If two examples of this operation race, one can appear to succeed but actually fail. You must protect multiple accesses with a
lock.
