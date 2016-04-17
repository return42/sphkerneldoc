.. -*- coding: utf-8; mode: rst -*-

=====
hsu.h
=====


.. _`hsu_dma_chip`:

struct hsu_dma_chip
===================

.. c:type:: hsu_dma_chip

    representation of HSU DMA hardware


.. _`hsu_dma_chip.definition`:

Definition
----------

.. code-block:: c

  struct hsu_dma_chip {
    struct device * dev;
    int irq;
    void __iomem * regs;
    unsigned int length;
    unsigned int offset;
    struct hsu_dma * hsu;
  };


.. _`hsu_dma_chip.members`:

Members
-------

:``dev``:
    struct device of the DMA controller

:``irq``:
    irq line

:``regs``:
    memory mapped I/O space

:``length``:
    I/O space length

:``offset``:
    offset of the I/O space where registers are located

:``hsu``:
    struct hsu_dma that is filed by ->:c:func:`probe`


