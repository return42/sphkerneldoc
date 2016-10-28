.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/irqchip/irq-versatile-fpga.c

.. _`fpga_irq_data`:

struct fpga_irq_data
====================

.. c:type:: struct fpga_irq_data

    irq data container for the FPGA IRQ controller

.. _`fpga_irq_data.definition`:

Definition
----------

.. code-block:: c

    struct fpga_irq_data {
        void __iomem *base;
        struct irq_chip chip;
        u32 valid;
        struct irq_domain *domain;
        u8 used_irqs;
    }

.. _`fpga_irq_data.members`:

Members
-------

base
    memory offset in virtual memory

chip
    chip container for this instance

valid
    mask for valid IRQs on this controller

domain
    IRQ domain for this instance

used_irqs
    number of active IRQs on this controller

.. This file was automatic generated / don't edit.

