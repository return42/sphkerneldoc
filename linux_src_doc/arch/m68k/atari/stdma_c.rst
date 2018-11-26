.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/m68k/atari/stdma.c

.. _`stdma_try_lock`:

stdma_try_lock
==============

.. c:function:: int stdma_try_lock(irq_handler_t handler, void *data)

    attempt to acquire ST DMA interrupt "lock"

    :param handler:
        interrupt handler to use after acquisition
    :type handler: irq_handler_t

    :param data:
        *undescribed*
    :type data: void \*

.. _`stdma_try_lock.description`:

Description
-----------

Returns !0 if lock was acquired; otherwise 0.

.. _`stdma_is_locked_by`:

stdma_is_locked_by
==================

.. c:function:: int stdma_is_locked_by(irq_handler_t handler)

    allow lock holder to check whether it needs to release.

    :param handler:
        interrupt handler previously used to acquire lock.
    :type handler: irq_handler_t

.. _`stdma_is_locked_by.description`:

Description
-----------

Returns !0 if locked for the given handler; 0 otherwise.

.. This file was automatic generated / don't edit.

