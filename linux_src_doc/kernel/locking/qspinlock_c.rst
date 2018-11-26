.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/locking/qspinlock.c

.. _`clear_pending`:

clear_pending
=============

.. c:function:: void clear_pending(struct qspinlock *lock)

    clear the pending bit.

    :param lock:
        Pointer to queued spinlock structure
    :type lock: struct qspinlock \*

.. _`clear_pending.description`:

Description
-----------

\*,1,\* -> \*,0,\*

.. _`clear_pending_set_locked`:

clear_pending_set_locked
========================

.. c:function:: void clear_pending_set_locked(struct qspinlock *lock)

    take ownership and clear the pending bit.

    :param lock:
        Pointer to queued spinlock structure
    :type lock: struct qspinlock \*

.. _`clear_pending_set_locked.description`:

Description
-----------

\*,1,0 -> \*,0,1

Lock stealing is not allowed if this function is used.

.. _`clear_pending`:

clear_pending
=============

.. c:function:: void clear_pending(struct qspinlock *lock)

    clear the pending bit.

    :param lock:
        Pointer to queued spinlock structure
    :type lock: struct qspinlock \*

.. _`clear_pending.description`:

Description
-----------

\*,1,\* -> \*,0,\*

.. _`clear_pending_set_locked`:

clear_pending_set_locked
========================

.. c:function:: void clear_pending_set_locked(struct qspinlock *lock)

    take ownership and clear the pending bit.

    :param lock:
        Pointer to queued spinlock structure
    :type lock: struct qspinlock \*

.. _`clear_pending_set_locked.description`:

Description
-----------

\*,1,0 -> \*,0,1

.. _`xchg_tail`:

xchg_tail
=========

.. c:function:: u32 xchg_tail(struct qspinlock *lock, u32 tail)

    Put in the new queue tail code word & retrieve previous one

    :param lock:
        Pointer to queued spinlock structure
    :type lock: struct qspinlock \*

    :param tail:
        The new queue tail code word
    :type tail: u32

.. _`xchg_tail.return`:

Return
------

The previous queue tail code word

xchg(lock, tail)

p,\*,\* -> n,\*,\* ; prev = xchg(lock, node)

.. _`queued_fetch_set_pending_acquire`:

queued_fetch_set_pending_acquire
================================

.. c:function:: u32 queued_fetch_set_pending_acquire(struct qspinlock *lock)

    fetch the whole lock value and set pending

    :param lock:
        Pointer to queued spinlock structure
    :type lock: struct qspinlock \*

.. _`queued_fetch_set_pending_acquire.return`:

Return
------

The previous lock value

\*,\*,\* -> \*,1,\*

.. _`set_locked`:

set_locked
==========

.. c:function:: void set_locked(struct qspinlock *lock)

    Set the lock bit and own the lock

    :param lock:
        Pointer to queued spinlock structure
    :type lock: struct qspinlock \*

.. _`set_locked.description`:

Description
-----------

\*,\*,0 -> \*,0,1

.. _`queued_spin_lock_slowpath`:

queued_spin_lock_slowpath
=========================

.. c:function:: void queued_spin_lock_slowpath(struct qspinlock *lock, u32 val)

    acquire the queued spinlock

    :param lock:
        Pointer to queued spinlock structure
    :type lock: struct qspinlock \*

    :param val:
        Current value of the queued spinlock 32-bit word
    :type val: u32

.. _`queued_spin_lock_slowpath.description`:

Description
-----------

(queue tail, pending bit, lock value)

fast     :    slow                                  :    unlock
:                                          :
uncontended  (0,0,0) -:--> (0,0,1) ------------------------------:--> (\*,\*,0)
:       \| ^--------.------.             /  :
:       v           \      \            \|  :
pending               :    (0,1,1) +--> (0,1,0)   \           \|  :
:       \| ^--'              \|           \|  :
:       v                   \|           \|  :
uncontended           :    (n,x,y) +--> (n,0,0) --'           \|  :
queue               :       \| ^--'                          \|  :
:       v                               \|  :
contended             :    (\*,x,y) +--> (\*,0,0) ---> (\*,0,1) -'  :
queue               :         ^--'                             :

.. This file was automatic generated / don't edit.

