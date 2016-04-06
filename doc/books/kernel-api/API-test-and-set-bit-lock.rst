
.. _API-test-and-set-bit-lock:

=====================
test_and_set_bit_lock
=====================

*man test_and_set_bit_lock(9)*

*4.6.0-rc1*

Set a bit and return its old value for lock


Synopsis
========

.. c:function:: int test_and_set_bit_lock( long nr, volatile unsigned long * addr )

Arguments
=========

``nr``
    Bit to set

``addr``
    Address to count from


Description
===========

This is the same as test_and_set_bit on x86.
