.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/idma64.h

.. _`idma64_chip`:

struct idma64_chip
==================

.. c:type:: struct idma64_chip

    representation of iDMA 64-bit controller hardware

.. _`idma64_chip.definition`:

Definition
----------

.. code-block:: c

    struct idma64_chip {
        struct device *dev;
        int irq;
        void __iomem *regs;
        struct idma64 *idma64;
    }

.. _`idma64_chip.members`:

Members
-------

dev
    struct device of the DMA controller

irq
    irq line

regs
    memory mapped I/O space

idma64
    struct idma64 that is filed by \ :c:func:`idma64_probe`\ 

.. This file was automatic generated / don't edit.

