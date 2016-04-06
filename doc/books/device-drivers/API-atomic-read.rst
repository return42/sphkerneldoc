
.. _API-atomic-read:

===========
atomic_read
===========

*man atomic_read(9)*

*4.6.0-rc1*

read atomic variable


Synopsis
========

.. c:function:: int atomic_read( const atomic_t * v )

Arguments
=========

``v``
    pointer of type atomic_t


Description
===========

Atomically reads the value of ``v``.
