.. -*- coding: utf-8; mode: rst -*-

=================
mpc52xx_lpbfifo.c
=================


.. _`mpc52xx_lpbfifo_kick`:

mpc52xx_lpbfifo_kick
====================

.. c:function:: void mpc52xx_lpbfifo_kick (struct mpc52xx_lpbfifo_request *req)

    Trigger the next block of data to be transferred

    :param struct mpc52xx_lpbfifo_request \*req:

        *undescribed*



.. _`mpc52xx_lpbfifo_irq`:

mpc52xx_lpbfifo_irq
===================

.. c:function:: irqreturn_t mpc52xx_lpbfifo_irq (int irq, void *dev_id)

    IRQ handler for LPB FIFO

    :param int irq:

        *undescribed*

    :param void \*dev_id:

        *undescribed*



.. _`mpc52xx_lpbfifo_irq.description`:

Description
-----------


On transmit, the dma completion irq triggers before the fifo completion
triggers.  Handle the dma completion here instead of the LPB FIFO Bestcomm
task completion irq because everything is not really done until the LPB FIFO
completion irq triggers.



.. _`mpc52xx_lpbfifo_irq.in-other-words`:

In other words
--------------

For DMA, on receive, the "Fat Lady" is the bestcom completion irq. on
transmit, the fifo completion irq is the "Fat Lady". The opera (or in this
case the DMA/FIFO operation) is not finished until the "Fat Lady" sings.



.. _`mpc52xx_lpbfifo_irq.reasons-for-entering-this-routine`:

Reasons for entering this routine
---------------------------------

1) PIO mode rx and tx completion irq
2) DMA interrupt mode tx completion irq
3) DMA polled mode tx



.. _`mpc52xx_lpbfifo_irq.exit-conditions`:

Exit conditions
---------------

1) Transfer aborted
2) FIFO complete without DMA; more data to do
3) FIFO complete without DMA; all data transferred
4) FIFO complete using DMA

Condition 1 can occur regardless of whether or not DMA is used.
It requires executing the callback to report the error and exiting
immediately.

Condition 2 requires programming the FIFO with the next block of data

Condition 3 requires executing the callback to report completion

Condition 4 means the same as 3, except that we also retrieve the bcom
buffer so DMA doesn't get clogged up.

To make things trickier, the spinlock must be dropped before
executing the callback, otherwise we could end up with a deadlock
or nested spinlock condition.  The out path is non-trivial, so
extra fiddling is done to make sure all paths lead to the same
outbound code.



.. _`mpc52xx_lpbfifo_bcom_irq`:

mpc52xx_lpbfifo_bcom_irq
========================

.. c:function:: irqreturn_t mpc52xx_lpbfifo_bcom_irq (int irq, void *dev_id)

    IRQ handler for LPB FIFO Bestcomm task

    :param int irq:

        *undescribed*

    :param void \*dev_id:

        *undescribed*



.. _`mpc52xx_lpbfifo_bcom_irq.description`:

Description
-----------


Only used when receiving data.



.. _`mpc52xx_lpbfifo_poll`:

mpc52xx_lpbfifo_poll
====================

.. c:function:: void mpc52xx_lpbfifo_poll ( void)

    Poll for DMA completion

    :param void:
        no arguments



.. _`mpc52xx_lpbfifo_submit`:

mpc52xx_lpbfifo_submit
======================

.. c:function:: int mpc52xx_lpbfifo_submit (struct mpc52xx_lpbfifo_request *req)

    Submit an LPB FIFO transfer request.

    :param struct mpc52xx_lpbfifo_request \*req:
        Pointer to request structure

