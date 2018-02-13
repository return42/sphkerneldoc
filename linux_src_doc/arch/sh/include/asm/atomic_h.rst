.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/sh/include/asm/atomic.h

.. _`__atomic_add_unless`:

\__atomic_add_unless
====================

.. c:function:: int __atomic_add_unless(atomic_t *v, int a, int u)

    add unless the number is a given value

    :param atomic_t \*v:
        pointer of type atomic_t

    :param int a:
        the amount to add to v...

    :param int u:
        ...unless v is equal to u.

.. _`__atomic_add_unless.description`:

Description
-----------

Atomically adds \ ``a``\  to \ ``v``\ , so long as it was not \ ``u``\ .
Returns the old value of \ ``v``\ .

.. This file was automatic generated / don't edit.

