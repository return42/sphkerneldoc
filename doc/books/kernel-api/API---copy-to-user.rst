
.. _API---copy-to-user:

==============
__copy_to_user
==============

*man __copy_to_user(9)*

*4.6.0-rc1*

Copy a block of data into user space, with less checking.


Synopsis
========

.. c:function:: unsigned long __copy_to_user( void __user * to, const void * from, unsigned long n )

Arguments
=========

``to``
    Destination address, in user space.

``from``
    Source address, in kernel space.

``n``
    Number of bytes to copy.


Context
=======

User context only. This function may sleep if pagefaults are enabled.


Description
===========

Copy data from kernel space to user space. Caller must check the specified block with ``access_ok`` before calling this function.

Returns number of bytes that could not be copied. On success, this will be zero.
