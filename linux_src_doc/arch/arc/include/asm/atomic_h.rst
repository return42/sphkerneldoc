.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arc/include/asm/atomic.h

.. _`atomic64_dec_if_positive`:

atomic64_dec_if_positive
========================

.. c:function:: long long atomic64_dec_if_positive(atomic64_t *v)

    decrement by 1 if old value positive

    :param v:
        pointer of type atomic64_t
    :type v: atomic64_t \*

.. _`atomic64_dec_if_positive.description`:

Description
-----------

The function returns the old value of \*v minus 1, even if
the atomic variable, v, was not decremented.

.. _`atomic64_fetch_add_unless`:

atomic64_fetch_add_unless
=========================

.. c:function:: long long atomic64_fetch_add_unless(atomic64_t *v, long long a, long long u)

    add unless the number is a given value

    :param v:
        pointer of type atomic64_t
    :type v: atomic64_t \*

    :param a:
        the amount to add to v...
    :type a: long long

    :param u:
        ...unless v is equal to u.
    :type u: long long

.. _`atomic64_fetch_add_unless.description`:

Description
-----------

Atomically adds \ ``a``\  to \ ``v``\ , if it was not \ ``u``\ .
Returns the old value of \ ``v``\ 

.. This file was automatic generated / don't edit.

