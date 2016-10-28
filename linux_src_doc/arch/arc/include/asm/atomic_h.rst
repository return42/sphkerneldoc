.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arc/include/asm/atomic.h

.. _`__atomic_add_unless`:

__atomic_add_unless
===================

.. c:function::  __atomic_add_unless( v,  a,  u)

    add unless the number is a given value

    :param  v:
        pointer of type atomic_t

    :param  a:
        the amount to add to v...

    :param  u:
        ...unless v is equal to u.

.. _`__atomic_add_unless.description`:

Description
-----------

Atomically adds \ ``a``\  to \ ``v``\ , so long as it was not \ ``u``\ .
Returns the old value of \ ``v``\ 

.. This file was automatic generated / don't edit.

