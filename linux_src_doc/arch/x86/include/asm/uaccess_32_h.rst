.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/asm/uaccess_32.h

.. _`__copy_to_user_inatomic`:

__copy_to_user_inatomic
=======================

.. c:function:: unsigned long __copy_to_user_inatomic(void __user *to, const void *from, unsigned long n)

    - Copy a block of data into user space, with less checking.

    :param void __user \*to:
        Destination address, in user space.

    :param const void \*from:
        Source address, in kernel space.

    :param unsigned long n:
        Number of bytes to copy.

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

.. _`__copy_to_user`:

__copy_to_user
==============

.. c:function:: unsigned long __copy_to_user(void __user *to, const void *from, unsigned long n)

    - Copy a block of data into user space, with less checking.

    :param void __user \*to:
        Destination address, in user space.

    :param const void \*from:
        Source address, in kernel space.

    :param unsigned long n:
        Number of bytes to copy.

.. _`__copy_to_user.context`:

Context
-------

User context only. This function may sleep if pagefaults are
enabled.

.. _`__copy_to_user.description`:

Description
-----------

Copy data from kernel space to user space.  Caller must check
the specified block with \ :c:func:`access_ok`\  before calling this function.

Returns number of bytes that could not be copied.
On success, this will be zero.

.. _`__copy_from_user`:

__copy_from_user
================

.. c:function:: unsigned long __copy_from_user(void *to, const void __user *from, unsigned long n)

    - Copy a block of data from user space, with less checking.

    :param void \*to:
        Destination address, in kernel space.

    :param const void __user \*from:
        Source address, in user space.

    :param unsigned long n:
        Number of bytes to copy.

.. _`__copy_from_user.context`:

Context
-------

User context only. This function may sleep if pagefaults are
enabled.

.. _`__copy_from_user.description`:

Description
-----------

Copy data from user space to kernel space.  Caller must check
the specified block with \ :c:func:`access_ok`\  before calling this function.

Returns number of bytes that could not be copied.
On success, this will be zero.

If some data could not be copied, this function will pad the copied
data to the requested size using zero bytes.

An alternate version - \__copy_from_user_inatomic() - may be called from
atomic context and will fail rather than sleep.  In this case the
uncopied bytes will \*NOT\* be padded with zeros.  See fs/filemap.h
for explanation of why this is needed.

.. This file was automatic generated / don't edit.

