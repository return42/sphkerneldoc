.. -*- coding: utf-8; mode: rst -*-

============
uaccess_32.h
============



.. _xref___copy_to_user_inatomic:

__copy_to_user_inatomic
=======================

.. c:function:: unsigned long __copy_to_user_inatomic (void __user * to, const void * from, unsigned long n)

    Copy a block of data into user space, with less checking.

    :param void __user * to:
        Destination address, in user space.

    :param const void * from:
        Source address, in kernel space.

    :param unsigned long n:
        Number of bytes to copy.



Context
-------

User context only.



Description
-----------

Copy data from kernel space to user space.  Caller must check
the specified block with :c:func:`access_ok` before calling this function.
The caller should also make sure he pins the user space address
so that we don't result in page fault and sleep.


Here we special-case 1, 2 and 4-byte copy_*_user invocations.  On a fault
we return the initial request size (1, 2 or 4), as copy_*_user should do.
If a store crosses a page boundary and gets a fault, the x86 will not write
anything, so this is accurate.




.. _xref___copy_to_user:

__copy_to_user
==============

.. c:function:: unsigned long __copy_to_user (void __user * to, const void * from, unsigned long n)

    Copy a block of data into user space, with less checking.

    :param void __user * to:
        Destination address, in user space.

    :param const void * from:
        Source address, in kernel space.

    :param unsigned long n:
        Number of bytes to copy.



Context
-------

User context only. This function may sleep if pagefaults are
         enabled.



Description
-----------

Copy data from kernel space to user space.  Caller must check
the specified block with :c:func:`access_ok` before calling this function.


Returns number of bytes that could not be copied.
On success, this will be zero.




.. _xref___copy_from_user:

__copy_from_user
================

.. c:function:: unsigned long __copy_from_user (void * to, const void __user * from, unsigned long n)

    Copy a block of data from user space, with less checking.

    :param void * to:
        Destination address, in kernel space.

    :param const void __user * from:
        Source address, in user space.

    :param unsigned long n:
        Number of bytes to copy.



Context
-------

User context only. This function may sleep if pagefaults are
         enabled.



Description
-----------

Copy data from user space to kernel space.  Caller must check
the specified block with :c:func:`access_ok` before calling this function.


Returns number of bytes that could not be copied.
On success, this will be zero.


If some data could not be copied, this function will pad the copied
data to the requested size using zero bytes.


An alternate version - :c:func:`__copy_from_user_inatomic` - may be called from
atomic context and will fail rather than sleep.  In this case the
uncopied bytes will *NOT* be padded with zeros.  See fs/filemap.h
for explanation of why this is needed.


