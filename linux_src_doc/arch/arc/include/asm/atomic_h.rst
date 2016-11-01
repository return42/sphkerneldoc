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

.. _`atomic64_dec_if_positive`:

atomic64_dec_if_positive
========================

.. c:function:: long long atomic64_dec_if_positive(atomic64_t *v)

    decrement by 1 if old value positive

    :param atomic64_t \*v:
        pointer of type atomic64_t

.. _`atomic64_dec_if_positive.description`:

Description
-----------

The function returns the old value of \*v minus 1, even if
the atomic variable, v, was not decremented.

.. _`atomic64_add_unless`:

atomic64_add_unless
===================

.. c:function:: int atomic64_add_unless(atomic64_t *v, long long a, long long u)

    add unless the number is a given value

    :param atomic64_t \*v:
        pointer of type atomic64_t

    :param long long a:
        the amount to add to v...

    :param long long u:
        ...unless v is equal to u.

.. _`atomic64_add_unless.description`:

Description
-----------

if (v != u) { v += a; ret = 1} else {ret = 0}
Returns 1 iff \ ``v``\  was not \ ``u``\  (i.e. if add actually happened)

.. This file was automatic generated / don't edit.

