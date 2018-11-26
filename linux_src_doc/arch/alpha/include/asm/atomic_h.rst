.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/alpha/include/asm/atomic.h

.. _`atomic_fetch_add_unless`:

atomic_fetch_add_unless
=======================

.. c:function:: int atomic_fetch_add_unless(atomic_t *v, int a, int u)

    add unless the number is a given value

    :param v:
        pointer of type atomic_t
    :type v: atomic_t \*

    :param a:
        the amount to add to v...
    :type a: int

    :param u:
        ...unless v is equal to u.
    :type u: int

.. _`atomic_fetch_add_unless.description`:

Description
-----------

Atomically adds \ ``a``\  to \ ``v``\ , so long as it was not \ ``u``\ .
Returns the old value of \ ``v``\ .

.. _`atomic64_fetch_add_unless`:

atomic64_fetch_add_unless
=========================

.. c:function:: long atomic64_fetch_add_unless(atomic64_t *v, long a, long u)

    add unless the number is a given value

    :param v:
        pointer of type atomic64_t
    :type v: atomic64_t \*

    :param a:
        the amount to add to v...
    :type a: long

    :param u:
        ...unless v is equal to u.
    :type u: long

.. _`atomic64_fetch_add_unless.description`:

Description
-----------

Atomically adds \ ``a``\  to \ ``v``\ , so long as it was not \ ``u``\ .
Returns the old value of \ ``v``\ .

.. This file was automatic generated / don't edit.

