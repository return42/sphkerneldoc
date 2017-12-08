.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/tile/include/asm/spinlock_32.h

.. _`arch_read_lock`:

arch_read_lock
==============

.. c:function:: void arch_read_lock(arch_rwlock_t *rwlock)

    acquire a read lock.

    :param arch_rwlock_t \*rwlock:
        *undescribed*

.. _`arch_write_lock`:

arch_write_lock
===============

.. c:function:: void arch_write_lock(arch_rwlock_t *rwlock)

    acquire a write lock.

    :param arch_rwlock_t \*rwlock:
        *undescribed*

.. _`arch_read_trylock`:

arch_read_trylock
=================

.. c:function:: int arch_read_trylock(arch_rwlock_t *rwlock)

    try to acquire a read lock.

    :param arch_rwlock_t \*rwlock:
        *undescribed*

.. _`arch_write_trylock`:

arch_write_trylock
==================

.. c:function:: int arch_write_trylock(arch_rwlock_t *rwlock)

    try to acquire a write lock.

    :param arch_rwlock_t \*rwlock:
        *undescribed*

.. _`arch_read_unlock`:

arch_read_unlock
================

.. c:function:: void arch_read_unlock(arch_rwlock_t *rwlock)

    release a read lock.

    :param arch_rwlock_t \*rwlock:
        *undescribed*

.. _`arch_write_unlock`:

arch_write_unlock
=================

.. c:function:: void arch_write_unlock(arch_rwlock_t *rwlock)

    release a write lock.

    :param arch_rwlock_t \*rwlock:
        *undescribed*

.. This file was automatic generated / don't edit.

