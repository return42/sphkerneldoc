.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/lib/usercopy_32.c

.. _`clear_user`:

clear_user
==========

.. c:function:: unsigned long clear_user(void __user *to, unsigned long n)

    - Zero a block of memory in user space.

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

.. c:function:: unsigned long __clear_user(void __user *to, unsigned long n)

    - Zero a block of memory in user space, with less checking.

    :param void __user \*to:
        Destination address, in user space.

    :param unsigned long n:
        Number of bytes to zero.

.. _`__clear_user.description`:

Description
-----------

Zero a block of memory in user space.  Caller must check
the specified block with \ :c:func:`access_ok`\  before calling this function.

Returns number of bytes that could not be cleared.
On success, this will be zero.

.. This file was automatic generated / don't edit.

