.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/rc/img-ir/img-ir.h

.. _`img_ir_priv`:

struct img_ir_priv
==================

.. c:type:: struct img_ir_priv

    Private driver data.

.. _`img_ir_priv.definition`:

Definition
----------

.. code-block:: c

    struct img_ir_priv {
        struct device *dev;
        int irq;
        struct clk *clk;
        struct clk *sys_clk;
        void __iomem *reg_base;
        spinlock_t lock;
        struct img_ir_priv_raw raw;
        struct img_ir_priv_hw hw;
    }

.. _`img_ir_priv.members`:

Members
-------

dev
    Platform device.

irq
    IRQ number.

clk
    Input clock.

sys_clk
    System clock.

reg_base
    Iomem base address of IR register block.

lock
    Protects IR registers and variables in this struct.

raw
    Driver data for raw decoder.

hw
    Driver data for hardware decoder.

.. This file was automatic generated / don't edit.

