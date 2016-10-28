.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thunderbolt/nhi.c

.. _`ring_interrupt_active`:

ring_interrupt_active
=====================

.. c:function:: void ring_interrupt_active(struct tb_ring *ring, bool active)

    activate/deactivate interrupts for a single ring

    :param struct tb_ring \*ring:
        *undescribed*

    :param bool active:
        *undescribed*

.. _`ring_interrupt_active.description`:

Description
-----------

ring->nhi->lock must be held.

.. _`nhi_disable_interrupts`:

nhi_disable_interrupts
======================

.. c:function:: void nhi_disable_interrupts(struct tb_nhi *nhi)

    disable interrupts for all rings

    :param struct tb_nhi \*nhi:
        *undescribed*

.. _`nhi_disable_interrupts.description`:

Description
-----------

Use only during init and shutdown.

.. _`ring_write_descriptors`:

ring_write_descriptors
======================

.. c:function:: void ring_write_descriptors(struct tb_ring *ring)

    post frames from ring->queue to the controller

    :param struct tb_ring \*ring:
        *undescribed*

.. _`ring_write_descriptors.description`:

Description
-----------

ring->lock is held.

.. _`ring_work`:

ring_work
=========

.. c:function:: void ring_work(struct work_struct *work)

    progress completed frames

    :param struct work_struct \*work:
        *undescribed*

.. _`ring_work.description`:

Description
-----------

If the ring is shutting down then all frames are marked as canceled and
their callbacks are invoked.

Otherwise we collect all completed frame from the ring buffer, write new
frame to the ring buffer and invoke the callbacks for the completed frames.

.. _`ring_start`:

ring_start
==========

.. c:function:: void ring_start(struct tb_ring *ring)

    enable a ring

    :param struct tb_ring \*ring:
        *undescribed*

.. _`ring_start.description`:

Description
-----------

Must not be invoked in parallel with \ :c:func:`ring_stop`\ .

.. _`ring_stop`:

ring_stop
=========

.. c:function:: void ring_stop(struct tb_ring *ring)

    shutdown a ring

    :param struct tb_ring \*ring:
        *undescribed*

.. _`ring_stop.description`:

Description
-----------

Must not be invoked from a callback.

This method will disable the ring. Further calls to ring_tx/ring_rx will
return -ESHUTDOWN until ring_stop has been called.

All enqueued frames will be canceled and their callbacks will be executed
with frame->canceled set to true (on the callback thread). This method
returns only after all callback invocations have finished.

.. This file was automatic generated / don't edit.

