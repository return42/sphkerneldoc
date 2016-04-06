
.. _API-atomic-dec-and-test:

===================
atomic_dec_and_test
===================

*man atomic_dec_and_test(9)*

*4.6.0-rc1*

decrement and test


Synopsis
========

.. c:function:: int atomic_dec_and_test( atomic_t * v )

Arguments
=========

``v``
    pointer of type atomic_t


Description
===========

Atomically decrements ``v`` by 1 and returns true if the result is 0, or false for all other cases.
