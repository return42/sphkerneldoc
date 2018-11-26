.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/include/asm/local.h

.. _`local_add_unless`:

local_add_unless
================

.. c:function:: int local_add_unless(local_t *l, long a, long u)

    add unless the number is a given value

    :param l:
        pointer of type local_t
    :type l: local_t \*

    :param a:
        the amount to add to v...
    :type a: long

    :param u:
        ...unless v is equal to u.
    :type u: long

.. _`local_add_unless.description`:

Description
-----------

Atomically adds \ ``a``\  to \ ``l``\ , so long as it was not \ ``u``\ .
Returns non-zero if \ ``l``\  was not \ ``u``\ , and zero otherwise.

.. This file was automatic generated / don't edit.

