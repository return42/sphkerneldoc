.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/tile/include/asm/spinlock_64.h

.. _`arch_read_can_lock`:

arch_read_can_lock
==================

.. c:function:: int arch_read_can_lock(arch_rwlock_t *rw)

    would \ :c:func:`read_trylock`\  succeed?

    :param arch_rwlock_t \*rw:
        *undescribed*

.. _`arch_write_can_lock`:

arch_write_can_lock
===================

.. c:function:: int arch_write_can_lock(arch_rwlock_t *rw)

    would \ :c:func:`write_trylock`\  succeed?

    :param arch_rwlock_t \*rw:
        *undescribed*

.. This file was automatic generated / don't edit.

