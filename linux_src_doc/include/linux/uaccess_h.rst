.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/uaccess.h

.. _`__copy_to_user_inatomic`:

\__copy_to_user_inatomic
========================

.. c:function:: unsigned long __copy_to_user_inatomic(void __user *to, const void *from, unsigned long n)

    - Copy a block of data into user space, with less checking.

    :param to:
        Destination address, in user space.
    :type to: void __user \*

    :param from:
        Source address, in kernel space.
    :type from: const void \*

    :param n:
        Number of bytes to copy.
    :type n: unsigned long

.. _`__copy_to_user_inatomic.context`:

Context
-------

User context only.

.. _`__copy_to_user_inatomic.description`:

Description
-----------

Copy data from kernel space to user space.  Caller must check
the specified block with \ :c:func:`access_ok`\  before calling this function.
The caller should also make sure he pins the user space address
so that we don't result in page fault and sleep.

.. _`probe_kernel_address`:

probe_kernel_address
====================

.. c:function::  probe_kernel_address( addr,  retval)

    safely attempt to read from a location

    :param addr:
        address to read from
    :type addr: 

    :param retval:
        read into this variable
    :type retval: 

.. _`probe_kernel_address.description`:

Description
-----------

Returns 0 on success, or -EFAULT.

.. This file was automatic generated / don't edit.

