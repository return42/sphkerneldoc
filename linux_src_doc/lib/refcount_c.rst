.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/refcount.c

.. _`refcount_add_not_zero_checked`:

refcount_add_not_zero_checked
=============================

.. c:function:: bool refcount_add_not_zero_checked(unsigned int i, refcount_t *r)

    add a value to a refcount unless it is 0

    :param i:
        the value to add to the refcount
    :type i: unsigned int

    :param r:
        the refcount
    :type r: refcount_t \*

.. _`refcount_add_not_zero_checked.description`:

Description
-----------

Will saturate at UINT_MAX and WARN.

Provides no memory ordering, it is assumed the caller has guaranteed the
object memory to be stable (RCU, etc.). It does provide a control dependency
and thereby orders future stores. See the comment on top.

Use of this function is not recommended for the normal reference counting
use case in which references are taken and released one at a time.  In these
cases, \ :c:func:`refcount_inc`\ , or one of its variants, should instead be used to
increment a reference count.

.. _`refcount_add_not_zero_checked.return`:

Return
------

false if the passed refcount is 0, true otherwise

.. _`refcount_add_checked`:

refcount_add_checked
====================

.. c:function:: void refcount_add_checked(unsigned int i, refcount_t *r)

    add a value to a refcount

    :param i:
        the value to add to the refcount
    :type i: unsigned int

    :param r:
        the refcount
    :type r: refcount_t \*

.. _`refcount_add_checked.description`:

Description
-----------

Similar to \ :c:func:`atomic_add`\ , but will saturate at UINT_MAX and WARN.

Provides no memory ordering, it is assumed the caller has guaranteed the
object memory to be stable (RCU, etc.). It does provide a control dependency
and thereby orders future stores. See the comment on top.

Use of this function is not recommended for the normal reference counting
use case in which references are taken and released one at a time.  In these
cases, \ :c:func:`refcount_inc`\ , or one of its variants, should instead be used to
increment a reference count.

.. _`refcount_inc_not_zero_checked`:

refcount_inc_not_zero_checked
=============================

.. c:function:: bool refcount_inc_not_zero_checked(refcount_t *r)

    increment a refcount unless it is 0

    :param r:
        the refcount to increment
    :type r: refcount_t \*

.. _`refcount_inc_not_zero_checked.description`:

Description
-----------

Similar to \ :c:func:`atomic_inc_not_zero`\ , but will saturate at UINT_MAX and WARN.

Provides no memory ordering, it is assumed the caller has guaranteed the
object memory to be stable (RCU, etc.). It does provide a control dependency
and thereby orders future stores. See the comment on top.

.. _`refcount_inc_not_zero_checked.return`:

Return
------

true if the increment was successful, false otherwise

.. _`refcount_inc_checked`:

refcount_inc_checked
====================

.. c:function:: void refcount_inc_checked(refcount_t *r)

    increment a refcount

    :param r:
        the refcount to increment
    :type r: refcount_t \*

.. _`refcount_inc_checked.description`:

Description
-----------

Similar to \ :c:func:`atomic_inc`\ , but will saturate at UINT_MAX and WARN.

Provides no memory ordering, it is assumed the caller already has a
reference on the object.

Will WARN if the refcount is 0, as this represents a possible use-after-free
condition.

.. _`refcount_sub_and_test_checked`:

refcount_sub_and_test_checked
=============================

.. c:function:: bool refcount_sub_and_test_checked(unsigned int i, refcount_t *r)

    subtract from a refcount and test if it is 0

    :param i:
        amount to subtract from the refcount
    :type i: unsigned int

    :param r:
        the refcount
    :type r: refcount_t \*

.. _`refcount_sub_and_test_checked.description`:

Description
-----------

Similar to \ :c:func:`atomic_dec_and_test`\ , but it will WARN, return false and
ultimately leak on underflow and will fail to decrement when saturated
at UINT_MAX.

Provides release memory ordering, such that prior loads and stores are done
before, and provides a control dependency such that \ :c:func:`free`\  must come after.
See the comment on top.

Use of this function is not recommended for the normal reference counting
use case in which references are taken and released one at a time.  In these
cases, \ :c:func:`refcount_dec`\ , or one of its variants, should instead be used to
decrement a reference count.

.. _`refcount_sub_and_test_checked.return`:

Return
------

true if the resulting refcount is 0, false otherwise

.. _`refcount_dec_and_test_checked`:

refcount_dec_and_test_checked
=============================

.. c:function:: bool refcount_dec_and_test_checked(refcount_t *r)

    decrement a refcount and test if it is 0

    :param r:
        the refcount
    :type r: refcount_t \*

.. _`refcount_dec_and_test_checked.description`:

Description
-----------

Similar to \ :c:func:`atomic_dec_and_test`\ , it will WARN on underflow and fail to
decrement when saturated at UINT_MAX.

Provides release memory ordering, such that prior loads and stores are done
before, and provides a control dependency such that \ :c:func:`free`\  must come after.
See the comment on top.

.. _`refcount_dec_and_test_checked.return`:

Return
------

true if the resulting refcount is 0, false otherwise

.. _`refcount_dec_checked`:

refcount_dec_checked
====================

.. c:function:: void refcount_dec_checked(refcount_t *r)

    decrement a refcount

    :param r:
        the refcount
    :type r: refcount_t \*

.. _`refcount_dec_checked.description`:

Description
-----------

Similar to \ :c:func:`atomic_dec`\ , it will WARN on underflow and fail to decrement
when saturated at UINT_MAX.

Provides release memory ordering, such that prior loads and stores are done
before.

.. _`refcount_dec_if_one`:

refcount_dec_if_one
===================

.. c:function:: bool refcount_dec_if_one(refcount_t *r)

    decrement a refcount if it is 1

    :param r:
        the refcount
    :type r: refcount_t \*

.. _`refcount_dec_if_one.description`:

Description
-----------

No atomic_t counterpart, it attempts a 1 -> 0 transition and returns the
success thereof.

Like all decrement operations, it provides release memory order and provides
a control dependency.

It can be used like a try-delete operator; this explicit case is provided
and not cmpxchg in generic, because that would allow implementing unsafe
operations.

.. _`refcount_dec_if_one.return`:

Return
------

true if the resulting refcount is 0, false otherwise

.. _`refcount_dec_not_one`:

refcount_dec_not_one
====================

.. c:function:: bool refcount_dec_not_one(refcount_t *r)

    decrement a refcount if it is not 1

    :param r:
        the refcount
    :type r: refcount_t \*

.. _`refcount_dec_not_one.description`:

Description
-----------

No atomic_t counterpart, it decrements unless the value is 1, in which case
it will return false.

Was often done like: atomic_add_unless(&var, -1, 1)

.. _`refcount_dec_not_one.return`:

Return
------

true if the decrement operation was successful, false otherwise

.. _`refcount_dec_and_mutex_lock`:

refcount_dec_and_mutex_lock
===========================

.. c:function:: bool refcount_dec_and_mutex_lock(refcount_t *r, struct mutex *lock)

    return holding mutex if able to decrement refcount to 0

    :param r:
        the refcount
    :type r: refcount_t \*

    :param lock:
        the mutex to be locked
    :type lock: struct mutex \*

.. _`refcount_dec_and_mutex_lock.description`:

Description
-----------

Similar to \ :c:func:`atomic_dec_and_mutex_lock`\ , it will WARN on underflow and fail
to decrement when saturated at UINT_MAX.

Provides release memory ordering, such that prior loads and stores are done
before, and provides a control dependency such that \ :c:func:`free`\  must come after.
See the comment on top.

.. _`refcount_dec_and_mutex_lock.return`:

Return
------

true and hold mutex if able to decrement refcount to 0, false
        otherwise

.. _`refcount_dec_and_lock`:

refcount_dec_and_lock
=====================

.. c:function:: bool refcount_dec_and_lock(refcount_t *r, spinlock_t *lock)

    return holding spinlock if able to decrement refcount to 0

    :param r:
        the refcount
    :type r: refcount_t \*

    :param lock:
        the spinlock to be locked
    :type lock: spinlock_t \*

.. _`refcount_dec_and_lock.description`:

Description
-----------

Similar to \ :c:func:`atomic_dec_and_lock`\ , it will WARN on underflow and fail to
decrement when saturated at UINT_MAX.

Provides release memory ordering, such that prior loads and stores are done
before, and provides a control dependency such that \ :c:func:`free`\  must come after.
See the comment on top.

.. _`refcount_dec_and_lock.return`:

Return
------

true and hold spinlock if able to decrement refcount to 0, false
        otherwise

.. _`refcount_dec_and_lock_irqsave`:

refcount_dec_and_lock_irqsave
=============================

.. c:function:: bool refcount_dec_and_lock_irqsave(refcount_t *r, spinlock_t *lock, unsigned long *flags)

    return holding spinlock with disabled interrupts if able to decrement refcount to 0

    :param r:
        the refcount
    :type r: refcount_t \*

    :param lock:
        the spinlock to be locked
    :type lock: spinlock_t \*

    :param flags:
        saved IRQ-flags if the is acquired
    :type flags: unsigned long \*

.. _`refcount_dec_and_lock_irqsave.description`:

Description
-----------

Same as \ :c:func:`refcount_dec_and_lock`\  above except that the spinlock is acquired
with disabled interupts.

.. _`refcount_dec_and_lock_irqsave.return`:

Return
------

true and hold spinlock if able to decrement refcount to 0, false
        otherwise

.. This file was automatic generated / don't edit.

