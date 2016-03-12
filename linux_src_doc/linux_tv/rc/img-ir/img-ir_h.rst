.. -*- coding: utf-8; mode: rst -*-

========
img-ir.h
========



.. _xref_struct_img_ir_priv:

struct img_ir_priv
==================

.. c:type:: struct img_ir_priv

    Private driver data.



Definition
----------

.. code-block:: c

  struct img_ir_priv {
    struct device * dev;
    int irq;
    struct clk * clk;
    struct clk * sys_clk;
    void __iomem * reg_base;
    spinlock_t lock;
    struct img_ir_priv_raw raw;
    struct img_ir_priv_hw hw;
  };



Members
-------

:``struct device * dev``:
    Platform device.

:``int irq``:
    IRQ number.

:``struct clk * clk``:
    Input clock.

:``struct clk * sys_clk``:
    System clock.

:``void __iomem * reg_base``:
    Iomem base address of IR register block.

:``spinlock_t lock``:
    Protects IR registers and variables in this struct.

:``struct img_ir_priv_raw raw``:
    Driver data for raw decoder.

:``struct img_ir_priv_hw hw``:
    Driver data for hardware decoder.



