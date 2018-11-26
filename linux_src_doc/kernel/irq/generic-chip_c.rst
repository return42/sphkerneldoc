.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/irq/generic-chip.c

.. _`irq_gc_noop`:

irq_gc_noop
===========

.. c:function:: void irq_gc_noop(struct irq_data *d)

    NOOP function

    :param d:
        irq_data
    :type d: struct irq_data \*

.. _`irq_gc_mask_disable_reg`:

irq_gc_mask_disable_reg
=======================

.. c:function:: void irq_gc_mask_disable_reg(struct irq_data *d)

    Mask chip via disable register

    :param d:
        irq_data
    :type d: struct irq_data \*

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

    :param d:
        irq_data
    :type d: struct irq_data \*

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

    :param d:
        irq_data
    :type d: struct irq_data \*

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

    :param d:
        irq_data
    :type d: struct irq_data \*

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

    :param d:
        irq_data
    :type d: struct irq_data \*

.. _`irq_gc_ack_clr_bit`:

irq_gc_ack_clr_bit
==================

.. c:function:: void irq_gc_ack_clr_bit(struct irq_data *d)

    Ack pending interrupt via clearing bit

    :param d:
        irq_data
    :type d: struct irq_data \*

.. _`irq_gc_mask_disable_and_ack_set`:

irq_gc_mask_disable_and_ack_set
===============================

.. c:function:: void irq_gc_mask_disable_and_ack_set(struct irq_data *d)

    Mask and ack pending interrupt

    :param d:
        irq_data
    :type d: struct irq_data \*

.. _`irq_gc_mask_disable_and_ack_set.description`:

Description
-----------

This generic implementation of the irq_mask_ack method is for chips
with separate enable/disable registers instead of a single mask
register and where a pending interrupt is acknowledged by setting a
bit.

.. _`irq_gc_mask_disable_and_ack_set.note`:

Note
----

This is the only permutation currently used.  Similar generic
functions should be added here if other permutations are required.

.. _`irq_gc_eoi`:

irq_gc_eoi
==========

.. c:function:: void irq_gc_eoi(struct irq_data *d)

    EOI interrupt

    :param d:
        irq_data
    :type d: struct irq_data \*

.. _`irq_gc_set_wake`:

irq_gc_set_wake
===============

.. c:function:: int irq_gc_set_wake(struct irq_data *d, unsigned int on)

    Set/clr wake bit for an interrupt

    :param d:
        irq_data
    :type d: struct irq_data \*

    :param on:
        Indicates whether the wake bit should be set or cleared
    :type on: unsigned int

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

    :param name:
        Name of the irq chip
    :type name: const char \*

    :param num_ct:
        Number of irq_chip_type instances associated with this
    :type num_ct: int

    :param irq_base:
        Interrupt base nr for this chip
    :type irq_base: unsigned int

    :param reg_base:
        Register base address (virtual)
    :type reg_base: void __iomem \*

    :param handler:
        Default flow handler associated with this chip
    :type handler: irq_flow_handler_t

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

    :param d:
        irq domain for which to allocate chips
    :type d: struct irq_domain \*

    :param irqs_per_chip:
        Number of interrupts each chip handles (max 32)
    :type irqs_per_chip: int

    :param num_ct:
        Number of irq_chip_type instances associated with this
    :type num_ct: int

    :param name:
        Name of the irq chip
    :type name: const char \*

    :param handler:
        Default flow handler associated with these chips
    :type handler: irq_flow_handler_t

    :param clr:
        IRQ_* bits to clear in the mapping function
    :type clr: unsigned int

    :param set:
        IRQ_* bits to set in the mapping function
    :type set: unsigned int

    :param gcflags:
        Generic chip specific setup flags
    :type gcflags: enum irq_gc_flags

.. _`irq_get_domain_generic_chip`:

irq_get_domain_generic_chip
===========================

.. c:function:: struct irq_chip_generic *irq_get_domain_generic_chip(struct irq_domain *d, unsigned int hw_irq)

    Get a pointer to the generic chip of a hw_irq

    :param d:
        irq domain pointer
    :type d: struct irq_domain \*

    :param hw_irq:
        Hardware interrupt number
    :type hw_irq: unsigned int

.. _`irq_setup_generic_chip`:

irq_setup_generic_chip
======================

.. c:function:: void irq_setup_generic_chip(struct irq_chip_generic *gc, u32 msk, enum irq_gc_flags flags, unsigned int clr, unsigned int set)

    Setup a range of interrupts with a generic chip

    :param gc:
        Generic irq chip holding all data
    :type gc: struct irq_chip_generic \*

    :param msk:
        Bitmask holding the irqs to initialize relative to gc->irq_base
    :type msk: u32

    :param flags:
        Flags for initialization
    :type flags: enum irq_gc_flags

    :param clr:
        IRQ_* bits to clear
    :type clr: unsigned int

    :param set:
        IRQ_* bits to set
    :type set: unsigned int

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

    :param d:
        irq_data for this interrupt
    :type d: struct irq_data \*

    :param type:
        Flow type to be initialized
    :type type: unsigned int

.. _`irq_setup_alt_chip.description`:

Description
-----------

Only to be called from chip->irq_set_type() callbacks.

.. _`irq_remove_generic_chip`:

irq_remove_generic_chip
=======================

.. c:function:: void irq_remove_generic_chip(struct irq_chip_generic *gc, u32 msk, unsigned int clr, unsigned int set)

    Remove a chip

    :param gc:
        Generic irq chip holding all data
    :type gc: struct irq_chip_generic \*

    :param msk:
        Bitmask holding the irqs to initialize relative to gc->irq_base
    :type msk: u32

    :param clr:
        IRQ_* bits to clear
    :type clr: unsigned int

    :param set:
        IRQ_* bits to set
    :type set: unsigned int

.. _`irq_remove_generic_chip.description`:

Description
-----------

Remove up to 32 interrupts starting from gc->irq_base.

.. This file was automatic generated / don't edit.

