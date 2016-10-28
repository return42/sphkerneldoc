.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-xgene-sb.c

.. _`xgene_gpio_sb`:

struct xgene_gpio_sb
====================

.. c:type:: struct xgene_gpio_sb

    GPIO-Standby private data structure.

.. _`xgene_gpio_sb.definition`:

Definition
----------

.. code-block:: c

    struct xgene_gpio_sb {
        struct gpio_chip gc;
        void __iomem *regs;
        struct irq_domain *irq_domain;
        u16 irq_start;
        u16 nirq;
        u16 parent_irq_base;
    }

.. _`xgene_gpio_sb.members`:

Members
-------

gc
    memory-mapped GPIO controllers.

regs
    GPIO register base offset

irq_domain
    GPIO interrupt domain

irq_start
    GPIO pin that start support interrupt

nirq
    Number of GPIO pins that supports interrupt

parent_irq_base
    Start parent HWIRQ

.. This file was automatic generated / don't edit.

