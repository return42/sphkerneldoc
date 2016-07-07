.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/tile/include/asm/uaccess.h

.. _`access_ok`:

access_ok
=========

.. c:function::  access_ok( type,  addr,  size)

    - Checks if a user space pointer is valid

    :param  type:
        Type of access: \ ``VERIFY_READ``\  or \ ``VERIFY_WRITE``\ .  Note that
        \ ``VERIFY_WRITE``\  is a superset of \ ``VERIFY_READ``\  - if it is safe
        to write to a block, it is always safe to read from it.

    :param  addr:
        User space pointer to start of block to check

    :param  size:
        Size of block to check

.. _`access_ok.context`:

Context
-------

User context only. This function may sleep if pagefaults are
enabled.

.. _`access_ok.description`:

Description
-----------

Checks if a pointer to a block of memory in user space is valid.

Returns true (nonzero) if the memory block may be valid, false (zero)
if it is definitely invalid.

Note that, depending on architecture, this function probably just
checks that the pointer is in the user space range - after calling
this function, memory access functions may still return -EFAULT.

.. _`__get_user`:

__get_user
==========

.. c:function::  __get_user( x,  ptr)

    - Get a simple variable from user space, with less checking.

    :param  x:
        Variable to store result.

    :param  ptr:
        Source address, in user space.

.. _`__get_user.context`:

Context
-------

User context only. This function may sleep if pagefaults are
enabled.

.. _`__get_user.description`:

Description
-----------

This macro copies a single simple variable from user space to kernel
space.  It supports simple types like char and int, but not larger
data types like structures or arrays.

\ ``ptr``\  must have pointer-to-simple-variable type, and the result of
dereferencing \ ``ptr``\  must be assignable to \ ``x``\  without a cast.

Returns zero on success, or -EFAULT on error.
On error, the variable \ ``x``\  is set to zero.

Caller must check the pointer with \ :c:func:`access_ok`\  before calling this
function.

.. _`__put_user`:

__put_user
==========

.. c:function::  __put_user( x,  ptr)

    - Write a simple value into user space, with less checking.

    :param  x:
        Value to copy to user space.

    :param  ptr:
        Destination address, in user space.

.. _`__put_user.context`:

Context
-------

User context only. This function may sleep if pagefaults are
enabled.

.. _`__put_user.description`:

Description
-----------

This macro copies a single simple value from kernel space to user
space.  It supports simple types like char and int, but not larger
data types like structures or arrays.

\ ``ptr``\  must have pointer-to-simple-variable type, and \ ``x``\  must be assignable
to the result of dereferencing \ ``ptr``\ .

Caller must check the pointer with \ :c:func:`access_ok`\  before calling this
function.

Returns zero on success, or -EFAULT on error.

.. _`__copy_to_user_inatomic`:

__copy_to_user_inatomic
=======================

.. c:function:: unsigned long __copy_to_user_inatomic(void __user *to, const void *from, unsigned long n)

    copy data into user space, with less checking.

    :param void __user \*to:
        Destination address, in user space.

    :param const void \*from:
        Source address, in kernel space.

    :param unsigned long n:
        Number of bytes to copy.

.. _`__copy_to_user_inatomic.context`:

Context
-------

User context only. This function may sleep if pagefaults are
enabled.

.. _`__copy_to_user_inatomic.description`:

Description
-----------

Copy data from kernel space to user space.  Caller must check
the specified block with \ :c:func:`access_ok`\  before calling this function.

Returns number of bytes that could not be copied.
On success, this will be zero.

An alternate version - \\ :c:func:`__copy_to_user_inatomic`\  - is designed
to be called from atomic context, typically bracketed by calls
to \ :c:func:`pagefault_disable`\  and \ :c:func:`pagefault_enable`\ .

.. _`__copy_from_user_inatomic`:

__copy_from_user_inatomic
=========================

.. c:function:: unsigned long __copy_from_user_inatomic(void *to, const void __user *from, unsigned long n)

    copy data from user space, with less checking.

    :param void \*to:
        Destination address, in kernel space.

    :param const void __user \*from:
        Source address, in user space.

    :param unsigned long n:
        Number of bytes to copy.

.. _`__copy_from_user_inatomic.context`:

Context
-------

User context only. This function may sleep if pagefaults are
enabled.

.. _`__copy_from_user_inatomic.description`:

Description
-----------

Copy data from user space to kernel space.  Caller must check
the specified block with \ :c:func:`access_ok`\  before calling this function.

Returns number of bytes that could not be copied.
On success, this will be zero.

If some data could not be copied, this function will pad the copied
data to the requested size using zero bytes.

An alternate version - \\ :c:func:`__copy_from_user_inatomic`\  - is designed
to be called from atomic context, typically bracketed by calls
to \ :c:func:`pagefault_disable`\  and \ :c:func:`pagefault_enable`\ .  This version
does \*NOT\* pad with zeros.

.. _`__copy_in_user_inatomic`:

__copy_in_user_inatomic
=======================

.. c:function:: unsigned long __copy_in_user_inatomic(void __user *to, const void __user *from, unsigned long n)

    copy data within user space, with less checking.

    :param void __user \*to:
        Destination address, in user space.

    :param const void __user \*from:
        Source address, in user space.

    :param unsigned long n:
        Number of bytes to copy.

.. _`__copy_in_user_inatomic.context`:

Context
-------

User context only. This function may sleep if pagefaults are
enabled.

.. _`__copy_in_user_inatomic.description`:

Description
-----------

Copy data from user space to user space.  Caller must check
the specified blocks with \ :c:func:`access_ok`\  before calling this function.

Returns number of bytes that could not be copied.
On success, this will be zero.

.. _`clear_user_asm`:

clear_user_asm
==============

.. c:function:: unsigned long clear_user_asm(void __user *mem, unsigned long len)

    - Zero a block of memory in user space.

    :param void __user \*mem:
        Destination address, in user space.

    :param unsigned long len:
        Number of bytes to zero.

.. _`clear_user_asm.description`:

Description
-----------

Zero a block of memory in user space.

Returns number of bytes that could not be cleared.
On success, this will be zero.

.. _`flush_user_asm`:

flush_user_asm
==============

.. c:function:: unsigned long flush_user_asm(void __user *mem, unsigned long len)

    - Flush a block of memory in user space from cache.

    :param void __user \*mem:
        Destination address, in user space.

    :param unsigned long len:
        Number of bytes to flush.

.. _`flush_user_asm.description`:

Description
-----------

Returns number of bytes that could not be flushed.
On success, this will be zero.

.. _`finv_user_asm`:

finv_user_asm
=============

.. c:function:: unsigned long finv_user_asm(void __user *mem, unsigned long len)

    - Flush-inval a block of memory in user space from cache.

    :param void __user \*mem:
        Destination address, in user space.

    :param unsigned long len:
        Number of bytes to invalidate.

.. _`finv_user_asm.description`:

Description
-----------

Returns number of bytes that could not be flush-invalidated.
On success, this will be zero.

.. This file was automatic generated / don't edit.

