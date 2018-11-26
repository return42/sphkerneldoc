.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/asm/qspinlock.h

.. _`native_queued_spin_unlock`:

native_queued_spin_unlock
=========================

.. c:function:: void native_queued_spin_unlock(struct qspinlock *lock)

    release a queued spinlock

    :param lock:
        Pointer to queued spinlock structure
    :type lock: struct qspinlock \*

.. _`native_queued_spin_unlock.description`:

Description
-----------

A \ :c:func:`smp_store_release`\  on the least-significant byte.

.. This file was automatic generated / don't edit.

