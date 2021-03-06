.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thunderbolt/nhi.c

.. _`ring_interrupt_active`:

ring_interrupt_active
=====================

.. c:function:: void ring_interrupt_active(struct tb_ring *ring, bool active)

    activate/deactivate interrupts for a single ring

    :param ring:
        *undescribed*
    :type ring: struct tb_ring \*

    :param active:
        *undescribed*
    :type active: bool

.. _`ring_interrupt_active.description`:

Description
-----------

ring->nhi->lock must be held.

.. _`nhi_disable_interrupts`:

nhi_disable_interrupts
======================

.. c:function:: void nhi_disable_interrupts(struct tb_nhi *nhi)

    disable interrupts for all rings

    :param nhi:
        *undescribed*
    :type nhi: struct tb_nhi \*

.. _`nhi_disable_interrupts.description`:

Description
-----------

Use only during init and shutdown.

.. _`ring_write_descriptors`:

ring_write_descriptors
======================

.. c:function:: void ring_write_descriptors(struct tb_ring *ring)

    post frames from ring->queue to the controller

    :param ring:
        *undescribed*
    :type ring: struct tb_ring \*

.. _`ring_write_descriptors.description`:

Description
-----------

ring->lock is held.

.. _`ring_work`:

ring_work
=========

.. c:function:: void ring_work(struct work_struct *work)

    progress completed frames

    :param work:
        *undescribed*
    :type work: struct work_struct \*

.. _`ring_work.description`:

Description
-----------

If the ring is shutting down then all frames are marked as canceled and
their callbacks are invoked.

Otherwise we collect all completed frame from the ring buffer, write new
frame to the ring buffer and invoke the callbacks for the completed frames.

.. _`tb_ring_poll`:

tb_ring_poll
============

.. c:function:: struct ring_frame *tb_ring_poll(struct tb_ring *ring)

    Poll one completed frame from the ring

    :param ring:
        Ring to poll
    :type ring: struct tb_ring \*

.. _`tb_ring_poll.description`:

Description
-----------

This function can be called when \ ``start_poll``\  callback of the \ ``ring``\ 
has been called. It will read one completed frame from the ring and
return it to the caller. Returns \ ``NULL``\  if there is no more completed
frames.

.. _`tb_ring_poll_complete`:

tb_ring_poll_complete
=====================

.. c:function:: void tb_ring_poll_complete(struct tb_ring *ring)

    Re-start interrupt for the ring

    :param ring:
        Ring to re-start the interrupt
    :type ring: struct tb_ring \*

.. _`tb_ring_poll_complete.description`:

Description
-----------

This will re-start (unmask) the ring interrupt once the user is done
with polling.

.. _`tb_ring_alloc_tx`:

tb_ring_alloc_tx
================

.. c:function:: struct tb_ring *tb_ring_alloc_tx(struct tb_nhi *nhi, int hop, int size, unsigned int flags)

    Allocate DMA ring for transmit

    :param nhi:
        Pointer to the NHI the ring is to be allocated
    :type nhi: struct tb_nhi \*

    :param hop:
        HopID (ring) to allocate
    :type hop: int

    :param size:
        Number of entries in the ring
    :type size: int

    :param flags:
        Flags for the ring
    :type flags: unsigned int

.. _`tb_ring_alloc_rx`:

tb_ring_alloc_rx
================

.. c:function:: struct tb_ring *tb_ring_alloc_rx(struct tb_nhi *nhi, int hop, int size, unsigned int flags, u16 sof_mask, u16 eof_mask, void (*start_poll)(void *), void *poll_data)

    Allocate DMA ring for receive

    :param nhi:
        Pointer to the NHI the ring is to be allocated
    :type nhi: struct tb_nhi \*

    :param hop:
        HopID (ring) to allocate. Pass \ ``-1``\  for automatic allocation.
    :type hop: int

    :param size:
        Number of entries in the ring
    :type size: int

    :param flags:
        Flags for the ring
    :type flags: unsigned int

    :param sof_mask:
        Mask of PDF values that start a frame
    :type sof_mask: u16

    :param eof_mask:
        Mask of PDF values that end a frame
    :type eof_mask: u16

    :param void (\*start_poll)(void \*):
        If not \ ``NULL``\  the ring will call this function when an
        interrupt is triggered and masked, instead of callback
        in each Rx frame.

    :param poll_data:
        Optional data passed to \ ``start_poll``\ 
    :type poll_data: void \*

.. _`tb_ring_start`:

tb_ring_start
=============

.. c:function:: void tb_ring_start(struct tb_ring *ring)

    enable a ring

    :param ring:
        *undescribed*
    :type ring: struct tb_ring \*

.. _`tb_ring_start.description`:

Description
-----------

Must not be invoked in parallel with \ :c:func:`tb_ring_stop`\ .

.. _`tb_ring_stop`:

tb_ring_stop
============

.. c:function:: void tb_ring_stop(struct tb_ring *ring)

    shutdown a ring

    :param ring:
        *undescribed*
    :type ring: struct tb_ring \*

.. _`tb_ring_stop.description`:

Description
-----------

Must not be invoked from a callback.

This method will disable the ring. Further calls to
tb_ring_tx/tb_ring_rx will return -ESHUTDOWN until ring_stop has been
called.

All enqueued frames will be canceled and their callbacks will be executed
with frame->canceled set to true (on the callback thread). This method
returns only after all callback invocations have finished.

.. _`nhi_mailbox_cmd`:

nhi_mailbox_cmd
===============

.. c:function:: int nhi_mailbox_cmd(struct tb_nhi *nhi, enum nhi_mailbox_cmd cmd, u32 data)

    Send a command through NHI mailbox

    :param nhi:
        Pointer to the NHI structure
    :type nhi: struct tb_nhi \*

    :param cmd:
        Command to send
    :type cmd: enum nhi_mailbox_cmd

    :param data:
        Data to be send with the command
    :type data: u32

.. _`nhi_mailbox_cmd.description`:

Description
-----------

Sends mailbox command to the firmware running on NHI. Returns \ ``0``\  in
case of success and negative errno in case of failure.

.. _`nhi_mailbox_mode`:

nhi_mailbox_mode
================

.. c:function:: enum nhi_fw_mode nhi_mailbox_mode(struct tb_nhi *nhi)

    Return current firmware operation mode

    :param nhi:
        Pointer to the NHI structure
    :type nhi: struct tb_nhi \*

.. _`nhi_mailbox_mode.description`:

Description
-----------

The function reads current firmware operation mode using NHI mailbox
registers and returns it to the caller.

.. This file was automatic generated / don't edit.

