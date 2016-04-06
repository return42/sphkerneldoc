
.. _API-atomic-add:

==========
atomic_add
==========

*man atomic_add(9)*

*4.6.0-rc1*

add integer to atomic variable


Synopsis
========

.. c:function:: void atomic_add( int i, atomic_t * v )

Arguments
=========

``i``
    integer value to add

``v``
    pointer of type atomic_t


Description
===========

Atomically adds ``i`` to ``v``.
