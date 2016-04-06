
.. _API-atomic-sub:

==========
atomic_sub
==========

*man atomic_sub(9)*

*4.6.0-rc1*

subtract integer from atomic variable


Synopsis
========

.. c:function:: void atomic_sub( int i, atomic_t * v )

Arguments
=========

``i``
    integer value to subtract

``v``
    pointer of type atomic_t


Description
===========

Atomically subtracts ``i`` from ``v``.
