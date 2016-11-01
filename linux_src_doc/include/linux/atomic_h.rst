.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/atomic.h

.. _`atomic_add_unless`:

atomic_add_unless
=================

.. c:function:: int atomic_add_unless(atomic_t *v, int a, int u)

    add unless the number is already a given value

    :param atomic_t \*v:
        pointer of type atomic_t

    :param int a:
        the amount to add to v...

    :param int u:
        ...unless v is equal to u.

.. _`atomic_add_unless.description`:

Description
-----------

Atomically adds \ ``a``\  to \ ``v``\ , so long as \ ``v``\  was not already \ ``u``\ .
Returns non-zero if \ ``v``\  was not \ ``u``\ , and zero otherwise.

.. _`atomic_inc_not_zero`:

atomic_inc_not_zero
===================

.. c:function::  atomic_inc_not_zero( v)

    increment unless the number is zero

    :param  v:
        pointer of type atomic_t

.. _`atomic_inc_not_zero.description`:

Description
-----------

Atomically increments \ ``v``\  by 1, so long as \ ``v``\  is non-zero.
Returns non-zero if \ ``v``\  was non-zero, and zero otherwise.

.. _`atomic_inc_not_zero_hint`:

atomic_inc_not_zero_hint
========================

.. c:function:: int atomic_inc_not_zero_hint(atomic_t *v, int hint)

    increment if not null

    :param atomic_t \*v:
        pointer of type atomic_t

    :param int hint:
        probable value of the atomic before the increment

.. _`atomic_inc_not_zero_hint.description`:

Description
-----------

This version of \ :c:func:`atomic_inc_not_zero`\  gives a hint of probable
value of the atomic. This helps processor to not read the memory
before doing the atomic read/modify/write cycle, lowering
number of bus transactions on some arches.

.. _`atomic_inc_not_zero_hint.return`:

Return
------

0 if increment was not done, 1 otherwise.

.. This file was automatic generated / don't edit.

