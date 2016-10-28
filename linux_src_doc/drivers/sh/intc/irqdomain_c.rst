.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/sh/intc/irqdomain.c

.. _`intc_evt_xlate`:

intc_evt_xlate
==============

.. c:function:: int intc_evt_xlate(struct irq_domain *d, struct device_node *ctrlr, const u32 *intspec, unsigned int intsize, unsigned long *out_hwirq, unsigned int *out_type)

    Generic xlate for vectored IRQs.

    :param struct irq_domain \*d:
        *undescribed*

    :param struct device_node \*ctrlr:
        *undescribed*

    :param const u32 \*intspec:
        *undescribed*

    :param unsigned int intsize:
        *undescribed*

    :param unsigned long \*out_hwirq:
        *undescribed*

    :param unsigned int \*out_type:
        *undescribed*

.. _`intc_evt_xlate.description`:

Description
-----------

This takes care of exception vector to hwirq translation through
by way of \ :c:func:`evt2irq`\  translation.

.. _`intc_evt_xlate.note`:

Note
----

For platforms that use a flat vector space without INTEVT this
basically just mimics \ :c:func:`irq_domain_xlate_onecell`\  by way of a nopped
out \ :c:func:`evt2irq`\  implementation.

.. This file was automatic generated / don't edit.

