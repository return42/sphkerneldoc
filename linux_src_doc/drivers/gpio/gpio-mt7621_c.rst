.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-mt7621.c

.. _`mtk`:

struct mtk
==========

.. c:type:: struct mtk

    state container for data of the platform driver. It is 3 separate gpio-chip each one with its own irq_chip.

.. _`mtk.definition`:

Definition
----------

.. code-block:: c

    struct mtk {
        struct device *dev;
        void __iomem *base;
        int gpio_irq;
        struct mtk_gc gc_map[MTK_BANK_CNT];
    }

.. _`mtk.members`:

Members
-------

dev
    device instance

base
    memory base address

gpio_irq
    irq number from the device tree

gc_map
    array of the gpio chips

.. This file was automatic generated / don't edit.

