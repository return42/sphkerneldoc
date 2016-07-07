.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/m32r/include/asm/uaccess.h

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

.. _`get_user`:

get_user
========

.. c:function::  get_user( x,  ptr)

    - Get a simple variable from user space.

    :param  x:
        Variable to store result.

    :param  ptr:
        Source address, in user space.

.. _`get_user.context`:

Context
-------

User context only. This function may sleep if pagefaults are
enabled.

.. _`get_user.description`:

Description
-----------

This macro copies a single simple variable from user space to kernel
space.  It supports simple types like char and int, but not larger
data types like structures or arrays.

\ ``ptr``\  must have pointer-to-simple-variable type, and the result of
dereferencing \ ``ptr``\  must be assignable to \ ``x``\  without a cast.

Returns zero on success, or -EFAULT on error.
On error, the variable \ ``x``\  is set to zero.

.. _`put_user`:

put_user
========

.. c:function::  put_user( x,  ptr)

    - Write a simple value into user space.

    :param  x:
        Value to copy to user space.

    :param  ptr:
        Destination address, in user space.

.. _`put_user.context`:

Context
-------

User context only. This function may sleep if pagefaults are
enabled.

.. _`put_user.description`:

Description
-----------

This macro copies a single simple value from kernel space to user
space.  It supports simple types like char and int, but not larger
data types like structures or arrays.

\ ``ptr``\  must have pointer-to-simple-variable type, and \ ``x``\  must be assignable
to the result of dereferencing \ ``ptr``\ .

Returns zero on success, or -EFAULT on error.

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

Caller must check the pointer with \ :c:func:`access_ok`\  before calling this
function.

Returns zero on success, or -EFAULT on error.
On error, the variable \ ``x``\  is set to zero.

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

.. _`__copy_to_user`:

__copy_to_user
==============

.. c:function::  __copy_to_user( to,  from,  n)

    - Copy a block of data into user space, with less checking.

    :param  to:
        Destination address, in user space.

    :param  from:
        Source address, in kernel space.

    :param  n:
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

.. _`copy_to_user`:

copy_to_user
============

.. c:function::  copy_to_user( to,  from,  n)

    - Copy a block of data into user space.

    :param  to:
        Destination address, in user space.

    :param  from:
        Source address, in kernel space.

    :param  n:
        Number of bytes to copy.

.. _`copy_to_user.context`:

Context
-------

User context only. This function may sleep if pagefaults are
enabled.

.. _`copy_to_user.description`:

Description
-----------

Copy data from kernel space to user space.

Returns number of bytes that could not be copied.
On success, this will be zero.

.. _`__copy_from_user`:

__copy_from_user
================

.. c:function::  __copy_from_user( to,  from,  n)

    - Copy a block of data from user space, with less checking. \* \ ``to``\ :   Destination address, in kernel space.

    :param  to:
        *undescribed*

    :param  from:
        Source address, in user space.

    :param  n:
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

.. _`copy_from_user`:

copy_from_user
==============

.. c:function::  copy_from_user( to,  from,  n)

    - Copy a block of data from user space.

    :param  to:
        Destination address, in kernel space.

    :param  from:
        Source address, in user space.

    :param  n:
        Number of bytes to copy.

.. _`copy_from_user.context`:

Context
-------

User context only. This function may sleep if pagefaults are
enabled.

.. _`copy_from_user.description`:

Description
-----------

Copy data from user space to kernel space.

Returns number of bytes that could not be copied.
On success, this will be zero.

If some data could not be copied, this function will pad the copied
data to the requested size using zero bytes.

.. _`__clear_user`:

__clear_user
============

.. c:function:: unsigned long __clear_user(void __user *mem, unsigned long len)

    - Zero a block of memory in user space, with less checking.

    :param void __user \*mem:
        *undescribed*

    :param unsigned long len:
        *undescribed*

.. _`__clear_user.description`:

Description
-----------

Zero a block of memory in user space.  Caller must check
the specified block with \ :c:func:`access_ok`\  before calling this function.

Returns number of bytes that could not be cleared.
On success, this will be zero.

.. _`clear_user`:

clear_user
==========

.. c:function:: unsigned long clear_user(void __user *mem, unsigned long len)

    - Zero a block of memory in user space.

    :param void __user \*mem:
        *undescribed*

    :param unsigned long len:
        *undescribed*

.. _`clear_user.description`:

Description
-----------

Zero a block of memory in user space.  Caller must check
the specified block with \ :c:func:`access_ok`\  before calling this function.

Returns number of bytes that could not be cleared.
On success, this will be zero.

.. _`strlen_user`:

strlen_user
===========

.. c:function::  strlen_user( str)

    - Get the size of a string in user space.

    :param  str:
        The string to measure.

.. _`strlen_user.context`:

Context
-------

User context only. This function may sleep if pagefaults are
enabled.

.. _`strlen_user.description`:

Description
-----------

Get the size of a NUL-terminated string in user space.

Returns the size of the string INCLUDING the terminating NUL.
On exception, returns 0.

If there is a limit on the length of a valid string, you may wish to
consider using \ :c:func:`strnlen_user`\  instead.

.. This file was automatic generated / don't edit.

