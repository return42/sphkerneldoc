
.. _API-wake-up-atomic-t:

================
wake_up_atomic_t
================

*man wake_up_atomic_t(9)*

*4.6.0-rc1*

Wake up a waiter on a atomic_t


Synopsis
========

.. c:function:: void wake_up_atomic_t( atomic_t * p )

Arguments
=========

``p``
    The atomic_t being waited on, a kernel virtual address


Description
===========

Wake up anyone waiting for the atomic_t to go to zero.

Abuse the bit-waker function and its waitqueue hash table set (the atomic_t check is done by the waiter's wake function, not the by the waker itself).
