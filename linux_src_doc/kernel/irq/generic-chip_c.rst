.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/irq/generic-chip.c

.. _`irq_gc_noop`:

irq_gc_noop
===========

.. c:function:: void irq_gc_noop(struct irq_data *d)

    NOOP function

    :param struct irq_data \*d:
        irq_data

.. _`irq_gc_mask_disable_reg`:

irq_gc_mask_disable_reg
=======================

.. c:function:: void irq_gc_mask_disable_reg(struct irq_data *d)

    Mask chip via disable register

    :param struct irq_data \*d:
        irq_data

.. _`irq_gc_mask_disable_reg.description`:

Description
-----------

Chip has separate enable/disable registers instead of a single mask
register.

.. _`irq_gc_mask_set_bit`:

irq_gc_mask_set_bit
===================

.. c:function:: void irq_gc_mask_set_bit(struct irq_data *d)

    Mask chip via setting bit in mask register

    :param struct irq_data \*d:
        irq_data

.. _`irq_gc_mask_set_bit.description`:

Description
-----------

Chip has a single mask register. Values of this register are cached
and protected by gc->lock

.. _`irq_gc_mask_clr_bit`:

irq_gc_mask_clr_bit
===================

.. c:function:: void irq_gc_mask_clr_bit(struct irq_data *d)

    Mask chip via clearing bit in mask register

    :param struct irq_data \*d:
        irq_data

.. _`irq_gc_mask_clr_bit.description`:

Description
-----------

Chip has a single mask register. Values of this register are cached
and protected by gc->lock

.. _`irq_gc_unmask_enable_reg`:

irq_gc_unmask_enable_reg
========================

.. c:function:: void irq_gc_unmask_enable_reg(struct irq_data *d)

    Unmask chip via enable register

    :param struct irq_data \*d:
        irq_data

.. _`irq_gc_unmask_enable_reg.description`:

Description
-----------

Chip has separate enable/disable registers instead of a single mask
register.

.. _`irq_gc_ack_set_bit`:

irq_gc_ack_set_bit
==================

.. c:function:: void irq_gc_ack_set_bit(struct irq_data *d)

    Ack pending interrupt via setting bit

    :param struct irq_data \*d:
        irq_data

.. _`irq_gc_ack_clr_bit`:

irq_gc_ack_clr_bit
==================

.. c:function:: void irq_gc_ack_clr_bit(struct irq_data *d)

    Ack pending interrupt via clearing bit

    :param struct irq_data \*d:
        irq_data

.. _`irq_gc_mask_disable_reg_and_ack`:

irq_gc_mask_disable_reg_and_ack
===============================

.. c:function:: void irq_gc_mask_disable_reg_and_ack(struct irq_data *d)

    Mask and ack pending interrupt

    :param struct irq_data \*d:
        irq_data

.. _`irq_gc_eoi`:

irq_gc_eoi
==========

.. c:function:: void irq_gc_eoi(struct irq_data *d)

    EOI interrupt

    :param struct irq_data \*d:
        irq_data

.. _`irq_gc_set_wake`:

irq_gc_set_wake
===============

.. c:function:: int irq_gc_set_wake(struct irq_data *d, unsigned int on)

    Set/clr wake bit for an interrupt

    :param struct irq_data \*d:
        irq_data

    :param unsigned int on:
        Indicates whether the wake bit should be set or cleared

.. _`irq_gc_set_wake.description`:

Description
-----------

For chips where the wake from suspend functionality is not
configured in a separate register and the wakeup active state is
just stored in a bitmask.

.. _`irq_alloc_generic_chip`:

irq_alloc_generic_chip
======================

.. c:function:: struct irq_chip_generic *irq_alloc_generic_chip(const char *name, int num_ct, unsigned int irq_base, void __iomem *reg_base, irq_flow_handler_t handler)

    Allocate a generic chip and initialize it

    :param const char \*name:
        Name of the irq chip

    :param int num_ct:
        Number of irq_chip_type instances associated with this

    :param unsigned int irq_base:
        Interrupt base nr for this chip

    :param void __iomem \*reg_base:
        Register base address (virtual)

    :param irq_flow_handler_t handler:
        Default flow handler associated with this chip

.. _`irq_alloc_generic_chip.description`:

Description
-----------

Returns an initialized irq_chip_generic structure. The chip defaults
to the primary (index 0) irq_chip_type and \ ``handler``\ 

.. _`__irq_alloc_domain_generic_chips`:

__irq_alloc_domain_generic_chips
================================

.. c:function:: int __irq_alloc_domain_generic_chips(struct irq_domain *d, int irqs_per_chip, int num_ct, const char *name, irq_flow_handler_t handler, unsigned int clr, unsigned int set, enum irq_gc_flags gcflags)

    Allocate generic chips for an irq domain

    :param struct irq_domain \*d:
        irq domain for which to allocate chips

    :param int irqs_per_chip:
        Number of interrupts each chip handles (max 32)

    :param int num_ct:
        Number of irq_chip_type instances associated with this

    :param const char \*name:
        Name of the irq chip

    :param irq_flow_handler_t handler:
        Default flow handler associated with these chips

    :param unsigned int clr:
        IRQ_* bits to clear in the mapping function

    :param unsigned int set:
        IRQ_* bits to set in the mapping function

    :param enum irq_gc_flags gcflags:
        Generic chip specific setup flags

.. _`irq_get_domain_generic_chip`:

irq_get_domain_generic_chip
===========================

.. c:function:: struct irq_chip_generic *irq_get_domain_generic_chip(struct irq_domain *d, unsigned int hw_irq)

    Get a pointer to the generic chip of a hw_irq

    :param struct irq_domain \*d:
        irq domain pointer

    :param unsigned int hw_irq:
        Hardware interrupt number

.. _`irq_setup_generic_chip`:

irq_setup_generic_chip
======================

.. c:function:: void irq_setup_generic_chip(struct irq_chip_generic *gc, u32 msk, enum irq_gc_flags flags, unsigned int clr, unsigned int set)

    Setup a range of interrupts with a generic chip

    :param struct irq_chip_generic \*gc:
        Generic irq chip holding all data

    :param u32 msk:
        Bitmask holding the irqs to initialize relative to gc->irq_base

    :param enum irq_gc_flags flags:
        Flags for initialization

    :param unsigned int clr:
        IRQ_* bits to clear

    :param unsigned int set:
        IRQ_* bits to set

.. _`irq_setup_generic_chip.description`:

Description
-----------

Set up max. 32 interrupts starting from gc->irq_base. Note, this
initializes all interrupts to the primary irq_chip_type and its
associated handler.

.. _`irq_setup_alt_chip`:

irq_setup_alt_chip
==================

.. c:function:: int irq_setup_alt_chip(struct irq_data *d, unsigned int type)

    Switch to alternative chip

    :param struct irq_data \*d:
        irq_data for this interrupt

    :param unsigned int type:
        Flow type to be initialized

.. _`irq_setup_alt_chip.description`:

Description
-----------

Only to be called from chip->irq_set_type() callbacks.

.. _`irq_remove_generic_chip`:

irq_remove_generic_chip
=======================

.. c:function:: void irq_remove_generic_chip(struct irq_chip_generic *gc, u32 msk, unsigned int clr, unsigned int set)

    Remove a chip

    :param struct irq_chip_generic \*gc:
        Generic irq chip holding all data

    :param u32 msk:
        Bitmask holding the irqs to initialize relative to gc->irq_base

    :param unsigned int clr:
        IRQ_* bits to clear

    :param unsigned int set:
        IRQ_* bits to set

.. _`irq_remove_generic_chip.description`:

Description
-----------

Remove up to 32 interrupts starting from gc->irq_base.

.. This file was automatic generated / don't edit.

