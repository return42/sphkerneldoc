.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/52xx/mpc52xx_pic.c

.. _`mpc52xx_is_extirq`:

mpc52xx_is_extirq
=================

.. c:function:: int mpc52xx_is_extirq(int l1, int l2)

    Returns true if hwirq number is for an external IRQ

    :param l1:
        *undescribed*
    :type l1: int

    :param l2:
        *undescribed*
    :type l2: int

.. _`mpc52xx_irqhost_xlate`:

mpc52xx_irqhost_xlate
=====================

.. c:function:: int mpc52xx_irqhost_xlate(struct irq_domain *h, struct device_node *ct, const u32 *intspec, unsigned int intsize, irq_hw_number_t *out_hwirq, unsigned int *out_flags)

    translate virq# from device tree interrupts property

    :param h:
        *undescribed*
    :type h: struct irq_domain \*

    :param ct:
        *undescribed*
    :type ct: struct device_node \*

    :param intspec:
        *undescribed*
    :type intspec: const u32 \*

    :param intsize:
        *undescribed*
    :type intsize: unsigned int

    :param out_hwirq:
        *undescribed*
    :type out_hwirq: irq_hw_number_t \*

    :param out_flags:
        *undescribed*
    :type out_flags: unsigned int \*

.. _`mpc52xx_irqhost_map`:

mpc52xx_irqhost_map
===================

.. c:function:: int mpc52xx_irqhost_map(struct irq_domain *h, unsigned int virq, irq_hw_number_t irq)

    Hook to map from virq to an irq_chip structure

    :param h:
        *undescribed*
    :type h: struct irq_domain \*

    :param virq:
        *undescribed*
    :type virq: unsigned int

    :param irq:
        *undescribed*
    :type irq: irq_hw_number_t

.. _`mpc52xx_init_irq`:

mpc52xx_init_irq
================

.. c:function:: void mpc52xx_init_irq( void)

    Initialize and register with the virq subsystem

    :param void:
        no arguments
    :type void: 

.. _`mpc52xx_init_irq.description`:

Description
-----------

Hook for setting up IRQs on an mpc5200 system.  A pointer to this function
is to be put into the machine definition structure.

This function searches the device tree for an MPC5200 interrupt controller,
initializes it, and registers it with the virq subsystem.

.. _`mpc52xx_get_irq`:

mpc52xx_get_irq
===============

.. c:function:: unsigned int mpc52xx_get_irq( void)

    Get pending interrupt number hook function

    :param void:
        no arguments
    :type void: 

.. _`mpc52xx_get_irq.description`:

Description
-----------

Called by the interrupt handler to determine what IRQ handler needs to be
executed.

Status of pending interrupts is determined by reading the encoded status
register.  The encoded status register has three fields; one for each of the
types of interrupts defined by the controller - 'critical', 'main' and
'peripheral'.  This function reads the status register and returns the IRQ
number associated with the highest priority pending interrupt.  'Critical'
interrupts have the highest priority, followed by 'main' interrupts, and
then 'peripheral'.

The mpc5200 interrupt controller can be configured to boost the priority
of individual 'peripheral' interrupts.  If this is the case then a special
value will appear in either the crit or main fields indicating a high
or medium priority peripheral irq has occurred.

This function checks each of the 3 irq request fields and returns the
first pending interrupt that it finds.

This function also identifies a 4th type of interrupt; 'bestcomm'.  Each
bestcomm DMA task can raise the bestcomm peripheral interrupt.  When this
occurs at task-specific IRQ# is decoded so that each task can have its
own IRQ handler.

.. This file was automatic generated / don't edit.

