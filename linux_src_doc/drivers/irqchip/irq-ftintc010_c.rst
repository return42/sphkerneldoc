.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/irqchip/irq-ftintc010.c

.. _`ft010_irq_data`:

struct ft010_irq_data
=====================

.. c:type:: struct ft010_irq_data

    irq data container for the Faraday IRQ controller

.. _`ft010_irq_data.definition`:

Definition
----------

.. code-block:: c

    struct ft010_irq_data {
        void __iomem *base;
        struct irq_chip chip;
        struct irq_domain *domain;
    }

.. _`ft010_irq_data.members`:

Members
-------

base
    memory offset in virtual memory

chip
    chip container for this instance

domain
    IRQ domain for this instance

.. This file was automatic generated / don't edit.

