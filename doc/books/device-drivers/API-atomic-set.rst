
.. _API-atomic-set:

==========
atomic_set
==========

*man atomic_set(9)*

*4.6.0-rc1*

set atomic variable


Synopsis
========

.. c:function:: void atomic_set( atomic_t * v, int i )

Arguments
=========

``v``
    pointer of type atomic_t

``i``
    required value


Description
===========

Atomically sets the value of ``v`` to ``i``.
