.. -*- coding: utf-8; mode: rst -*-

.. _API---copy-from-user:

================
__copy_from_user
================

*man __copy_from_user(9)*

*4.6.0-rc5*

Copy a block of data from user space, with less checking.


Synopsis
========

.. c:function:: unsigned long __copy_from_user( void * to, const void __user * from, unsigned long n )

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

Copy data from user space to kernel space. Caller must check the
specified block with ``access_ok`` before calling this function.

Returns number of bytes that could not be copied. On success, this will
be zero.

If some data could not be copied, this function will pad the copied data
to the requested size using zero bytes.

An alternate version - ``__copy_from_user_inatomic`` - may be called
from atomic context and will fail rather than sleep. In this case the
uncopied bytes will *NOT* be padded with zeros. See fs/filemap.h for
explanation of why this is needed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
