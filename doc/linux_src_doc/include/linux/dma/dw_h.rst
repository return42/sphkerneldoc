.. -*- coding: utf-8; mode: rst -*-

====
dw.h
====


.. _`dw_dma_chip`:

struct dw_dma_chip
==================

.. c:type:: dw_dma_chip

    representation of DesignWare DMA controller hardware


.. _`dw_dma_chip.definition`:

Definition
----------

.. code-block:: c

  struct dw_dma_chip {
    struct device * dev;
    int irq;
    void __iomem * regs;
    struct clk * clk;
    struct dw_dma * dw;
  };


.. _`dw_dma_chip.members`:

Members
-------

:``dev``:
    struct device of the DMA controller

:``irq``:
    irq line

:``regs``:
    memory mapped I/O space

:``clk``:
    hclk clock

:``dw``:
    struct dw_dma that is filed by :c:func:`dw_dma_probe`


