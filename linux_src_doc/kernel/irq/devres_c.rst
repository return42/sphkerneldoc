.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/irq/devres.c

.. _`devm_request_threaded_irq`:

devm_request_threaded_irq
=========================

.. c:function:: int devm_request_threaded_irq(struct device *dev, unsigned int irq, irq_handler_t handler, irq_handler_t thread_fn, unsigned long irqflags, const char *devname, void *dev_id)

    allocate an interrupt line for a managed device

    :param dev:
        device to request interrupt for
    :type dev: struct device \*

    :param irq:
        Interrupt line to allocate
    :type irq: unsigned int

    :param handler:
        Function to be called when the IRQ occurs
    :type handler: irq_handler_t

    :param thread_fn:
        function to be called in a threaded interrupt context. NULL
        for devices which handle everything in \ ``handler``\ 
    :type thread_fn: irq_handler_t

    :param irqflags:
        Interrupt type flags
    :type irqflags: unsigned long

    :param devname:
        An ascii name for the claiming device, dev_name(dev) if NULL
    :type devname: const char \*

    :param dev_id:
        A cookie passed back to the handler function
    :type dev_id: void \*

.. _`devm_request_threaded_irq.description`:

Description
-----------

Except for the extra \ ``dev``\  argument, this function takes the
same arguments and performs the same function as
\ :c:func:`request_threaded_irq`\ .  IRQs requested with this function will be
automatically freed on driver detach.

If an IRQ allocated with this function needs to be freed
separately, \ :c:func:`devm_free_irq`\  must be used.

.. _`devm_request_any_context_irq`:

devm_request_any_context_irq
============================

.. c:function:: int devm_request_any_context_irq(struct device *dev, unsigned int irq, irq_handler_t handler, unsigned long irqflags, const char *devname, void *dev_id)

    allocate an interrupt line for a managed device

    :param dev:
        device to request interrupt for
    :type dev: struct device \*

    :param irq:
        Interrupt line to allocate
    :type irq: unsigned int

    :param handler:
        Function to be called when the IRQ occurs
    :type handler: irq_handler_t

    :param irqflags:
        Interrupt type flags
    :type irqflags: unsigned long

    :param devname:
        An ascii name for the claiming device, dev_name(dev) if NULL
    :type devname: const char \*

    :param dev_id:
        A cookie passed back to the handler function
    :type dev_id: void \*

.. _`devm_request_any_context_irq.description`:

Description
-----------

Except for the extra \ ``dev``\  argument, this function takes the
same arguments and performs the same function as
\ :c:func:`request_any_context_irq`\ .  IRQs requested with this function will be
automatically freed on driver detach.

If an IRQ allocated with this function needs to be freed
separately, \ :c:func:`devm_free_irq`\  must be used.

.. _`devm_free_irq`:

devm_free_irq
=============

.. c:function:: void devm_free_irq(struct device *dev, unsigned int irq, void *dev_id)

    free an interrupt

    :param dev:
        device to free interrupt for
    :type dev: struct device \*

    :param irq:
        Interrupt line to free
    :type irq: unsigned int

    :param dev_id:
        Device identity to free
    :type dev_id: void \*

.. _`devm_free_irq.description`:

Description
-----------

Except for the extra \ ``dev``\  argument, this function takes the
same arguments and performs the same function as \ :c:func:`free_irq`\ .
This function instead of \ :c:func:`free_irq`\  should be used to manually
free IRQs allocated with \ :c:func:`devm_request_irq`\ .

.. _`__devm_irq_alloc_descs`:

\__devm_irq_alloc_descs
=======================

.. c:function:: int __devm_irq_alloc_descs(struct device *dev, int irq, unsigned int from, unsigned int cnt, int node, struct module *owner, const struct cpumask *affinity)

    Allocate and initialize a range of irq descriptors for a managed device

    :param dev:
        Device to allocate the descriptors for
    :type dev: struct device \*

    :param irq:
        Allocate for specific irq number if irq >= 0
    :type irq: int

    :param from:
        Start the search from this irq number
    :type from: unsigned int

    :param cnt:
        Number of consecutive irqs to allocate
    :type cnt: unsigned int

    :param node:
        Preferred node on which the irq descriptor should be allocated
    :type node: int

    :param owner:
        Owning module (can be NULL)
    :type owner: struct module \*

    :param affinity:
        Optional pointer to an affinity mask array of size \ ``cnt``\ 
        which hints where the irq descriptors should be allocated
        and which default affinities to use
    :type affinity: const struct cpumask \*

.. _`__devm_irq_alloc_descs.description`:

Description
-----------

Returns the first irq number or error code.

.. _`__devm_irq_alloc_descs.note`:

Note
----

Use the provided wrappers (devm_irq_alloc_desc\*) for simplicity.

.. _`devm_irq_alloc_generic_chip`:

devm_irq_alloc_generic_chip
===========================

.. c:function:: struct irq_chip_generic *devm_irq_alloc_generic_chip(struct device *dev, const char *name, int num_ct, unsigned int irq_base, void __iomem *reg_base, irq_flow_handler_t handler)

    Allocate and initialize a generic chip for a managed device

    :param dev:
        Device to allocate the generic chip for
    :type dev: struct device \*

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

.. _`devm_irq_alloc_generic_chip.description`:

Description
-----------

Returns an initialized irq_chip_generic structure. The chip defaults
to the primary (index 0) irq_chip_type and \ ``handler``\ 

.. _`devm_irq_setup_generic_chip`:

devm_irq_setup_generic_chip
===========================

.. c:function:: int devm_irq_setup_generic_chip(struct device *dev, struct irq_chip_generic *gc, u32 msk, enum irq_gc_flags flags, unsigned int clr, unsigned int set)

    Setup a range of interrupts with a generic chip for a managed device

    :param dev:
        Device to setup the generic chip for
    :type dev: struct device \*

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
        IRQ\_\* bits to clear
    :type clr: unsigned int

    :param set:
        IRQ\_\* bits to set
    :type set: unsigned int

.. _`devm_irq_setup_generic_chip.description`:

Description
-----------

Set up max. 32 interrupts starting from gc->irq_base. Note, this
initializes all interrupts to the primary irq_chip_type and its
associated handler.

.. This file was automatic generated / don't edit.

