.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/irqchip/irq-imgpdc.c

.. _`pdc_intc_priv`:

struct pdc_intc_priv
====================

.. c:type:: struct pdc_intc_priv

    private pdc interrupt data.

.. _`pdc_intc_priv.definition`:

Definition
----------

.. code-block:: c

    struct pdc_intc_priv {
        unsigned int nr_perips;
        unsigned int nr_syswakes;
        unsigned int *perip_irqs;
        unsigned int syswake_irq;
        struct irq_domain *domain;
        void __iomem *pdc_base;
        u32 irq_route;
        raw_spinlock_t lock;
    }

.. _`pdc_intc_priv.members`:

Members
-------

nr_perips
    Number of peripheral interrupt signals.

nr_syswakes
    Number of syswake signals.

perip_irqs
    List of peripheral IRQ numbers handled.

syswake_irq
    Shared PDC syswake IRQ number.

domain
    IRQ domain for PDC peripheral and syswake IRQs.

pdc_base
    Base of PDC registers.

irq_route
    Cached version of PDC_IRQ_ROUTE register.

lock
    Lock to protect the PDC syswake registers and the cached
    values of those registers in this struct.

.. This file was automatic generated / don't edit.

