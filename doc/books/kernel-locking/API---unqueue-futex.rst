
.. _API---unqueue-futex:

===============
__unqueue_futex
===============

*man __unqueue_futex(9)*

*4.6.0-rc1*

Remove the futex_q from its futex_hash_bucket


Synopsis
========

.. c:function:: void __unqueue_futex( struct futex_q * q )

Arguments
=========

``q``
    The futex_q to unqueue


Description
===========

The q->lock_ptr must not be NULL and must be held by the caller.
