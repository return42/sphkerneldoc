.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/m68k/kernel/ints.c

.. _`m68k_setup_auto_interrupt`:

m68k_setup_auto_interrupt
=========================

.. c:function:: void m68k_setup_auto_interrupt(void (*) handler (unsigned int, struct pt_regs *)

    :param (void (\*) handler (unsigned int, struct pt_regs \*):
        called from auto vector interrupts

.. _`m68k_setup_auto_interrupt.description`:

Description
-----------

setup the handler to be called from auto vector interrupts instead of the
standard \ :c:func:`do_IRQ`\ , it will be called with irq numbers in the range
from IRQ_AUTO_1 - IRQ_AUTO_7.

.. _`m68k_setup_user_interrupt`:

m68k_setup_user_interrupt
=========================

.. c:function:: void m68k_setup_user_interrupt(unsigned int vec, unsigned int cnt)

    :param unsigned int vec:
        first user vector interrupt to handle

    :param unsigned int cnt:
        number of active user vector interrupts

.. _`m68k_setup_user_interrupt.description`:

Description
-----------

setup user vector interrupts, this includes activating the specified range
of interrupts, only then these interrupts can be requested (note: this is
different from auto vector interrupts).

.. _`m68k_setup_irq_controller`:

m68k_setup_irq_controller
=========================

.. c:function:: void m68k_setup_irq_controller(struct irq_chip *chip, irq_flow_handler_t handle, unsigned int irq, unsigned int cnt)

    :param struct irq_chip \*chip:
        irq chip which controls specified irq

    :param irq_flow_handler_t handle:
        flow handler which handles specified irq

    :param unsigned int irq:
        first irq to be managed by the controller

    :param unsigned int cnt:
        number of irqs to be managed by the controller

.. _`m68k_setup_irq_controller.description`:

Description
-----------

Change the controller for the specified range of irq, which will be used to
manage these irq. auto/user irq already have a default controller, which can
be changed as well, but the controller probably should use m68k_irq_startup/
m68k_irq_shutdown.

.. This file was automatic generated / don't edit.

