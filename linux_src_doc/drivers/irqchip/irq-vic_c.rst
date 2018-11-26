.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/irqchip/irq-vic.c

.. _`vic_device`:

struct vic_device
=================

.. c:type:: struct vic_device

    VIC PM device

.. _`vic_device.definition`:

Definition
----------

.. code-block:: c

    struct vic_device {
        void __iomem *base;
        int irq;
        u32 valid_sources;
        u32 resume_sources;
        u32 resume_irqs;
        u32 int_select;
        u32 int_enable;
        u32 soft_int;
        u32 protect;
        struct irq_domain *domain;
    }

.. _`vic_device.members`:

Members
-------

base
    The register base for the VIC.

irq
    The IRQ number for the base of the VIC.

valid_sources
    A bitmask of valid interrupts

resume_sources
    A bitmask of interrupts for resume.

resume_irqs
    The IRQs enabled for resume.

int_select
    Save for VIC_INT_SELECT.

int_enable
    Save for VIC_INT_ENABLE.

soft_int
    Save for VIC_INT_SOFT.

protect
    Save for VIC_PROTECT.

domain
    The IRQ domain for the VIC.

.. _`vic_init2`:

vic_init2
=========

.. c:function:: void vic_init2(void __iomem *base)

    common initialisation code

    :param base:
        Base of the VIC.
    :type base: void __iomem \*

.. _`vic_init2.description`:

Description
-----------

Common initialisation code for registration
and resume.

.. _`vic_pm_init`:

vic_pm_init
===========

.. c:function:: int vic_pm_init( void)

    initicall to register VIC pm

    :param void:
        no arguments
    :type void: 

.. _`vic_pm_init.description`:

Description
-----------

This is called via \ :c:func:`late_initcall`\  to register
the resources for the VICs due to the early
nature of the VIC's registration.

.. _`vic_register`:

vic_register
============

.. c:function:: void vic_register(void __iomem *base, unsigned int parent_irq, unsigned int irq, u32 valid_sources, u32 resume_sources, struct device_node *node)

    Register a VIC.

    :param base:
        The base address of the VIC.
    :type base: void __iomem \*

    :param parent_irq:
        The parent IRQ if cascaded, else 0.
    :type parent_irq: unsigned int

    :param irq:
        The base IRQ for the VIC.
    :type irq: unsigned int

    :param valid_sources:
        bitmask of valid interrupts
    :type valid_sources: u32

    :param resume_sources:
        bitmask of interrupts allowed for resume sources.
    :type resume_sources: u32

    :param node:
        The device tree node associated with the VIC.
    :type node: struct device_node \*

.. _`vic_register.description`:

Description
-----------

Register the VIC with the system device tree so that it can be notified
of suspend and resume requests and ensure that the correct actions are
taken to re-instate the settings on resume.

This also configures the IRQ domain for the VIC.

.. _`vic_init`:

vic_init
========

.. c:function:: void vic_init(void __iomem *base, unsigned int irq_start, u32 vic_sources, u32 resume_sources)

    initialise a vectored interrupt controller

    :param base:
        iomem base address
    :type base: void __iomem \*

    :param irq_start:
        starting interrupt number, must be muliple of 32
    :type irq_start: unsigned int

    :param vic_sources:
        bitmask of interrupt sources to allow
    :type vic_sources: u32

    :param resume_sources:
        bitmask of interrupt sources to allow for resume
    :type resume_sources: u32

.. _`vic_init_cascaded`:

vic_init_cascaded
=================

.. c:function:: int vic_init_cascaded(void __iomem *base, unsigned int parent_irq, u32 vic_sources, u32 resume_sources)

    initialise a cascaded vectored interrupt controller

    :param base:
        iomem base address
    :type base: void __iomem \*

    :param parent_irq:
        the parent IRQ we're cascaded off
    :type parent_irq: unsigned int

    :param vic_sources:
        bitmask of interrupt sources to allow
    :type vic_sources: u32

    :param resume_sources:
        bitmask of interrupt sources to allow for resume
    :type resume_sources: u32

.. _`vic_init_cascaded.description`:

Description
-----------

This returns the base for the new interrupts or negative on error.

.. This file was automatic generated / don't edit.

