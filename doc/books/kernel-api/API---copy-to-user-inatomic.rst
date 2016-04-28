.. -*- coding: utf-8; mode: rst -*-

.. _API---copy-to-user-inatomic:

=======================
__copy_to_user_inatomic
=======================

*man __copy_to_user_inatomic(9)*

*4.6.0-rc5*

Copy a block of data into user space, with less checking.


Synopsis
========

.. c:function:: unsigned long __copy_to_user_inatomic( void __user * to, const void * from, unsigned long n )

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

User context only.


Description
===========

Copy data from kernel space to user space. Caller must check the
specified block with ``access_ok`` before calling this function. The
caller should also make sure he pins the user space address so that we
don't result in page fault and sleep.

Here we special-case 1, 2 and 4-byte copy_*_user invocations. On a
fault we return the initial request size (1, 2 or 4), as copy_*_user
should do. If a store crosses a page boundary and gets a fault, the x86
will not write anything, so this is accurate.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
