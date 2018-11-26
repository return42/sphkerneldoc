.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/spinlock.h

.. _`spin_is_locked`:

spin_is_locked
==============

.. c:function:: int spin_is_locked(spinlock_t *lock)

    Check whether a spinlock is locked.

    :param lock:
        Pointer to the spinlock.
    :type lock: spinlock_t \*

.. _`spin_is_locked.description`:

Description
-----------

This function is NOT required to provide any memory ordering
guarantees; it could be used for debugging purposes or, when
additional synchronization is needed, accompanied with other
constructs (memory barriers) enforcing the synchronization.

.. _`spin_is_locked.return`:

Return
------

1 if \ ``lock``\  is locked, 0 otherwise.

Note that the function only tells you that the spinlock is
seen to be locked, not that it is locked on your CPU.

Further, on CONFIG_SMP=n builds with CONFIG_DEBUG_SPINLOCK=n,
the return value is always 0 (see include/linux/spinlock_up.h).
Therefore you should not rely heavily on the return value.

.. _`_atomic_dec_and_lock`:

\_atomic_dec_and_lock
=====================

.. c:function:: int _atomic_dec_and_lock(atomic_t *atomic, spinlock_t *lock)

    lock on reaching reference count zero

    :param atomic:
        the atomic counter
    :type atomic: atomic_t \*

    :param lock:
        the spinlock in question
    :type lock: spinlock_t \*

.. _`_atomic_dec_and_lock.description`:

Description
-----------

Decrements \ ``atomic``\  by 1.  If the result is 0, returns true and locks
\ ``lock``\ .  Returns false for all other cases.

.. This file was automatic generated / don't edit.

