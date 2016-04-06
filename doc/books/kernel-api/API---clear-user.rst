
.. _API---clear-user:

============
__clear_user
============

*man __clear_user(9)*

*4.6.0-rc1*

Zero a block of memory in user space, with less checking.


Synopsis
========

.. c:function:: unsigned long __clear_user( void __user * to, unsigned long n )

Arguments
=========

``to``
    Destination address, in user space.

``n``
    Number of bytes to zero.


Description
===========

Zero a block of memory in user space. Caller must check the specified block with ``access_ok`` before calling this function.

Returns number of bytes that could not be cleared. On success, this will be zero.
