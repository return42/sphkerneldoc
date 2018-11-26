.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/octeon/cvmx-spinlock.h

.. _`cvmx_spinlock_t`:

typedef cvmx_spinlock_t
=======================

.. c:type:: typedef cvmx_spinlock_t


.. _`cvmx_spinlock_init`:

cvmx_spinlock_init
==================

.. c:function:: void cvmx_spinlock_init(cvmx_spinlock_t *lock)

    :param lock:
        Lock to initialize
    :type lock: cvmx_spinlock_t \*

.. _`cvmx_spinlock_locked`:

cvmx_spinlock_locked
====================

.. c:function:: int cvmx_spinlock_locked(cvmx_spinlock_t *lock)

    zero if the spinlock is currently locked

    :param lock:
        Lock to check
        Returns Non-zero if locked
    :type lock: cvmx_spinlock_t \*

.. _`cvmx_spinlock_unlock`:

cvmx_spinlock_unlock
====================

.. c:function:: void cvmx_spinlock_unlock(cvmx_spinlock_t *lock)

    :param lock:
        pointer to lock structure
    :type lock: cvmx_spinlock_t \*

.. _`cvmx_spinlock_trylock`:

cvmx_spinlock_trylock
=====================

.. c:function:: unsigned int cvmx_spinlock_trylock(cvmx_spinlock_t *lock)

    May take some time to acquire the lock even if it is available due to the ll/sc not succeeding.

    :param lock:
        pointer to lock structure
    :type lock: cvmx_spinlock_t \*

.. _`cvmx_spinlock_trylock.returns-0`:

Returns 0
---------

lock successfully taken
1: lock not taken, held by someone else
These return values match the Linux semantics.

.. _`cvmx_spinlock_lock`:

cvmx_spinlock_lock
==================

.. c:function:: void cvmx_spinlock_lock(cvmx_spinlock_t *lock)

    :param lock:
        pointer to lock structure
    :type lock: cvmx_spinlock_t \*

.. _`cvmx_spinlock_bit_lock`:

cvmx_spinlock_bit_lock
======================

.. c:function:: void cvmx_spinlock_bit_lock(uint32_t *word)

    Preserves the low 31 bits of the 32 bit word used for the lock.

    :param word:
        word to lock bit 31 of
    :type word: uint32_t \*

.. _`cvmx_spinlock_bit_trylock`:

cvmx_spinlock_bit_trylock
=========================

.. c:function:: unsigned int cvmx_spinlock_bit_trylock(uint32_t *word)

    Preserves the low 31 bits of the 32 bit word used for the lock.

    :param word:
        word to lock bit 31 of
    :type word: uint32_t \*

.. _`cvmx_spinlock_bit_trylock.returns-0`:

Returns 0
---------

lock successfully taken
1: lock not taken, held by someone else
These return values match the Linux semantics.

.. _`cvmx_spinlock_bit_unlock`:

cvmx_spinlock_bit_unlock
========================

.. c:function:: void cvmx_spinlock_bit_unlock(uint32_t *word)

    :param word:
        word to unlock bit 31 in
    :type word: uint32_t \*

.. _`cvmx_spinlock_bit_unlock.description`:

Description
-----------

Unconditionally clears bit 31 of the lock word.  Note that this is
done non-atomically, as this implementation assumes that the rest
of the bits in the word are protected by the lock.

.. This file was automatic generated / don't edit.

