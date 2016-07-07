.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/serio/gscps2.c

.. _`gscps2_interrupt`:

gscps2_interrupt
================

.. c:function:: irqreturn_t gscps2_interrupt(int irq, void *dev)

    Interruption service routine

    :param int irq:
        *undescribed*

    :param void \*dev:
        *undescribed*

.. _`gscps2_interrupt.description`:

Description
-----------

This function reads received PS/2 bytes and processes them on
all interfaces.
The problematic part here is, that the keyboard and mouse PS/2 port
share the same interrupt and it's not possible to send data if any
one of them holds input data. To solve this problem we try to receive
the data as fast as possible and handle the reporting to the upper layer
later.

.. _`gscps2_probe`:

gscps2_probe
============

.. c:function:: int gscps2_probe(struct parisc_device *dev)

    Probes PS2 devices

    :param struct parisc_device \*dev:
        *undescribed*

.. _`gscps2_remove`:

gscps2_remove
=============

.. c:function:: int gscps2_remove(struct parisc_device *dev)

    Removes PS2 devices

    :param struct parisc_device \*dev:
        *undescribed*

.. This file was automatic generated / don't edit.

