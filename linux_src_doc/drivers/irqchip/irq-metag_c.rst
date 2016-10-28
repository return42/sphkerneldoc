.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/irqchip/irq-metag.c

.. _`metag_internal_irq_priv`:

struct metag_internal_irq_priv
==============================

.. c:type:: struct metag_internal_irq_priv

    private meta internal interrupt data

.. _`metag_internal_irq_priv.definition`:

Definition
----------

.. code-block:: c

    struct metag_internal_irq_priv {
        struct irq_domain *domain;
        unsigned long unmasked;
    }

.. _`metag_internal_irq_priv.members`:

Members
-------

domain
    IRQ domain for all internal Meta IRQs (HWSTATMETA)

unmasked
    Record of unmasked IRQs

.. _`metag_internal_irq_mask`:

metag_internal_irq_mask
=======================

.. c:function:: void metag_internal_irq_mask(struct irq_data *data)

    mask an internal irq by unvectoring

    :param struct irq_data \*data:
        data for the internal irq to mask

.. _`metag_internal_irq_mask.description`:

Description
-----------

HWSTATMETA has no mask register. Instead the IRQ is unvectored from the core
and retriggered if necessary later.

.. _`metag_internal_irq_unmask`:

metag_internal_irq_unmask
=========================

.. c:function:: void metag_internal_irq_unmask(struct irq_data *data)

    unmask an edge irq by revectoring

    :param struct irq_data \*data:
        data for the internal irq to unmask

.. _`metag_internal_irq_unmask.description`:

Description
-----------

HWSTATMETA has no mask register. Instead the IRQ is revectored back to the
core and retriggered if necessary.

.. _`internal_irq_map`:

internal_irq_map
================

.. c:function:: int internal_irq_map(unsigned int hw)

    Map an internal meta IRQ to a virtual IRQ number.

    :param unsigned int hw:
        Number of the internal IRQ. Must be in range.

.. _`internal_irq_map.return`:

Return
------

The virtual IRQ number of the Meta internal IRQ specified by
\ ``hw``\ .

.. _`metag_internal_irq_init_cpu`:

metag_internal_irq_init_cpu
===========================

.. c:function:: void metag_internal_irq_init_cpu(struct metag_internal_irq_priv *priv, int cpu)

    regsister with the Meta cpu

    :param struct metag_internal_irq_priv \*priv:
        *undescribed*

    :param int cpu:
        the CPU to register on

.. _`metag_internal_irq_init_cpu.description`:

Description
-----------

Configure \ ``cpu``\ 's TR1 irq so that we can demux irqs.

.. _`metag_internal_intc_map`:

metag_internal_intc_map
=======================

.. c:function:: int metag_internal_intc_map(struct irq_domain *d, unsigned int irq, irq_hw_number_t hw)

    map an internal irq

    :param struct irq_domain \*d:
        irq domain of internal trigger block

    :param unsigned int irq:
        virtual irq number

    :param irq_hw_number_t hw:
        hardware irq number within internal trigger block

.. _`metag_internal_intc_map.description`:

Description
-----------

This sets up a virtual irq for a specified hardware interrupt. The irq chip
and handler is configured.

.. _`init_internal_irq`:

init_internal_IRQ
=================

.. c:function:: int init_internal_IRQ( void)

    register internal IRQs

    :param  void:
        no arguments

.. _`init_internal_irq.description`:

Description
-----------

Register the irq chip and handler function for all internal IRQs

.. This file was automatic generated / don't edit.

