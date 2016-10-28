.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/include/asm/atomic.h

.. _`__atomic_add_unless`:

__atomic_add_unless
===================

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

.. _`atomic_inc_not_zero`:

atomic_inc_not_zero
===================

.. c:function:: int atomic_inc_not_zero(atomic_t *v)

    increment unless the number is zero

    :param atomic_t \*v:
        pointer of type atomic_t

.. _`atomic_inc_not_zero.description`:

Description
-----------

Atomically increments \ ``v``\  by 1, so long as \ ``v``\  is non-zero.
Returns non-zero if \ ``v``\  was non-zero, and zero otherwise.

.. _`atomic64_add_unless`:

atomic64_add_unless
===================

.. c:function:: int atomic64_add_unless(atomic64_t *v, long a, long u)

    add unless the number is a given value

    :param atomic64_t \*v:
        pointer of type atomic64_t

    :param long a:
        the amount to add to v...

    :param long u:
        ...unless v is equal to u.

.. _`atomic64_add_unless.description`:

Description
-----------

Atomically adds \ ``a``\  to \ ``v``\ , so long as it was not \ ``u``\ .
Returns the old value of \ ``v``\ .

.. _`atomic64_inc_not_zero`:

atomic64_inc_not_zero
=====================

.. c:function:: long atomic64_inc_not_zero(atomic64_t *v)

    increment unless the number is zero

    :param atomic64_t \*v:
        pointer of type atomic64_t

.. _`atomic64_inc_not_zero.description`:

Description
-----------

Atomically increments \ ``v``\  by 1, so long as \ ``v``\  is non-zero.
Returns non-zero if \ ``v``\  was non-zero, and zero otherwise.

.. This file was automatic generated / don't edit.

