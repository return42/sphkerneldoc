.. -*- coding: utf-8; mode: rst -*-

==========
spinlock.h
==========


.. _`raw_spin_unlock_wait`:

raw_spin_unlock_wait
====================

.. c:function:: raw_spin_unlock_wait ( lock)

    wait until the spinlock gets unlocked

    :param lock:
        the spinlock in question.



.. _`raw_spin_can_lock`:

raw_spin_can_lock
=================

.. c:function:: raw_spin_can_lock ( lock)

    would raw_spin_trylock() succeed?

    :param lock:
        the spinlock in question.



.. _`_atomic_dec_and_lock`:

_atomic_dec_and_lock
====================

.. c:function:: int _atomic_dec_and_lock (atomic_t *atomic, spinlock_t *lock)

    lock on reaching reference count zero

    :param atomic_t \*atomic:
        the atomic counter

    :param spinlock_t \*lock:
        the spinlock in question



.. _`_atomic_dec_and_lock.description`:

Description
-----------

Decrements ``atomic`` by 1.  If the result is 0, returns true and locks
``lock``\ .  Returns false for all other cases.

