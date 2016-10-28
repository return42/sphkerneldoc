.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/ipu/ipu_irq.c

.. _`ipu_irq_status`:

ipu_irq_status
==============

.. c:function:: bool ipu_irq_status(unsigned int irq)

    returns the current interrupt status of the specified IRQ.

    :param unsigned int irq:
        interrupt line to get status for.

.. _`ipu_irq_map`:

ipu_irq_map
===========

.. c:function:: int ipu_irq_map(unsigned int source)

    map an IPU interrupt source to an IRQ number

    :param unsigned int source:
        interrupt source bit position (see below)

.. _`ipu_irq_map.description`:

Description
-----------

The source parameter has to be explained further. On i.MX31 IPU has 137 IRQ
sources, they are broken down in 5 32-bit registers, like 32, 32, 24, 32, 17.
However, the source argument of this function is not the sequence number of
the possible IRQ, but rather its bit position. So, first interrupt in fourth
register has source number 96, and not 88. This makes calculations easier,
and also provides forward compatibility with any future IPU implementations
with any interrupt bit assignments.

.. _`ipu_irq_unmap`:

ipu_irq_unmap
=============

.. c:function:: int ipu_irq_unmap(unsigned int source)

    map an IPU interrupt source to an IRQ number

    :param unsigned int source:
        interrupt source bit position (see \ :c:func:`ipu_irq_map`\ )

.. This file was automatic generated / don't edit.

