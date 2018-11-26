.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/asm-generic/qspinlock.h

.. _`queued_spin_is_locked`:

queued_spin_is_locked
=====================

.. c:function:: int queued_spin_is_locked(struct qspinlock *lock)

    is the spinlock locked?

    :param lock:
        Pointer to queued spinlock structure
    :type lock: struct qspinlock \*

.. _`queued_spin_is_locked.return`:

Return
------

1 if it is locked, 0 otherwise

.. _`queued_spin_value_unlocked`:

queued_spin_value_unlocked
==========================

.. c:function:: int queued_spin_value_unlocked(struct qspinlock lock)

    is the spinlock structure unlocked?

    :param lock:
        queued spinlock structure
    :type lock: struct qspinlock

.. _`queued_spin_value_unlocked.return`:

Return
------

1 if it is unlocked, 0 otherwise

N.B. Whenever there are tasks waiting for the lock, it is considered
locked wrt the lockref code to avoid lock stealing by the lockref
code and change things underneath the lock. This also allows some
optimizations to be applied without conflict with lockref.

.. _`queued_spin_is_contended`:

queued_spin_is_contended
========================

.. c:function:: int queued_spin_is_contended(struct qspinlock *lock)

    check if the lock is contended

    :param lock:
        Pointer to queued spinlock structure
    :type lock: struct qspinlock \*

.. _`queued_spin_is_contended.return`:

Return
------

1 if lock contended, 0 otherwise

.. _`queued_spin_trylock`:

queued_spin_trylock
===================

.. c:function:: int queued_spin_trylock(struct qspinlock *lock)

    try to acquire the queued spinlock

    :param lock:
        Pointer to queued spinlock structure
    :type lock: struct qspinlock \*

.. _`queued_spin_trylock.return`:

Return
------

1 if lock acquired, 0 if failed

.. _`queued_spin_lock`:

queued_spin_lock
================

.. c:function:: void queued_spin_lock(struct qspinlock *lock)

    acquire a queued spinlock

    :param lock:
        Pointer to queued spinlock structure
    :type lock: struct qspinlock \*

.. _`queued_spin_unlock`:

queued_spin_unlock
==================

.. c:function:: void queued_spin_unlock(struct qspinlock *lock)

    release a queued spinlock

    :param lock:
        Pointer to queued spinlock structure
    :type lock: struct qspinlock \*

.. This file was automatic generated / don't edit.

