.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/irqchip/irq-brcmstb-l2.c

.. _`brcmstb_l2_mask_and_ack`:

brcmstb_l2_mask_and_ack
=======================

.. c:function:: void brcmstb_l2_mask_and_ack(struct irq_data *d)

    Mask and ack pending interrupt

    :param struct irq_data \*d:
        irq_data

.. _`brcmstb_l2_mask_and_ack.description`:

Description
-----------

Chip has separate enable/disable registers instead of a single mask
register and pending interrupt is acknowledged by setting a bit.

.. _`brcmstb_l2_mask_and_ack.note`:

Note
----

This function is generic and could easily be added to the
generic irqchip implementation if there ever becomes a will to do so.
Perhaps with a name like \ :c:func:`irq_gc_mask_disable_and_ack_set`\ .

e.g.: https://patchwork.kernel.org/patch/9831047/

.. This file was automatic generated / don't edit.

