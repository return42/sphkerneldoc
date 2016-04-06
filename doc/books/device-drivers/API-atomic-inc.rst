
.. _API-atomic-inc:

==========
atomic_inc
==========

*man atomic_inc(9)*

*4.6.0-rc1*

increment atomic variable


Synopsis
========

.. c:function:: void atomic_inc( atomic_t * v )

Arguments
=========

``v``
    pointer of type atomic_t


Description
===========

Atomically increments ``v`` by 1.
