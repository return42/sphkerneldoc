.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/microblaze/include/asm/uaccess.h

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

.. This file was automatic generated / don't edit.

