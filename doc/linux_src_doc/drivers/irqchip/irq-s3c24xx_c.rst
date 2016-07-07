.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/irqchip/irq-s3c24xx.c

.. _`s3c24xx_set_fiq`:

s3c24xx_set_fiq
===============

.. c:function:: int s3c24xx_set_fiq(unsigned int irq, bool on)

    set the FIQ routing

    :param unsigned int irq:
        IRQ number to route to FIQ on processor.

    :param bool on:
        Whether to route \ ``irq``\  to the FIQ, or to remove the FIQ routing.

.. _`s3c24xx_set_fiq.description`:

Description
-----------

Change the state of the IRQ to FIQ routing depending on \ ``irq``\  and \ ``on``\ . If
\ ``on``\  is true, the \ ``irq``\  is checked to see if it can be routed and the
interrupt controller updated to route the IRQ. If \ ``on``\  is false, the FIQ
routing is cleared, regardless of which \ ``irq``\  is specified.

.. This file was automatic generated / don't edit.

