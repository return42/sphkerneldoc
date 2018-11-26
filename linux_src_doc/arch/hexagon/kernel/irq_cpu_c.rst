.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/hexagon/kernel/irq_cpu.c

.. _`init_irq`:

init_IRQ
========

.. c:function:: void init_IRQ( void)

    level interrupt controller with 32 total possible interrupts.  When the core is embedded into different systems/platforms, it is typically wrapped by macro cells that provide one or more second-level interrupt controllers that are cascaded into one or more of the first-level interrupts handled here. The precise wiring of these other irqs varies from platform to platform, and are set up & configured in the platform-specific files.

    :param void:
        no arguments
    :type void: 

.. _`init_irq.description`:

Description
-----------

The first-level interrupt controller is wrapped by the VM, which
virtualizes the interrupt controller for us.  It provides a very
simple, fast & efficient API, and so the fasteoi handler is
appropriate for this case.

.. This file was automatic generated / don't edit.

