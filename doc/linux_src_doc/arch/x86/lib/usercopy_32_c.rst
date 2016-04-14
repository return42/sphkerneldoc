.. -*- coding: utf-8; mode: rst -*-

=============
usercopy_32.c
=============

.. _`clear_user`:

clear_user
==========

.. c:function:: unsigned long clear_user (void __user *to, unsigned long n)

    Zero a block of memory in user space.

    :param void __user \*to:
        Destination address, in user space.

    :param unsigned long n:
        Number of bytes to zero.


.. _`clear_user.description`:

Description
-----------

Zero a block of memory in user space.

Returns number of bytes that could not be cleared.
On success, this will be zero.


.. _`__clear_user`:

__clear_user
============

.. c:function:: unsigned long __clear_user (void __user *to, unsigned long n)

    Zero a block of memory in user space, with less checking.

    :param void __user \*to:
        Destination address, in user space.

    :param unsigned long n:
        Number of bytes to zero.


.. _`__clear_user.description`:

Description
-----------

Zero a block of memory in user space.  Caller must check
the specified block with :c:func:`access_ok` before calling this function.

Returns number of bytes that could not be cleared.
On success, this will be zero.


.. _`_copy_to_user`:

_copy_to_user
=============

.. c:function:: unsigned long _copy_to_user (void __user *to, const void *from, unsigned n)

    Copy a block of data into user space.

    :param void __user \*to:
        Destination address, in user space.

    :param const void \*from:
        Source address, in kernel space.

    :param unsigned n:
        Number of bytes to copy.


.. _`_copy_to_user.description`:

Description
-----------

Context: User context only. This function may sleep if pagefaults are
enabled.

Copy data from kernel space to user space.

Returns number of bytes that could not be copied.
On success, this will be zero.


.. _`_copy_from_user`:

_copy_from_user
===============

.. c:function:: unsigned long _copy_from_user (void *to, const void __user *from, unsigned n)

    Copy a block of data from user space.

    :param void \*to:
        Destination address, in kernel space.

    :param const void __user \*from:
        Source address, in user space.

    :param unsigned n:
        Number of bytes to copy.


.. _`_copy_from_user.description`:

Description
-----------

Context: User context only. This function may sleep if pagefaults are
enabled.

Copy data from user space to kernel space.

Returns number of bytes that could not be copied.
On success, this will be zero.

If some data could not be copied, this function will pad the copied
data to the requested size using zero bytes.

