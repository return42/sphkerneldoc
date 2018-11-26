.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/irqchip/irq-crossbar.c

.. _`crossbar_device`:

struct crossbar_device
======================

.. c:type:: struct crossbar_device

    crossbar device description

.. _`crossbar_device.definition`:

Definition
----------

.. code-block:: c

    struct crossbar_device {
        raw_spinlock_t lock;
        uint int_max;
        uint safe_map;
        uint max_crossbar_sources;
        uint *irq_map;
        void __iomem *crossbar_base;
        int *register_offsets;
        void (*write)(int, int);
    }

.. _`crossbar_device.members`:

Members
-------

lock
    spinlock serializing access to \ ``irq_map``\ 

int_max
    maximum number of supported interrupts

safe_map
    safe default value to initialize the crossbar

max_crossbar_sources
    Maximum number of crossbar sources

irq_map
    array of interrupts to crossbar number mapping

crossbar_base
    crossbar base address

register_offsets
    offsets for each irq number

write
    register write function pointer

.. _`crossbar_domain_free`:

crossbar_domain_free
====================

.. c:function:: void crossbar_domain_free(struct irq_domain *domain, unsigned int virq, unsigned int nr_irqs)

    unmap/free a crossbar<->irq connection

    :param domain:
        domain of irq to unmap
    :type domain: struct irq_domain \*

    :param virq:
        virq number
    :type virq: unsigned int

    :param nr_irqs:
        number of irqs to free
    :type nr_irqs: unsigned int

.. _`crossbar_domain_free.description`:

Description
-----------

We do not maintain a use count of total number of map/unmap
calls for a particular irq to find out if a irq can be really
unmapped. This is because unmap is called during irq_dispose_mapping(irq),
after which irq is anyways unusable. So an explicit map has to be called
after that.

.. This file was automatic generated / don't edit.

