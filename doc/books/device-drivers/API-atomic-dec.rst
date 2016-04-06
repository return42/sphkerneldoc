
.. _API-atomic-dec:

==========
atomic_dec
==========

*man atomic_dec(9)*

*4.6.0-rc1*

decrement atomic variable


Synopsis
========

.. c:function:: void atomic_dec( atomic_t * v )

Arguments
=========

``v``
    pointer of type atomic_t


Description
===========

Atomically decrements ``v`` by 1.
