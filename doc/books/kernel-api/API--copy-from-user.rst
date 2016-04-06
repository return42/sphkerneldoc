
.. _API--copy-from-user:

===============
_copy_from_user
===============

*man _copy_from_user(9)*

*4.6.0-rc1*

Copy a block of data from user space.


Synopsis
========

.. c:function:: unsigned long _copy_from_user( void * to, const void __user * from, unsigned n )

Arguments
=========

``to``
    Destination address, in kernel space.

``from``
    Source address, in user space.

``n``
    Number of bytes to copy.


Context
=======

User context only. This function may sleep if pagefaults are enabled.


Description
===========

Copy data from user space to kernel space.

Returns number of bytes that could not be copied. On success, this will be zero.

If some data could not be copied, this function will pad the copied data to the requested size using zero bytes.
