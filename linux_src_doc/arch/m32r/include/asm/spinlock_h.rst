.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/m32r/include/asm/spinlock.h

.. _`arch_spin_trylock`:

arch_spin_trylock
=================

.. c:function:: int arch_spin_trylock(arch_spinlock_t *lock)

    Try spin lock and return a result

    :param arch_spinlock_t \*lock:
        Pointer to the lock variable

.. _`arch_spin_trylock.description`:

Description
-----------

\ :c:func:`arch_spin_trylock`\  tries to get the lock and returns a result.
On the m32r, the result value is 1 (= Success) or 0 (= Failure).

.. _`arch_read_can_lock`:

arch_read_can_lock
==================

.. c:function::  arch_read_can_lock( x)

    would \ :c:func:`read_trylock`\  succeed?

    :param  x:
        *undescribed*

.. _`arch_write_can_lock`:

arch_write_can_lock
===================

.. c:function::  arch_write_can_lock( x)

    would \ :c:func:`write_trylock`\  succeed?

    :param  x:
        *undescribed*

.. This file was automatic generated / don't edit.

