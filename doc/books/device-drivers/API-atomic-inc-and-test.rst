
.. _API-atomic-inc-and-test:

===================
atomic_inc_and_test
===================

*man atomic_inc_and_test(9)*

*4.6.0-rc1*

increment and test


Synopsis
========

.. c:function:: int atomic_inc_and_test( atomic_t * v )

Arguments
=========

``v``
    pointer of type atomic_t


Description
===========

Atomically increments ``v`` by 1 and returns true if the result is zero, or false for all other cases.
