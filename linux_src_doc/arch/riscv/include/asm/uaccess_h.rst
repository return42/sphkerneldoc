.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/riscv/include/asm/uaccess.h

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

User context only.  This function may sleep.

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

\__get_user
===========

.. c:function::  __get_user( x,  ptr)

    - Get a simple variable from user space, with less checking.

    :param  x:
        Variable to store result.

    :param  ptr:
        Source address, in user space.

.. _`__get_user.context`:

Context
-------

User context only.  This function may sleep.

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

User context only.  This function may sleep.

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

.. _`__put_user`:

\__put_user
===========

.. c:function::  __put_user( x,  ptr)

    - Write a simple value into user space, with less checking.

    :param  x:
        Value to copy to user space.

    :param  ptr:
        Destination address, in user space.

.. _`__put_user.context`:

Context
-------

User context only.  This function may sleep.

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

User context only.  This function may sleep.

.. _`put_user.description`:

Description
-----------

This macro copies a single simple value from kernel space to user
space.  It supports simple types like char and int, but not larger
data types like structures or arrays.

\ ``ptr``\  must have pointer-to-simple-variable type, and \ ``x``\  must be assignable
to the result of dereferencing \ ``ptr``\ .

Returns zero on success, or -EFAULT on error.

.. This file was automatic generated / don't edit.

