.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/m68k/atari/stdma.c

.. _`stdma_try_lock`:

stdma_try_lock
==============

.. c:function:: int stdma_try_lock(irq_handler_t handler, void *data)

    attempt to acquire ST DMA interrupt "lock"

    :param irq_handler_t handler:
        interrupt handler to use after acquisition

    :param void \*data:
        *undescribed*

.. _`stdma_try_lock.description`:

Description
-----------

Returns !0 if lock was acquired; otherwise 0.

.. _`stdma_is_locked_by`:

stdma_is_locked_by
==================

.. c:function:: int stdma_is_locked_by(irq_handler_t handler)

    allow lock holder to check whether it needs to release.

    :param irq_handler_t handler:
        interrupt handler previously used to acquire lock.

.. _`stdma_is_locked_by.description`:

Description
-----------

Returns !0 if locked for the given handler; 0 otherwise.

.. This file was automatic generated / don't edit.

